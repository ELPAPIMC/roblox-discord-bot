# Bot de Discord para Notificaciones del Foro de Roblox

## Descripción
Sistema automatizado 24/7 que monitorea el foro de un grupo de Roblox y envía notificaciones automáticas a Discord cuando se publican nuevos mensajes.

## Características
- Monitoreo automático cada 5 minutos del foro del grupo de Roblox (ID: 35815907)
- Envío de notificaciones formateadas a Discord vía webhook
- Sistema anti-duplicados para evitar notificaciones repetidas
- Manejo de errores y reconexión automática
- Operación continua 24/7 en Replit

## Tecnologías
- Python 3.11
- Flask (servidor keep-alive)
- Requests (llamadas API)
- Roblox Groups API
- Discord Webhook API

## Estructura del Proyecto
- `main.py`: Script principal del bot con lógica de monitoreo
- `keep_alive.py`: Servidor Flask para mantener el bot activo 24/7
- `processed_posts.json`: Base de datos local de posts procesados
- `requirements.txt`: Dependencias del proyecto

## Estado Actual
Fecha de creación: 2025-11-02
Fecha de finalización: 2025-11-02
Estado: ✅ Completado y funcionando

### Último Test
- Bot monitoreando correctamente el foro del grupo 35815907
- 10 notificaciones enviadas exitosamente a Discord en el primer ciclo
- Sistema anti-duplicados funcionando correctamente
- Servidor keep-alive activo en puerto 5000

## Configuración
- Webhook de Discord configurado
- Grupo de Roblox: 35815907
- Intervalo de verificación: 5 minutos
