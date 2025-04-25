# Apuntes de Clase - CURSO
## Applied High Performance Computing
### Fundamentos en HPC: DAG-PRAM
**Profesor:** José Fiestas - UTEC

---

### Resumen:
* Parallel RAM (PRAM)
* Diagramas acíclicos dirigidos (DAGs), métricas de performance
* Fundamentos de escalabilidad

---

## Unidad 1: Diagramas acíclicos dirigidos (DAGs)

### Clasificación de algoritmos paralelos:
* **Secuenciales:** No pueden ser paralelizados debido a dependencias.
    * Ejemplo: Sistemas de navegación aérea
* **Paralelos:** Las tareas se ejecutan de forma simultánea.
    * Ejemplo: Procesamiento gráfico simple (intensidad, rotación, desplazamiento)
* **Secuencial-Paralelo:** Niveles en paralelo que se ejecutan secuencialmente.
    * Ejemplo: Modelo climático, ML
* **No-Secuencial-Paralelo:** No hay un patrón aplicable.
    * Ejemplo: Dinámica de fluidos, búsqueda

### Modelo de costo DAG
El *scheduling* (plan de ejecución) asigna a cada nodo (tarea) del DAG:
* Un tiempo de ejecución $t_i$
* Un proceso $p_i$

El algoritmo se ejecuta en un tiempo conocido como **Span**.

El **Trabajo (W)** del algoritmo en paralelo se define como el tiempo secuencial óptimo ($T_s^*$).

Se busca obtener un trabajo y span mínimo.

En paralelo, $p$ procesos ejecutan en por lo menos $T_s / p$ unidades de tiempo.

### Métricas de Performance
* **Speedup (Velocidad):** $S = T_s / T_p$
    * $S \sim p$ es un *speedup*-óptimo (lineal).
* **Eficiencia:** $E = S / p$ (carga promedio por proceso).
* **Escalabilidad:** Mantiene la eficiencia constante si se incrementa el número de procesadores ($p$) a la vez que la carga de datos ($n$).
    * Es decir, si problemas grandes pueden ser resueltos con la misma eficiencia que problemas pequeños.

### Tipos de Escalabilidad:
* **Escalabilidad fuerte:** Solo crece el número de procesos ($p$).
* **Escalabilidad débil:** Crece tanto el número de procesos ($p$) como la cantidad de datos ($n$).

---

## Tarea 1a: DAG - métricas de performance

### Ejemplo 01:
Determine Span y $W$ en el siguiente DAG si cada tarea tiene complejidad constante.

### Ejemplo 02:
La Suma de Números se utiliza como una operación básica en algoritmos de regresión logística, gradiente descendente, random forest o X-GBoost.
* Construya un DAG eficiente para la suma de $n$ enteros en paralelo, si se tiene $n=16$ (datos), $p=8$ (procesadores disponibles).
* Compare el DAG con el caso $n=16$, $p=5$.
* Determine $T_s$, $T_\infty(n)$, $W(n)$, $S(n)$ en cada caso.

### Ejemplo 03:
Diagrame el DAG correspondiente al siguiente código:



--------------

Las funciones leen y modifican ambos argumentos.

Determine Span del algoritmo paralelo asumiendo una complejidad constante de las tareas.

Recalcule las métricas si $T_1, T_2, T_5 = O(n)$, $T_3 = O(n \log(n))$, $T_4 = \log(n)$, $T_6 = O(n^2)$.

---

## Unidad 2: FUNDAMENTOS DE ESCALABILIDAD

### Tiempo de ejecución ($T_p$):
Consiste en el tiempo necesario para completar la ejecución del algoritmo en paralelo. Está compuesto por el **Tiempo de cómputo ($T_{comp}$)** y el **tiempo de comunicación ($T_{comm}$)**.

### Speedup ($S$):
Dado por la relación $T_s / T_p$. Se aproxima al *speedup* ideal ($\sim p$) en un rango determinado de procesos.

### Eficiencia ($E$):
Dado por la relación $S / p$. Se aproxima a la eficiencia ideal ($\sim 1$) en un rango determinado de procesos.

### Relación entre $T$, $S$, $E$:
$E = \frac{T_s}{p \cdot T_p} = \frac{S}{p}$

---

## Tarea 1b: Análisis de escalabilidad

### Caso 1: Strong scaling
Novoa & Badia, 2023, *Scalable Random Forest with Data-Parallel Computing*

