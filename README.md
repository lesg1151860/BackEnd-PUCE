# Inicio de sesión básico (FastAPI)

Instrucciones rápidas para ejecutar la API localmente:

Instalar dependencias:

```bash
python -m pip install -r requirements.txt
```

Ejecutar el servidor:

```bash
uvicorn app.main:app --reload
```

Endpoints principales:
- `POST /register` — Crear usuario (campos: `full_name`, `email`, `password`, `role`)
- `POST /token` — Obtener token (OAuth2 password, usar `username`=email)
- `GET /users` — Listar usuarios (requiere rol `admin`)
- `DELETE /users/{id}` — Eliminar usuario (requiere rol `admin`)

Notas:
- Cambia `SECRET_KEY` en `app/main.py` antes de producción.
- La base de datos usada es SQLite (`dev.db`) en la raíz del proyecto.
