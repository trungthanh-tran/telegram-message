from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async


class TelegramBot:

    def __init__(self, token):
        if not token:
            raise Exception ('Token {} is not valid'.format(token))
        self.updater = Updater(token=token, use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('hello', self.hello))
        self.updater.dispatcher.add_handler(CommandHandler('get_id', self.get_id))
        self.updater.start_polling()

    def start_webhook(self):
        self.updater.start_polling()
        self.updater.idle()

    def stop_webhook(self):
        self.updater.stop()

    def hello(self, update, context):
        update.message.reply_text(
            'Hello {}'.format(update.message.from_user.first_name))

    def get_id(self, update, context):
        update.message.reply_text(
            'ChatID: {}'.format(update.message.chat.id))

    @run_async
    def send_message (self, chat_id, message):
        self.updater.bot.send_message(chat_id=chat_id, text=message)