Describa cómo se deriva la curva de *speedup* (derecha) de los tiempos de ejecución (izquierda). ¿Cuál algoritmo es más escalable en cada *dataset*?

### Caso 2: Weak scaling
Novoa & Badia, 2023, *Scalable Random Forest with Data-Parallel Computing*

Describa cómo se deriva la curva de eficiencia (derecha) de los tiempos de ejecución (izquierda). ¿Cuál algoritmo es más escalable en cada *dataset*?

---

## Unidad 3: PARALLEL RAM (PRAM)

### Problemas “naturalmente” paralelizables
El modelo PRAM consiste en un conjunto de procesadores idénticos $\{P_1, P_2, ..., P_n\}$, con acceso a una memoria compartida para lectura/escritura de datos.

Cada procesador es un RAM, que ejecuta el mismo código en forma sincrónica. No existe una red entre procesos, sino que se comunican a través de la memoria común. Cada proceso, en cada paso, ejecuta:
* Lectura de data de la memoria común
* Ejecución local de instrucciones
* Escritura de data en la memoria común

### Clasificación PRAM
Clasificación según acceso en paralelo a registros de memoria:
{exclusive, concurrent}read {exclusive, concurrent}write
* **EREW (Exclusive Read Exclusive Write):** Cada locación de memoria puede ser leída o escrita por un solo proceso a la vez.
* **CREW (Concurrent Read Exclusive Write):** Múltiples procesos pueden leer la memoria pero solo uno puede escribir en ella durante el mismo paso (Broadcast).
* **ERCW (Exclusive Read Concurrent Write):** Se permite escritura simultánea, pero la lectura es exclusiva en el mismo paso. No es muy usada.
* **CRCW (Concurrent Read Concurrent Write):** Múltiples procesos pueden leer y escribir en el mismo paso.
    * Ejemplo: Búsqueda de un valor en un array de dimensión $n$, dados $p$ procesos ($p < n$). ¿Cuál será el mejor método?

### Paradigma Work-Time (WT)
Dado un algoritmo paralelo con tiempo de ejecución $T_\infty(n)$ y un total de $W(n)$ operaciones (tareas), este puede simularse en un PRAM de $p$ procesos en $O(W(n)/p + T_\infty(n))$ tiempo.

Para la suma de números:

### Pseudocódigo (secuencial)

------------------------


### Modelo formal PRAM
El lenguaje formal utiliza `pardo` (`do in parallel`).

---------------


**Condición:** $n = p$
Se asignan $n$ elementos de $A$ a $B$ en paralelo. Es decir, si $n=p$, un elemento por proceso.
El bloque `for` se ejecuta en forma concurrente.
I.e. proceso $P_1$ asigna $B[1]$ a $A[1]$, proceso $P_2$ asigna $B[2]$ a $A[2]$, etc.

### Caso 1: Global OR / AND
**Global OR:**

----------------------


Cada proceso evalúa la condición `if` y modifica el valor de `Result` si $x[i] = 1$.

**Global AND:**

--------------

Cada proceso evalúa la condición `if` y modifica el valor de `Result` si $x[i] = 0$.

### Caso 2: Máximo de $n$ números

-----------


Cada proceso compara el valor de un elemento del array con otro del mismo array $A$.
El índice del elemento de $A$ donde el array booleano $M$ sea 1 sería el máximo de $A$.

El máximo de $n$ números se puede calcular en $O(1)$ usando $n^2$ procesadores, lo que lo hace impracticable para $n$ grande.
* En forma secuencial, $P(n) = 1$, $T(n) = O(n)$.
* En paralelo, $P(n) = O(n^2)$, $T(n) = O(1) \rightarrow C_p(n) = O(n^2)$.
* $S(n) = O(n) / O(1) = O(n)$.
* $E(n) = O(n) / O(n^2) = O(1/n)$.
* Optimiza solo $T(n)$ sin considerar $P(n)$.

### Caso 3: Suma de $n$ números
En el paso 1 se ejecutan $n/2$ operaciones.
En el paso 2 se ejecutan $n/4$ operaciones.
...
En el paso $\log_2(n)$ se ejecuta 1 operación.

---

## Resumen:
* Se reconocen distintos tipos de DAG, para distintas aplicaciones.
* Se comprenden los principios de escalabilidad (fuerte y débil).
* Se hace uso de pseudocódigos (PRAM) para representar algoritmos paralelos.

-----------