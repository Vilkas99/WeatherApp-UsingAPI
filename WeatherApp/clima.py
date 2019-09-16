#Programa desarrollado por: Víctor Alfonso Mancera Osorio (15/09/19)
#Guía: https://youtu.be/D8-snVfekto

import tkinter as tk #Importo la libreria 'tkinter' y la renombro 'tk' para acceder a sus métodos.
from tkinter import font #También importamos las fonts disponibles para el GUI
import requests #Libreria que permite realizar encargos de HTTP a servidores. 
from PIL import ImageTk, Image #Importamos los métodos específicos de las librerías de manejo de imagenes de Tk.


#Método que obtiene el clima al ser presionado un botón. (Toma comoa rg el nombre de la ciudad)
def boton_ObtenerClima(ciudad):
    #Almaceno la llave de mi API de clima.
    llave_clima = "9eb4b4f35f3e7a1b151c82d3c382c0d6"
    #Almaceno la URL de mi API.
    url = "https://api.openweathermap.org/data/2.5/weather"
    #Creo un arreglo de parametros (Que serán utilizados en el request)
    parametros ={'appid': llave_clima, 'q': ciudad, 'unidades': "Celsius"}
    #Obtengo la información a través del método 'get' de mi libreria ed
    respuesta = requests.get(url, params = parametros)
    #Almaceno mi respuesta (En formato 'json')
    clima = respuesta.json()

    #Establezco que el componente 'text' de mi elemento gráfico 'label' será lo que regrese la función 'respuesta_ConFormato...'
        #Cuyo parametro es mi variable 'clima' (La cual recordemos que posee los valores de mi respuesta del servidor)
    label['text'] = respuesta_ConFormato(clima)

#Función que establece la respuesta provista por mi API, en un formato coherente para ser presentado.
def respuesta_ConFormato(clima):
    #Intenta ejecutar el código con el argumento provisto.
    try:
        #Accedemos a la lista de 'clima' en el dato con 'id' de 'name' y lo almacenamos en mi variable 'nombre'
        nombre = clima['name']
        #De forma análoga, accedemos a la propiedad 0 del dato 'weather', con id de 'description', y lo almacenamos. 
        descripcion_Clima= clima['weather'][0]['description']
        #Accedemos al dato 'main' en donde obtenemos el valor de 'temp'
        temperatura = clima['main']['temp']

        #Estructuramos todos los datos en una variable llamada 'texto'
        texto = 'Ciudad: %s \nTemperatura (°F): %s \nDescripción: %s' % (nombre, temperatura, descripcion_Clima)
    #Si el programa falla (Por ejemplo, si el usuario escribe una ciudad incorrectamente, o coloca otro tipo de valor...)
    except:
        #Entonces texto contendrá un mensaje de error
        texto = 'No pudimos localizar la ciudad.'
    #Al final, regresamos texto-
    return texto

root = tk.Tk() ## Método que genera la ventana principal del GUI 


#Establezco un lienzo en el que colocaré mis objetos principales
lienzo = tk.Canvas(root, height = 500, width = 600)
## El método 'pack' me permite renderizar los elementos que vaya creando.
lienzo.pack()

#Establezco una variable 'fondo' que será de tipo 'ImageTK'
fondo = ImageTk.PhotoImage(Image.open("/Users/Vilkas/Documents/Programacion/ProyectosGit/WeatherApp-UsingAPI/WeatherApp/fondo.jpg"))
#Establezco un label (Cuyo parent es 'root') que posee una imagen (La cual es 'fondo')
fondo_label = tk.Label(root, image = fondo)
#La coloco en el canvas.
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

#Creamos un 'frame' azulado, con borde de 5 (bd) y con un parent (root).
frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
#Lo colocamos a una posición relativa en x de .5 (En medio) y de .1 en y. Además, lo anclamos en la parte superior ('n' north)
frame.place(relx = .5, rely = .1 ,relwidth = .75, relheight = .1, anchor = 'n')

#Establezco un campo de entrada (Cuyo parent es 'frame' y con un tamaño de font de 70)
campoEntrada = tk.Entry(frame, font = 70 )
#Lo colocamos
campoEntrada.place(relwidth = 0.65, relheight = 1)

#Creamos un botón (Con parent de 'frame'), texto y un comando (Proceso que se ejecuta cuando este es usado.)
    #En caso de que 'command' involucre una función con argumentos, esta sólo leera los argumentos 1 SOLA VEZ.
    #Por ello, en la sig linea utilizamos a 'lambda',  la cual es una función anónima que te permite ejecutar 1 sola expresión.
        #Aquí la expresión es la función 'boton_ObtenerClima' (Con todo y sus argumentos).
        #Como nuestra función lambda no tiene argumentos (Solo expresiones que tienen argumentos), ejecuta el código correctamente.
boton = tk.Button(frame, text="Obtener clima", command = lambda: boton_ObtenerClima(campoEntrada.get()))
boton.place(relx = .7, relheight = 1, relwidth = 0.3)

#Establecemos un frame inferior
frame_inferior = tk.Frame(root, bg =  "#80c1ff", bd = 10)
frame_inferior.place(relx = .5, rely = .25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

#Creamos un label (Cuyo parent es el frame_inferior) que contendrá la información del clima.
label = tk.Label(frame_inferior, font=("Modern", 20), justify ="left")
label.place(relwidth = 1, relheight = 1)

#Método de la ventana principal que ejecuta un ciclo que permite el funcionamiento continuo del programa.
root.mainloop()