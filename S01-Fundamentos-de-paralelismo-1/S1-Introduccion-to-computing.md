######  Fundamentos de Pararelismo

### Notas de Clase: Fundamentos de Paralelismo

#### Introducción
En este primer capítulo se presentan los objetivos del curso, que se divide en tres etapas principales. Cada etapa analiza la arquitectura HPC y herramientas de software en paralelo.

**Resultados de Aprendizaje (RA):**
- **RA1:** Analizar arquitecturas de HPC.
- **RA2:** Desarrollar soluciones en paralelo.
- **RA3:** Gestionar proyectos HPC.

#### Temas Principales
1. Introducción al curso.
2. Transición del procesamiento secuencial al paralelo.
3. Aplicaciones en paralelo.
4. Paradigmas en paralelo.

#### Unidades de Enfoque
1. Introducción a HPC.
2. Modelos en paralelo.
3. Multithreading.
4. Paralelismo distribuido e híbrido.
5. Paralelismo aplicado.

---

### Historia de la Computación Paralela

#### Primer Computador Electrónico
El primer computador electrónico que empleaba código y datos fue diseñado por John von Neumann con la IAS Machine (1952). Su arquitectura era secuencial, ejecutando una tarea después de otra.

![Arquitectura de John von Neumann](image.png)

#### Computo vs Acceso a Memoria
Desde los inicios de la computación, existe un paralelismo inherente entre el cómputo y el acceso a memoria, representado en las gráficas históricas de rendimiento.

#### Transición del Procesamiento Secuencial al Paralelo
La evolución de la computación ha llevado a un cambio significativo del procesamiento secuencial al paralelo, permitiendo un aumento en la eficiencia y velocidad de ejecución.

---

### Speedup (FLOPs)

#### Definición
El **Speedup** mide la velocidad máxima de ejecución de operaciones de coma flotante por unidad de tiempo, expresada en **FLOPs** (Floating Point Operations per second).

#### Tipos de Operaciones
- **Aritmética de Coma Flotante Simple:** Suma, multiplicación.
- **Aritmética Compleja:** División, raíz, trigonometría, logaritmos (más lenta, debe evitarse en HPC).

#### Ejemplos Prácticos
1. **Procesador realizando una suma:**
    - Operación en $10^{-9}$ segundos → $10^9$ FLOPs (1 GFLOP).

2. **Programa con $10^{12}$ operaciones:**
    - Computadora A: $10^{10}$ FLOPs → Tiempo: 100 segundos.
    - Computadora B: $5 \cdot 10^{10}$ FLOPs → Tiempo: 20 segundos.
    - **Speedup:** $100 / 20 = 5$ (5 veces más rápida).

3. **Comparación de sistemas:**
    - GPU de alto rendimiento: Varios TFLOPs ($10^{12}$ FLOPs).
    - CPU típica: Decenas o cientos de GFLOPs.

4. **Importancia en HPC:**
    - Resolver problemas complejos como simulaciones científicas, modelado climático, análisis de datos masivos e inteligencia artificial.

#### Notas Finales
El Speedup en FLOPs es un indicador clave en HPC para optimizar hardware y software, maximizando el rendimiento en aplicaciones específicas.

--- 
En este primer capítulo se presentaran los objetivos del desarrollo de todo el curso.
------
Temas: 

1. Introducción al curso 
2. Transición del procesamiento secuencial paralelo 
3. Aplicaciones en paralelo 
4. Paradigmas en paralelo

------ 


1. Introducción al curso 

Se dibidirá principalmente en tres etapas.En cada una de ellas se analizará la arquitectura HPC y herramientas de softwere en paralelo. 



**RA1**
Analizar Arquitecturas de HPC 


**RA2**
Desarrolla 
soluciones en paralelo

**RA3**
GESTIONA prouectos HPC


### Unidades de Enfoque 

1. Introducción a HPC 
2. Modelos en paralelo
3. Multithreading
4. Paralelismo distribuido e híbrido 
5. Paralelismo aplicado


##### Historia 

El primer computador electrónico que empleadba código  y data fue el de John von Neumann y la IAS machines (1952)

Tenía una arquitectura simple de entrada y salida de código. Secuencial una tarea despues de la otra. 

![alt text][def]

[def]: image.png

##### Arquitectura de John Van Neuman 

#### Computo vs acceso a memorio 

Existe un paralelismo entre el computo y el acceso a memorio representado en la gráfica desde los incios de la creación del primer computador electronico 


#### Del procesamiento secuencial al paralelo 

Imagen 


#### Speeedup (FLOPs)

## Speedup (FLOPs)

IEEE754 especifica un Número de Coma Flotante (FLOP) de precisión simple, de 32-bit base-2, con un valor máximo de $2^{128} \approx 3 \cdot 10^{38}$.

**Speedup** es la velocidad (máxima) de ejecución del total de operaciones de coma flotante por unidad de tiempo, medida en **FLOPs** (Floating Point Operations per second).

Se aplica a:

* **Aritmética de Coma Flotante simple:** (suma, multiplicación)
* **Aritmética compleja:** (división, raíz, trigonometría, logaritmos, etc.) es mucho más lenta y deben evitarse en HPC.

**Ejemplos para entender mejor el Speedup (FLOPs):**

1.  **Un procesador realizando una suma:** Si un procesador puede realizar una operación de suma de coma flotante en $10^{-9}$ segundos (1 nanosegundo), entonces su velocidad para esta operación específica es de $1 / 10^{-9} = 10^9$ FLOPs o 1 GFLOP.

2.  **Un programa con muchas operaciones:** Imagina un programa que necesita realizar $10^{12}$ operaciones de coma flotante.
    * Si una computadora puede ejecutar estas operaciones a una velocidad de $10^{10}$ FLOPs, el tiempo de ejecución del programa sería de $(10^{12} \text{ operaciones}) / (10^{10} \text{ FLOPs}) = 100$ segundos.
    * Si una computadora más potente puede ejecutar estas operaciones a una velocidad de $5 \cdot 10^{10}$ FLOPs, el tiempo de ejecución se reduciría a $(10^{12} \text{ operaciones}) / (5 \cdot 10^{10} \text{ FLOPs}) = 20$ segundos.
    * En este caso, el speedup de la segunda computadora sobre la primera para este programa específico sería de $100 / 20 = 5$. Esto significa que la segunda computadora es 5 veces más rápida para ejecutar este programa en términos de operaciones de coma flotante.

3.  **Comparando diferentes sistemas:** Un sistema con una tarjeta gráfica de alto rendimiento diseñada para cálculos paralelos podría tener una velocidad de varios TeraFLOPs (TFLOPs), donde 1 TFLOP es $10^{12}$ FLOPs. En comparación, un procesador central (CPU) típico podría tener una velocidad de decenas o cientos de GFLOPs. La diferencia en FLOPs indica la capacidad relativa de cada sistema para realizar cálculos intensivos en coma flotante.

4.  **Importancia en HPC:** En la computación de alto rendimiento (HPC), alcanzar un alto speedup en FLOPs es crucial para resolver problemas complejos en tiempos razonables, como simulaciones científicas, modelado climático, análisis de datos masivos e inteligencia artificial. Los arquitectos de sistemas y los desarrolladores de software se esfuerzan por optimizar tanto el hardware como el software para maximizar la tasa de FLOPs alcanzable en aplicaciones específicas.

Espero que estos ejemplos adicionales te ayuden a comprender mejor el concepto de Speedup (FLOPs) y su importancia. ¿Hay algo más en lo que pueda ayudarte?



00:51:55