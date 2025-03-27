
# 🛒 **Automatización de Pruebas con Selenium para SauceDemo** 🛠️

Este proyecto contiene pruebas automatizadas utilizando **Selenium WebDriver** para interactuar con el sitio web **SauceDemo**. La automatización se utiliza para verificar la funcionalidad de un sitio web de comercio electrónico, asegurando que las operaciones clave se realicen correctamente.

## 📋 **Descripción**

El objetivo de este proyecto es demostrar cómo automatizar casos de prueba para un sitio de comercio electrónico. Las pruebas cubren:

- **Inicio de sesión** con credenciales válidas e inválidas.
- **Agregar productos** al carrito y **eliminarlos**.
- **Proceso de compra (Checkout)**.

Estas pruebas están implementadas usando **Python** y **Selenium WebDriver** con el framework de pruebas **unittest** para gestionar y ejecutar los casos de prueba.

## 📑 **Tabla de Contenidos**

1. [Características](#características)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Casos de Prueba](#casos-de-prueba)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Ejecución de las Pruebas](#ejecución-de-las-pruebas)


## 🔥 **Características**

- **Automatización de Pruebas Funcionales:** Usando Selenium WebDriver.
- **Pruebas con Datos Reales:** Inicio de sesión, agregar productos al carrito, y finalizar la compra.
- **Gestión de Pruebas con Unittest:** Framework de Python para la organización y ejecución de pruebas.
- **Resultados Claros:** Verificación de las interacciones en la interfaz con aserciones para confirmar resultados.

## 📦 **Requisitos**

Para ejecutar este proyecto, asegúrate de tener los siguientes elementos:

- **Python 3.x** (Se recomienda Python 3.7 o superior)
- **Selenium WebDriver**: Para la automatización de las pruebas.
- **ChromeDriver**: Descárgalo desde [aquí](https://sites.google.com/a/chromium.org/chromedriver/), asegurándote de que la versión coincida con tu navegador Chrome.
- **unittest**: Framework de pruebas incluido en Python.

## 🚀 **Instalación**

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clonar el repositorio:**
   
   Abre tu terminal o línea de comandos y ejecuta:
   
   ```bash
   git clone https://github.com/tu_usuario/selenium-saucedemo.git
Instalar Selenium:

Usa pip para instalar las dependencias necesarias:

bash
Copiar
Editar
pip install selenium
Descargar ChromeDriver:

Ve a ChromeDriver y descarga la versión correspondiente a tu navegador Google Chrome.

Colócalo en el mismo directorio que el script o asegúrate de que esté en tu PATH.

🧪 Casos de Prueba
A continuación se describen los casos de prueba que se automatizan:

1. Inicio de sesión exitoso
Objetivo: Verificar que un usuario pueda iniciar sesión con credenciales válidas.

Acción: Ingresar el nombre de usuario "standard_user" y la contraseña "secret_sauce".

Resultado esperado: El sistema debe redirigir a la página de inventario.

2. Inicio de sesión fallido
Objetivo: Verificar que el sistema muestre un mensaje de error con credenciales inválidas.

Acción: Ingresar un nombre de usuario incorrecto y una contraseña inválida.

Resultado esperado: El sistema debe mostrar un mensaje de error: "Epic sadface".

3. Agregar producto al carrito
Objetivo: Verificar que un producto pueda ser agregado al carrito.

Acción: Hacer clic en el botón de "Agregar al carrito" para un producto.

Resultado esperado: El ícono del carrito debe mostrar el número "1", indicando que un producto ha sido añadido.

4. Eliminar producto del carrito
Objetivo: Verificar que un producto pueda ser eliminado del carrito.

Acción: Hacer clic en el botón de "Eliminar" para el producto agregado.

Resultado esperado: El ícono del carrito debe desaparecer, indicando que no hay productos en el carrito.

5. Proceso de compra (Checkout)
Objetivo: Verificar que un usuario pueda completar el proceso de compra correctamente.

Acción: Ingresar los datos de pago, confirmar la información y finalizar la compra.

Resultado esperado: El sistema debe mostrar el mensaje "Thank you for your order!" tras completar el pedido.

🏁 Estructura del Proyecto
La estructura de archivos es la siguiente:

bash
Copiar
Editar
selenium-saucedemo/
│
├── test_saucedemo.py       # Código principal con las pruebas automatizadas
├── README.md              # Documentación del proyecto
├── requirements.txt       # Dependencias del proyecto
└── chromedriver.exe       # Driver de Chrome (asegúrate de tener la versión correcta)
🖥️ Ejecución de las Pruebas
Abre tu terminal o línea de comandos.

Navega al directorio del proyecto:

bash
Copiar
Editar
cd selenium-saucedemo
Ejecuta las pruebas utilizando unittest:

bash
Copiar
Editar
python -m unittest test_saucedemo.py
Esto ejecutará todas las pruebas definidas en el archivo test_saucedemo.py y te mostrará los resultados.
