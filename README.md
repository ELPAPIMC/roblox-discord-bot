# 🤖 Bot de Discord para Notificaciones del Foro de Roblox

Sistema automatizado que monitorea el foro de un grupo de Roblox y envía notificaciones automáticas a Discord cuando se publican nuevos mensajes.

## 📋 Características

- ✅ Monitoreo automático cada 5 minutos del foro de Roblox
- ✅ Notificaciones en tiempo real a Discord vía webhook
- ✅ Mensajes formateados con embeds elegantes
- ✅ Sistema anti-duplicados (no envía el mismo post dos veces)
- ✅ Manejo de errores y reconexión automática
- ✅ Operación 24/7 sin interrupciones
- ✅ Servidor keep-alive para funcionamiento continuo en Replit

## 🚀 Instalación y Configuración

### 1. Configurar el Webhook de Discord

1. Ve a tu servidor de Discord
2. Selecciona el canal donde quieres recibir las notificaciones
3. Haz clic en el ícono de configuración del canal (⚙️)
4. Ve a **Integraciones** → **Webhooks**
5. Haz clic en **Nuevo Webhook**
6. Personaliza el nombre y avatar (opcional)
7. Copia la **URL del Webhook**

### 2. Configurar Variables de Entorno en Replit

1. En tu proyecto de Replit, ve al panel de Secrets (🔒)
2. Agrega una nueva variable:
   - **Key**: `DISCORD_WEBHOOK_URL`
   - **Value**: [Pega aquí la URL del webhook que copiaste]
3. Guarda los cambios

### 3. Ejecutar el Bot

1. Asegúrate de que las dependencias estén instaladas:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecuta el bot:
   ```bash
   python main.py
   ```

3. El bot comenzará a monitorear el foro automáticamente

## 📊 Configuración Personalizada

Puedes modificar estos parámetros en `main.py`:

```python
ROBLOX_GROUP_ID = "35815907"  # ID del grupo de Roblox
CHECK_INTERVAL = 300           # Intervalo en segundos (300 = 5 minutos)
BOT_NAME = "zzzmx_bot"         # Nombre del bot en Discord
BOT_AVATAR_URL = "..."         # URL del icono del bot
```

### 🎨 Cambiar el Icono del Bot

Para usar un icono personalizado en Discord:

**Opción 1: Editar directamente en el código**
1. Abre `main.py`
2. Busca la línea `BOT_AVATAR_URL = ...`
3. Reemplaza la URL con la de tu imagen

**Opción 2: Usar variable de entorno (Recomendado)**
1. Ve al panel de Secrets (🔒) en Replit
2. Agrega: `BOT_AVATAR_URL` con la URL de tu icono
3. El bot usará automáticamente ese icono

**Cómo obtener una URL de icono:**
- Sube tu imagen a un canal de Discord y copia el enlace de la imagen
- Usa servicios como Imgur, Discord CDN, o cualquier URL pública de imagen

## 📦 Estructura del Proyecto

```
├── main.py                   # Script principal del bot
├── keep_alive.py             # Servidor Flask para mantener activo el bot
├── requirements.txt          # Dependencias de Python
├── processed_posts.json      # Base de datos de posts procesados (se crea automáticamente)
└── README.md                 # Esta documentación
```

## 🔧 Funcionamiento Técnico

1. **Monitoreo**: El bot consulta la API de Roblox cada 5 minutos para obtener los últimos posts del foro
2. **Detección**: Compara los IDs de los posts con los ya procesados
3. **Notificación**: Envía posts nuevos a Discord con formato embed
4. **Persistencia**: Guarda los IDs procesados en `processed_posts.json`
5. **Keep-Alive**: Un servidor Flask en el puerto 5000 mantiene el bot activo 24/7

## 📱 Formato de Notificaciones

Las notificaciones en Discord incluyen:
- 📢 Título indicando nuevo mensaje
- 📝 Contenido completo del post
- 👤 Nombre del autor
- 🕒 Fecha y hora de publicación
- 🔗 Enlace al grupo de Roblox
- 🆔 ID del post

## 🛠️ Solución de Problemas

### El bot no envía notificaciones

1. Verifica que `DISCORD_WEBHOOK_URL` esté correctamente configurada en Secrets
2. Comprueba que la URL del webhook sea válida
3. Revisa los logs del bot para ver mensajes de error

### El bot se detiene

- Replit mantiene los bots activos automáticamente
- El servidor keep-alive en puerto 5000 ayuda a mantener el proceso activo
- Si se detiene, simplemente vuelve a ejecutar `python main.py`

### No detecta posts nuevos

1. Verifica que el ID del grupo sea correcto (35815907)
2. Asegúrate de que el grupo tenga posts recientes en el foro
3. Comprueba que la API de Roblox esté disponible

## 🌐 APIs Utilizadas

- **Roblox Groups API**: `https://groups.roblox.com/v2/groups/{groupId}/wall/posts`
- **Roblox Users API**: `https://users.roblox.com/v1/users/{userId}`
- **Discord Webhook API**: Para enviar mensajes a Discord

## 📝 Mantenimiento

El bot almacena los últimos 100 posts procesados para optimizar el almacenamiento. Los posts más antiguos se eliminan automáticamente del registro.

## ⚙️ Despliegue 24/7

Este bot está diseñado para funcionar en Replit de forma continua:
- El servidor Flask en puerto 5000 mantiene el proceso activo
- Replit mantiene automáticamente los proyectos activos
- No requiere configuración adicional para operar 24/7

## 📄 Licencia

Proyecto de código abierto para uso personal y educativo.

## 🤝 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de Solución de Problemas
2. Verifica los logs del bot en la consola
3. Asegúrate de que todas las variables de entorno estén configuradas

---

**Nota**: Este bot utiliza APIs públicas de Roblox. Asegúrate de cumplir con los Términos de Servicio de Roblox al usar este bot.
