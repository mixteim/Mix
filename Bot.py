from pyrogram import Client
from loguru import logger

api_id = '27271687'  # Замените на свой API ID, если не используете переменные окружения
api_hash = '3d0b892d8ed7b62a0935088331ad61d5'  # Замените на свой API Hash, если не используете переменные окружения

app = Client('my acc', api_id, api_hash)

@app.on_message(['text'])  # Получаем сообщения
def main(_, message):
    try:
        logger.info(f"FIND NEW MESSAGE - {message.chat.id} | {message.from_user.id}")
        app.send_reaction(message_id=message.message_id, chat_id=message.chat.id, emoji="")  # ставим реакцию, можно поставить любую другую которая имеется в тг
    except:
        pass

app.run()
