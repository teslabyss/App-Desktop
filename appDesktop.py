# Control final cibergaleon
import tkinter as tk
import requests

# URL del Mockapi
url_api = "https://66eb019a55ad32cda47b4cc5.mockapi.io/IoTCarStatus"

# Función para enviar el estado al Mockapi
def enviar_a_api(direccion):
    datos = {"direccion": direccion}
    try:
        response = requests.post(url_api, json=datos)
        if response.status_code == 201:
            mensaje = f"Dirección '{direccion}' enviada correctamente."
            print(mensaje)
            actualizar_salida(mensaje)
        else:
            mensaje = f"Error al enviar la dirección '{direccion}'. Estado: {response.status_code}"
            print(mensaje)
            actualizar_salida(mensaje)
    except requests.RequestException as e:
        mensaje = f"Error al conectar con la API: {e}"
        print(mensaje)
        actualizar_salida(mensaje)

# Función para actualizar la descripción en la interfaz y enviarla al Mockapi
def actualizar_direccion(direccion):
    label_direccion.config(text=f"Dirección: {direccion}")
    enviar_a_api(direccion)

# Función para actualizar la salida de los ultimos registros
def actualizar_salida(mensaje):
    text_salida.config(state=tk.NORMAL)
    text_salida.insert(tk.END, mensaje + "\n")
    text_salida.config(state=tk.DISABLED)
    text_salida.see(tk.END)

# Funciones para los botones
def adelante():
    actualizar_direccion("adelante")

def atras():
    actualizar_direccion("atras")

def izquierda():
    actualizar_direccion("izquierda")

def derecha():
    actualizar_direccion("derecha")

def alto():
    actualizar_direccion("alto")

# Ventana principañ
ventana = tk.Tk()
ventana.title("Control del Cibergaleon Alicia")

# Funcion para cambiar el icono y tamaño de la ventana
ventana.iconbitmap("pirate.ico")
ventana.geometry("400x440")
ventana.resizable(False, False)

# Mostrar la dirección actual
label_direccion = tk.Label(ventana, text="Dirección: ", font=("Helvetica", 14))
label_direccion.grid(row=0, column=0, columnspan=3, pady=10)

# Mostrar la salida del Mockapi
text_salida = tk.Text(ventana, height=8, width=40, font=("Helvetica", 10))
text_salida.grid(row=5, column=0, columnspan=3, padx=10, pady=20)
text_salida.config(state=tk.DISABLED)

# Estilo de los botones
btn_style = {"font": ("Helvetica", 12), "width": 10, "height": 2, "bg": "#bd4be3", "fg": "white"}

btn_adelante = tk.Button(ventana, text="Adelante", command=adelante, **btn_style)
btn_atras = tk.Button(ventana, text="Atrás", command=atras, **btn_style)
btn_izquierda = tk.Button(ventana, text="Izquierda", command=izquierda, **btn_style)
btn_derecha = tk.Button(ventana, text="Derecha", command=derecha, **btn_style)
btn_alto = tk.Button(ventana, text="Alto", command=alto, **btn_style)

# Posicionar los botones en la ventana y centrados
btn_adelante.grid(row=1, column=1, pady=10)
btn_izquierda.grid(row=2, column=0, padx=10, pady=10)
btn_alto.grid(row=2, column=1, padx=10, pady=10)
btn_derecha.grid(row=2, column=2, padx=10, pady=10)
btn_atras.grid(row=3, column=1, pady=10)

# Centrar
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)

ventana.mainloop()
