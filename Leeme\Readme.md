Para graficas Integradas AMD Radeon R2 a la R9 - For integrated AMD Radeon R2 to R9 graphics

Problema: Al maximizar ciertos juegos y aplicaciones, los colores pueden invertirse o aparecer un filtro azul molesto debido a problemas con los drivers superiores a la 20.11.1 de adrenalin mas frecuentemente con las que usan directx11 en gpu integradas de la serie A.

Solución: Ya se he corrovorado en 2 laptops con CPU AMD series A (a4-9120 y un a10-7300), esta solucion consiste en usar un script en Python que utiliza las bibliotecas ' tkinter ' para crear una ventana traslúcida invisible que se mantiene en primer plano. Esta ventana copia automáticamente el color de fondo detrás de ella cada medio segundo, lo que evita que los cambios visuales afecten a los juegos y aplicaciones en primer plano.

Problem: When maximizing certain games and applications, colors may invert or an annoying blue filter may appear due to problems with drivers higher than adrenalin 20.11.1, most frequently with those that use directx11 on integrated A-series GPUs.

Solution: I have already been corrupted on 2 laptops with AMD A series CPUs (a4-9120 and an a10-7300), this solution consists of using a Python script that uses the 'tkinter' libraries to create an invisible translucent window that remains spotlight. This window automatically copies the background color behind it every half second, preventing visual changes from affecting foreground games and apps.

Instrucciones:

Instalación de Python:
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

Instructions:

Python installation:
Make sure you have Python installed on your system. You can download it from python.org.

Código del script - Script Code:

Solucion AMD.py or Solution AMD.exe

Cómo usar:

Copia el código en un archivo Python (por ejemplo, Filtro_AMD.py).
Ejecuta el script usando Python. La ventana traslúcida invisible se creará y comenzará a funcionar automáticamente.
Espero que esta solución sea útil para aquellos que enfrentan problemas similares con los drivers de AMD y los cambios de color en juegos y aplicaciones maximizadas.

How to use:

Copy the code to a Python file (for example, AMD_Filter.py).
Run the script using Python. The invisible translucent window will be created and start working automatically.

I hope this solution is useful for those who are facing similar problems with AMD drivers and color changes in maximized games and applications.

El .exe es la misma version .py pero ya pasda a .exe para su facil acceso y uso.

The .exe is the same .py version but it has already been converted to .exe for easy access and use.


-------------------------------------------------------------------------------------
   ....no me responsabilizo por mal funcioanmiento, o uso inadecuado del mismo....
-------------------------------------------------------------------------------------

