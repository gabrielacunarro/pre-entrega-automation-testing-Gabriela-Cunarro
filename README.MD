## 🧪 Proyecto de Automatización – Pre Entrega (Selenium + Pytest)
    Este proyecto contiene pruebas automatizadas para el sitio **SauceDemo**, desarrolladas como parte de la pre-entrega del curso de Automatización QA.  
    Incluye validaciones de login, inventario y carrito de compras utilizando **Selenium WebDriver**, **Pytest** y el patrón **Page Object Model (POM)**.

## 🎯 Propósito del Proyecto
    - Automatización de pruebas UI con Selenium.
    - Uso de Pytest como framework de testing.
    - Estructuración profesional de un framework de automatización.
    - Validación de elementos clave del flujo de compra:
    - Login
    - Visualización de productos
    - Agregar productos al carrito
    - Verificar el contenido del carrito

## 🛠️ Tecnologías Utilizadas
    - Python 3.x  
    - Selenium WebDriver  
    - Pytest  
    - Requests (para pruebas de API)  
    - WebDriver Manager  
    - Pytest-HTML  
    - Page Object Model (POM)

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
    │── assets/
    │
    │── data/
    │   └── users.csv
    │
    │── features/
    │   ├── environment.py
    │   ├── login.feature
    │   └── steps/
    │       └── login_steps.py
    │
    │── pages/
    │   ├── cart_page.py
    │   ├── inventory_page.py
    │   └── login_page.py
    │
    │── reports/
    │   ├── assets/
    │   ├── screenshots/
    │   ├── carrito_report.html
    │   ├── inventario_report.html
    │   ├── login_report.html
    │   ├── preentrega_pom.html
    │   ├── report.html
    │   └── ui_report.html
    │
    │── src/
    │   └── conftest.py
    │
    │── test/
    │   ├── test_api/
    │   │   ├── json_placeholder/
    │   │   └── reqres/
    │   │       ├── test_reqres_get.py
    │   │       ├── test_reqres_post.py
    │   │       └── test_reqres_delete.py
    │   ├── test_carrito.py
    │   ├── test_cart_json.py
    │   ├── test_inventory.py
    │   ├── test_login.py
    │   └── test_login_csv.py
    │
    │── utils/
    │   ├── api_config.py
    │   └── data_reader.py
    │
    │── pytest.ini
    │── requirements.txt
    │── README.md


## 📊 Reportes HTML y Capturas
    La carpeta reports/ contiene:

    reporte.html → generado automáticamente por Pytest-HTML

    screenshots/ → capturas automáticas cuando una prueba falla

    Estas evidencias permiten revisar resultados sin necesidad de ejecutar nuevamente las pruebas.

## ✔️ Pruebas Incluidas
    🔐 Login
    Validación de credenciales correctas

    Validación de credenciales incorrectas (escenario negativo)

    📦 Inventario
    Visualización de productos

    Validación de nombres y elementos visibles

    🛒 Carrito
    Agregar un producto al carrito

    Verificar el contador del carrito

    Confirmar que el producto agregado coincide con el mostrado en el carrito

## 🌐 Pruebas de API (Requests)
        Se incluyen pruebas utilizando la API pública ReqRes:

        GET usuario

        POST creación de usuario

        DELETE eliminación de usuario

        Cada prueba valida:

        Código de estado HTTP

        Estructura del JSON

        Campos esperados

## 📘 Notas Finales
        Este proyecto demuestra:

        Buenas prácticas de automatización

        Separación clara entre lógica de pruebas y lógica de páginas

        Uso de datos externos

        Reportes profesionales

        Pruebas UI + API