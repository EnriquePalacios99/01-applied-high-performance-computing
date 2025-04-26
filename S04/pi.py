from mpi4py import MPI
import time
import math

t0 = time.time()

# 1. Inicialice el universo de procesos y parametros 
#    rank (id del proceso) y nproc (numero de procesos)
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()

# 2. cantidad de intervalos de integracion
nsteps = 1024 # use cantidades variables desde 2^10 a 2^24
# ancho de cada intervalo (eje x)
dx = 1.0 / nsteps

# se definen parametros de particionamiento de datos en el maestro
if rank == 0:
    # tamanho de cada sub-dominio
    ave, res = divmod(nsteps, nprocs)
    counts = [ave + 1 if p < res else ave for p in range(nprocs)]

    # inicio y fin de indices de cada sub-dominio
    starts = [sum(counts[:p]) for p in range(nprocs)]
    ends = [sum(counts[:p+1]) for p in range(nprocs)]

    # se almacena inicio y fin en data
    data = [(starts[p], ends[p]) for p in range(nprocs)]
else:
    data = None

# 3. se distribuyen los datos entre procesos (scatter)
#    utilice comm.scatter(...)
data = comm.scatter(data, root=0)

# cada proceso realiza un calculo parcial (integracion)
partial_pi = 0.0
for i in range(data[0], data[1]):
    x = (i + 0.5) * dx
    partial_pi += 4.0 / (1.0 + x * x)
partial_pi *= dx

# 4. se recolectan resultados parciales 
#    use comm.gather(...)
partial_pi = comm.gather(partial_pi,root=0)

# calculo del resultado final en el maestro
if rank == 0:
    print('pi computed in {:.3f} sec'.format(time.time() - t0))
    print('error is {}'.format(abs(sum(partial_pi) - math.pi)))

