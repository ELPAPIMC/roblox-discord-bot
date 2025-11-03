from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot de Discord para Roblox está activo 24/7!"

@app.route('/status')
def status():
    return {
        "status": "online",
        "bot": "Roblox Forum Monitor",
        "message": "El bot está monitoreando el foro de Roblox"
    }

def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.start()
