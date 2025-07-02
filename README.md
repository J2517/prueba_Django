# To-Do List API

API RESTful desarrollada con Django y Django REST Framework para la gestión de tareas por usuario, con autenticación JWT, documentación automática y pruebas unitarias.

---

## Características

- Autenticación mediante **JWT** (`access` y `refresh tokens`)
- Gestión de tareas por usuario: **CRUD completo**
- Autorización: cada usuario solo puede acceder a sus propias tareas
- Pruebas unitarias de modelos y endpoints

---

## ⚙️ Tecnologías

- Python 3.11+
- Django 5.2.3
- Django REST Framework
- Simple JWT
- drf-spectacular
- SQLite3 (por defecto)

---

## Instalación

1. **Clone el repositorio:**

```bash
git clone https://github.com/J2517/prueba_Django
```

2. **Cree y active un entorno virtual:**

```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instale las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Aplique las migraciones:**

```bash
python manage.py migrate
```

5. **Cree un superusuario (opcional, para admin):**

```bash
python manage.py createsuperuser
```

6. **Inicie el servidor:**

```bash
python manage.py runserver
```

---

## Autenticación

La API usa **JWT** para autenticar a los usuarios.
Para mayor facilidad, puede probar todos los endpoints desde la ruta http://127.0.0.1:8000/documentation/docs/

### Obtener token:

`POST /login/`

```json
{
  "username": "su_usuario",
  "password": "su_contraseña"
}
```

📌 Respuesta:

```json
{
  "refresh": "string",
  "access": "string"
}
```


## Documentación

Una vez el servidor esté corriendo, acceda a:

[http://127.0.0.1:8000/documentation/docs/](http://127.0.0.1:8000/documentation/docs/)  
Generado con `drf-spectacular` y `Swagger UI`.

---

## Endpoints

| Método | Ruta               | Descripción                        |
|--------|--------------------|------------------------------------|
| GET    | `/tasks/`          | Listar tareas del usuario          |
| POST   | `/tasks/`          | Crear nueva tarea                  |
| GET    | `/tasks/{id}/`     | Ver detalles de una tarea          |
| PUT    | `/tasks/{id}/`     | Actualizar una tarea               |
| DELETE | `/tasks/{id}/`     | Eliminar una tarea                 |

Todos los endpoints requieren token JWT

---

## Pruebas

1. Ejecute las pruebas unitarias:

```bash
python manage.py test tasks
```

Las pruebas están separadas por:

- Modelos (`tests/test_models.py`)
- Endpoints (`tests/test_endpoints.py`)

---

## Recomendaciones

- Use `http://127.0.0.1:8000/documentation/docs/` para probar fácilmente los endpoints con su token.
---

## Autor

Desarrollado por **Jackeline Rivera**  
Prueba técnica Backend con Django · 2025

---