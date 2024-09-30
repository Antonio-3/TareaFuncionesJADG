import streamlit as st

#Jose Antonio Delgado Guillermo

def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def area_triangulo(base, altura):
    return (base * altura) / 2

def precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    return precio_descuento + (precio_descuento * impuesto / 100)

def sumar_lista(numeros):
    return sum(numeros)

def total_producto(nombre, cantidad=1, precio=10):
    return f"Total por {cantidad} {nombre}(s): {cantidad * precio}"

def pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado if args else 1

def info_persona(**kwargs):
    return kwargs

def calculadora(num1, num2, operacion='suma'):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        return num1 / num2
    return "Operación no válida"

st.title("Tablero de Ejercicios Interactivos")

ejercicio = st.sidebar.selectbox(
    "Selecciona un ejercicio",
    (
        "Saludo simple",
        "Suma de dos números",
        "Área de un triángulo",
        "Calculadora de descuento",
        "Suma de una lista",
        "Producto con valores predeterminados",
        "Números pares e impares",
        "Multiplicación con *args",
        "Información personal con **kwargs",
        "Calculadora flexible"
    )
)

if ejercicio == "Saludo simple":
    nombre = st.text_input("Ingresa tu nombre")
    if st.button("Saludar"):
        st.write(saludar(nombre))

elif ejercicio == "Suma de dos números":
    a = st.number_input("Número 1", step=1)
    b = st.number_input("Número 2", step=1)
    if st.button("Sumar"):
        st.write(f"Suma: {sumar(a, b)}")

elif ejercicio == "Área de un triángulo":
    base = st.number_input("Base del triángulo", step=1.0)
    altura = st.number_input("Altura del triángulo", step=1.0)
    if st.button("Calcular Área"):
        st.write(f"Área: {area_triangulo(base, altura)}")

elif ejercicio == "Calculadora de descuento":
    precio = st.number_input("Precio original", step=1.0)
    descuento = st.number_input("Descuento (%)", value=10, step=1.0)
    impuesto = st.number_input("Impuesto (%)", value=16, step=1.0)
    if st.button("Calcular Precio Final"):
        st.write(f"Precio final: {precio_final(precio, descuento, impuesto)}")

elif ejercicio == "Suma de una lista":
    numeros = st.text_input("Lista de números separados por comas")
    if st.button("Sumar Lista"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        st.write(f"Suma: {sumar_lista(lista_numeros)}")

elif ejercicio == "Producto con valores predeterminados":
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", value=1, step=1)
    precio = st.number_input("Precio por unidad", value=10.0, step=1.0)
    if st.button("Calcular Precio"):
        st.write(total_producto(producto, cantidad, precio))

elif ejercicio == "Números pares e impares":
    numeros = st.text_input("Lista de números separados por comas")
    if st.button("Dividir"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        pares, impares = pares_e_impares(lista_numeros)
        st.write(f"Pares: {pares}")
        st.write(f"Impares: {impares}")

elif ejercicio == "Multiplicación con *args":
    numeros = st.text_input("Números a multiplicar separados por comas")
    if st.button("Multiplicar"):
        lista_numeros = [int(num) for num in numeros.split(",")]
        st.write(f"Resultado: {multiplicar_todos(*lista_numeros)}")

elif ejercicio == "Información personal con **kwargs":
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", step=1)
    direccion = st.text_input("Dirección")
    if st.button("Mostrar Información"):
        st.write(info_persona(nombre=nombre, edad=edad, direccion=direccion))

elif ejercicio == "Calculadora flexible":
    num1 = st.number_input("Número 1", step=1.0)
    num2 = st.number_input("Número 2", step=1.0)
    operacion = st.selectbox("Operación", ["suma", "resta", "multiplicacion", "division"])
    if st.button("Calcular"):
        st.write(f"Resultado: {calculadora(num1, num2, operacion)}")
