## 🧪 Proyecto de Automatización – Pre Entrega (Selenium + Pytest)
    Este proyecto contiene pruebas automatizadas para el sitio SauceDemo, desarrolladas como parte de la pre-entrega del curso de Automatización QA.
    Incluye validaciones de login, inventario y carrito de compras utilizando Selenium WebDriver y Pytest.

## 🎯 Propósito del Proyecto
    El objetivo principal es practicar y demostrar:

    Automatización de pruebas UI con Selenium.

    Uso de Pytest como framework de testing.

    Estructuración profesional de un proyecto de automatización.

    Validación de elementos clave del flujo de compra:

    Login

    Visualización de productos

    Agregar productos al carrito

    Verificar el contenido del carrito

## 🛠️ Tecnologías Utilizadas
    Python 3.x

    Selenium WebDriver

    Pytest

    WebDriver Manager (para manejar drivers automáticamente)

    Estructura modular con helpers.py y conftest.py

## 📦 Instalación de dependencias
    Instalar todas las dependencias necesarias:

    Código
    pip install -r requirements.txt

## ▶️ Ejecución de las pruebas
    Para ejecutar todas las pruebas y generar un reporte HTML:

    Código
    python -m pytest -v --html=reports/reporte.html
    Esto generará un archivo reporte.html dentro de la carpeta reports/.

## 📁 Estructura del Proyecto
    Proyecto/
    │── src/
    │   ├── helpers.py
    │   └── conftest.py
    │
    │── tests/
    │   ├── test_login.py
    │   ├── test_inventory.py
    │   └── test_carrito.py
    │
    │── reports/
    │   ├── reporte.html
    │   └── capturas/ (si aplica)
    │
    │── datos/ (si aplica)
    │── requirements.txt
    │── README.md

## 📊 Reportes HTML y Capturas
    La carpeta reports/ contiene:

    reporte.html → reporte generado automáticamente por Pytest-HTML

    capturas/ → carpeta opcional para guardar screenshots de fallos

    Estos archivos sirven como evidencia del resultado de las pruebas sin necesidad de ejecutar el proyecto.

## ✔️ Pruebas Incluidas
    🔐 Login
        Validación de credenciales correctas

        Verificación de acceso al inventario

    📦 Inventario
     Visualización de productos

     Validación de nombres y elementos visibles

    🛒 Carrito
        Agregar un producto al carrito

        Verificar el contador del carrito

        Confirmar que el producto agregado coincide con el mostrado en el carrito