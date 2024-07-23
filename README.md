# entregable-22-jul-2024
Ejercicios entregables con Django / Python

**Ejercicios elegidos:**

- 1  J
- 19 Marina
- 17 Solomon
- 13 Gerard
-  4  Adán
- 14 Alejandro
- 10 Cristian
- 20 Erik
- 8  Irene
- 5  Fran
- 16 Glenn
- 6  Sergio
- 9  Josias
- 12 Yago

Libres: 2, 3, 7, 11, 15, 18 
---

Lista de 20 ejercicios de Django que cubren diferentes aspectos del desarrollo web con este framework. Cada ejercicio incluye una breve descripción de los requisitos y los objetivos.

### Ejercicios de Django

#### 1. API Data Fetching [máxima puntuación]
**Descripción**: Crear un endpoint que haga una petición a una API externa, obtenga datos y los devuelva formateados en una lista.
**Requisitos**:
- Usar `requests` para hacer la petición.
- Formatear los datos obtenidos.
- Devolverlos en formato JSON.

#### 2. JSON User List [5 raspado, hecho en clase]
**Descripción**: Crear un endpoint que devuelva una lista de usuarios en formato JSON.
**Requisitos**:
- Crear un modelo `User`.
- Poblar la base de datos con usuarios de prueba.
- Crear una vista que devuelva todos los usuarios en formato JSON.

#### 3. File List with Download Links [notable alto]
**Descripción**: Crear un endpoint que devuelva una lista de archivos en una carpeta específica con enlaces de descarga.
**Requisitos**:
- Leer el contenido de una carpeta.
- Generar enlaces de descarga para cada archivo.
- Devolver la lista en formato JSON.

#### 4. Profile Page with Login Requirement [sin librerías: máxima puntuación, con librerías: notable alto]
**Descripción**: Crear una página de perfil que requiera autenticación para acceder.
**Requisitos**:
- Crear un sistema de autenticación.
- Crear una vista de perfil.
- Proteger la vista de perfil para que solo sea accesible a usuarios autenticados.

#### 5. CRUD Operations [máxima puntuación]
**Descripción**: Implementar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para un modelo `Item`.
**Requisitos**:
- Crear el modelo `Item`.
- Implementar vistas para cada operación.
- Usar formularios de Django.

#### 6. Search Functionality [máxima puntuación]
**Descripción**: Implementar una funcionalidad de búsqueda en una lista de artículos.
**Requisitos**:
- Crear un modelo `Article`.
- Crear una vista de búsqueda.
- Devolver resultados coincidentes.

#### 7. Pagination [notable alto / máxima puntuación]
**Descripción**: Implementar paginación en una lista de productos.
**Requisitos**:
- Crear un modelo `Product`.
- Crear una vista que soporte paginación.
- Mostrar un número limitado de productos por página.

#### 8. User Registration [sin librerías: máxima puntuación, con librerías: notable alto]
**Descripción**: Crear un sistema de registro de usuarios.
**Requisitos**:
- Crear formularios de registro.
- Validar la información del usuario.
- Guardar nuevos usuarios en la base de datos.

#### 9. Email Sending [máxima puntuación]
**Descripción**: Implementar una funcionalidad para enviar correos electrónicos.
**Requisitos**:
- Configurar un backend de email.
- Crear una vista para enviar correos.
- Enviar un correo de prueba.

#### 10. User Login and Logout [notable alto / máxima puntuación]
**Descripción**: Implementar vistas de inicio y cierre de sesión para usuarios.
**Requisitos**:
- Crear formularios de inicio de sesión.
- Manejar la sesión del usuario.
- Crear vistas para login y logout.

#### 11. File Upload [notable alto / máxima puntuación]
**Descripción**: Crear una funcionalidad para subir archivos.
**Requisitos**:
- Crear un formulario de subida de archivos.
- Manejar el almacenamiento de archivos subidos.
- Mostrar una lista de archivos subidos.

#### 12. User Profile Update [notable alto / máxima puntuación]
**Descripción**: Permitir a los usuarios actualizar su perfil.
**Requisitos**:
- Crear un formulario de actualización de perfil.
- Validar y guardar los cambios.
- Proteger la vista con autenticación.

#### 13. Dynamic Forms [máxima puntuación]
**Descripción**: Crear formularios dinámicos que cambian según la entrada del usuario.
**Requisitos**:
- Usar formularios de Django.
- Implementar lógica para formularios dependientes.
- Actualizar el formulario dinámicamente con JavaScript.

#### 14. Social Login [notable alto / máxima puntuación]
**Descripción**: Implementar inicio de sesión con una red social (por ejemplo, Google o Facebook).
**Requisitos**:
- Configurar Django Allauth o similar.
- Integrar el login social.
- Manejar la autenticación y los perfiles sociales.

#### 15. Image Gallery [notable alto / máxima puntuación]
**Descripción**: Crear una galería de imágenes con subida y visualización.
**Requisitos**:
- Crear un modelo `Image`.
- Implementar la subida y almacenamiento de imágenes.
- Mostrar las imágenes en una galería.

#### 16. Data Export [notable alto / máxima puntuación]
**Descripción**: Implementar una funcionalidad para exportar datos a CSV.
**Requisitos**:
- Crear una vista para generar y descargar el archivo CSV.
- Formatear los datos en CSV.
- Manejar la descarga del archivo.

#### 17. Comment System [máxima puntuación]
**Descripción**: Crear un sistema de comentarios para artículos.
**Requisitos**:
- Crear modelos `Article` y `Comment`.
- Implementar vistas para agregar y mostrar comentarios.
- Validar y guardar comentarios.

#### 18. Real-time Notifications [máxima puntuación]
**Descripción**: Implementar notificaciones en tiempo real.
**Requisitos**:
- Usar Django Channels.
- Configurar WebSocket.
- Enviar y mostrar notificaciones en tiempo real.

#### 19. Like System [notable alto]
**Descripción**: Crear un sistema de "me gusta" para publicaciones.
**Requisitos**:
- Crear un modelo `Like`.
- Implementar lógica para agregar y quitar "me gusta".
- Mostrar el número de "me gusta" por publicación.

#### 20. Contact Form [notable]
**Descripción**: Crear un formulario de contacto que envíe mensajes por email.
**Requisitos**:
- Crear un formulario de contacto.
- Validar y procesar los datos.
- Enviar el mensaje por email.

### Entrega

- **Instrucciones**: Cada ejercicio debe completarse y subirse en una rama separada con el nombre del ejercicio (por ejemplo, `feature/exercise1`).
- **Repositorio**: Los alumnos recibirán la URL del repositorio donde deben hacer los pull requests.
- **Pull Requests**: Cada pull request debe incluir una descripción clara de los cambios y cómo probar la funcionalidad.
  - Rama: `ejercicio + nombre`, p.e. `01-pepe`
  - Recomendación: nombrar carpeta proyecto `proyecto`

### Instrucciones

Comandos a ejecutar para probar el proyecto:

```bash
  cd <carpeta_de_proyecto>
  python -m venv .venv && source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py collectstatic --noinput # si arroja error, revisar STATIC_ROOT
  python manage.py makemigrations && python manage migrate
  python manage.py runserver
```

---

Estos ejercicios pueden completarse en aproximadamente 1 hora cada uno aproximadamente.
