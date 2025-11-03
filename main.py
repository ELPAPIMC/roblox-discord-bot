import requests
import json
import time
import os
from datetime import datetime
from keep_alive import keep_alive

ROBLOX_GROUP_ID = "35815907"
CHECK_INTERVAL = 300
PROCESSED_POSTS_FILE = "processed_posts.json"

# Configuración del bot de Discord
BOT_NAME = "zzzmx_bot"
# Puedes cambiar esta URL por la de tu icono personalizado
# Para usar un icono personalizado, sube tu imagen a Discord o usa una URL pública
BOT_AVATAR_URL = os.getenv('BOT_AVATAR_URL', "https://tr.rbxcdn.com/38c6458fc6a8e171315f83244dfd8cdf/150/150/Image/Png")

def get_discord_webhook():
    webhook = os.getenv('DISCORD_WEBHOOK_URL')
    if not webhook:
        print("ERROR: DISCORD_WEBHOOK_URL no está configurada en las variables de entorno")
        print("Por favor, configura la variable de entorno DISCORD_WEBHOOK_URL")
        return None
    return webhook

def load_processed_posts():
    try:
        with open(PROCESSED_POSTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_processed_posts(posts):
    with open(PROCESSED_POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=2)

def get_forum_posts():
    try:
        url = f"https://groups.roblox.com/v2/groups/{ROBLOX_GROUP_ID}/wall/posts"
        params = {
            "limit": 10,
            "sortOrder": "Desc"
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener posts del foro: {e}")
        return []

def get_user_info(user_id):
    try:
        url = f"https://users.roblox.com/v1/users/{user_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        return {"name": "Usuario Desconocido"}

def send_discord_notification(post):
    webhook_url = get_discord_webhook()
    if not webhook_url:
        return False
    
    try:
        author_info = get_user_info(post['poster']['user']['userId'])
        author_name = author_info.get('name', 'Usuario Desconocido')
        
        created_time = datetime.fromisoformat(post['created'].replace('Z', '+00:00'))
        formatted_time = created_time.strftime('%Y-%m-%d %H:%M:%S UTC')
        
        post_url = f"https://www.roblox.com/groups/{ROBLOX_GROUP_ID}"
        
        embed = {
            "title": "📢 Nuevo Estafador Encontrado",
            "description": post['body'],
            "color": 0x00A2FF,
            "fields": [
                {
                    "name": "👤 Autor",
                    "value": author_name,
                    "inline": True
                },
                {
                    "name": "🕒 Fecha",
                    "value": formatted_time,
                    "inline": True
                }
            ],
            "footer": {
                "text": f"Post ID: {post['id']}"
            },
            "url": post_url
        }
        
        payload = {
            "embeds": [embed],
            "username": BOT_NAME,
            "avatar_url": BOT_AVATAR_URL
        }
        
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        
        print(f"✅ Notificación enviada: Post {post['id']} de {author_name}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al enviar notificación a Discord: {e}")
        return False

def monitor_forum():
    print("🤖 Bot de Discord para Roblox iniciado")
    print(f"📊 Monitoreando grupo: {ROBLOX_GROUP_ID}")
    print(f"⏰ Intervalo de verificación: {CHECK_INTERVAL} segundos (5 minutos)")
    print("-" * 50)
    
    processed_posts = load_processed_posts()
    
    while True:
        try:
            posts = get_forum_posts()
            
            if posts:
                new_posts_found = 0
                
                for post in reversed(posts):
                    post_id = str(post['id'])
                    
                    if post_id not in processed_posts:
                        if send_discord_notification(post):
                            processed_posts.append(post_id)
                            new_posts_found += 1
                            time.sleep(2)
                
                if new_posts_found > 0:
                    save_processed_posts(processed_posts[-100:])
                    print(f"📨 {new_posts_found} nuevos posts encontrados y notificados")
                else:
                    print(f"✓ Sin nuevos posts [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
            else:
                print(f"⚠ No se pudieron obtener posts [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        
        except Exception as e:
            print(f"❌ Error en el monitor: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    keep_alive()
    monitor_forum()
