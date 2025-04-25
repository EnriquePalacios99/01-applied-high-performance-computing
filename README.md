### 01-applied-high-performance-computing













------------------
En caso desees crear carpetas para tomar tus apuntes puedes realizarlo de la siguiente forma
tomando en cuenta que te encuentres en la carpeta de destino

```
for i in $(seq 1 16); do
  carpeta=$(printf "S%02d" "$i")
  mkdir "$carpeta"
  touch "$carpeta/$carpeta.md"
done

```
