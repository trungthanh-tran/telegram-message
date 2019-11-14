from threet.chatbot.tele.TelegramBot import TelegramBot
from threet.chatbot.tele.Config import Config
from flask import Flask, escape, request
import os, sys

app = Flask(__name__)
global telegram_bot
global config

@app.route('/send-message',  methods=['GET'])
def message():
    name = request.args.get("id", "")
    message = request.args.get("message", "")
    telegram_bot.send_message(int(name), message)
    return f'Sent to {name} message {message}'

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":
    try:
        config = Config(os.path.abspath('config.yml'))
        telegram_bot = TelegramBot(config.get_credential())
        app.run(threaded=True, host=config.get_host_name(), port=config.get_port())
    except Exception as e:
        print(str(e))
        sys.exit()
