### Lecture Notes: Applied high-performance computing

Este es un repositorio de las notas importantes sobre el paralelismo y accesos a memoria en computación. No solamente
se toman aspectos teóricos, sino que la parte práctica tambipen esta incluida en los ejercicios de cada tema por carpeta. 


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
