# Django_proyect1

Este es un proyecto creado con **Django**, un framework de desarrollo web en Python, iniciado desde cero con el propósito de practicar y desarrollar aplicaciones web robustas y escalables.

## 🚀 Objetivo del Proyecto
El objetivo es construir una aplicación web utilizando las herramientas que ofrece Django, incluyendo:

- Configuración inicial de un proyecto Django.
- Creación de aplicaciones (apps) internas.
- Gestión de bases de datos con el ORM de Django.
- Desarrollo de interfaces web con templates HTML y Bootstrap.
- Autenticación de usuarios y gestión de sesiones.
- Implementación de vistas, URLs y modelos personalizados.

## ⚙️ Tecnologías Usadas

- **Python 3.x**
- **Django 4.x**
- HTML5, CSS3 (con Bootstrap)
- Base de datos SQLite (por defecto) / PostgreSQL (opcional)
- Git & GitHub para control de versiones

## 📦 Instalación y Configuración

1. Clona este repositorio:
   ```bash
   git clone https://github.com/SamuelGirount333/Django_proyect1.git
   cd Django_proyect1
   ```

2. Crea un entorno virtual:

   **En Linux / macOS**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   **En Windows (CMD o PowerShell)**:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

   Para desactivar el entorno virtual:
   ```bash
   deactivate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta migraciones:
   ```bash
   python manage.py migrate
   ```

5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

6. Accede a la app en tu navegador:
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Estructura del Proyecto (simplificada)

```
littlelemon/
├── manage.py
├── myproject/           # Configuración global del proyecto
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── myapp/      # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── requirements.txt
```

## 📌 Estado del Proyecto

Actualmente en desarrollo. Se están implementando las funcionalidades básicas y pruebas de vistas, modelos y autenticación de usuarios.

## 💡 Próximos pasos

- Despliegue en Heroku o Render.
- Integración de un sistema de comentarios.
- Implementación de pruebas automatizadas.

## ✍️ Autor

Desarrollado por **Samuel Giraldo**  
[GitHub: SamuelGirount333](https://github.com/SamuelGirount333)

