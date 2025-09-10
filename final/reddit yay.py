import praw
import requests
import telebot
from telebot.types import InputMediaPhoto
from config import BOT_TOKEN, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, USER_AGENT

AUTHORIZED_USERS = [7739944746] 

def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS

bot = telebot.TeleBot(BOT_TOKEN)
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=USER_AGENT
)
@bot.message_handler(func=lambda message: "reddit.com" in message.text or "redd.it" in message.text)
def handle_reddit_link(message):
    if not is_authorized(message.from_user.id):
        bot.send_message(message.chat.id, "❌ У вас нет доступа к этому боту.")
        return

    try:
        url = message.text.split()[0]
        
        submission = reddit.submission(url=url)
        

        if hasattr(submission, 'gallery_data'):
            bot.send_message(message.chat.id, "⌛️ Загружаю альбом...")
            media = []
            
            if len(submission.gallery_data['items']) > 10:
                bot.send_message(message.chat.id, "❌ В альбоме больше 10 фотографий. Отправлю только первые 10.")
            
            for item in submission.gallery_data['items'][:10]:
                image_url = f"https://i.redd.it/{item['media_id']}.jpg"
                media.append(InputMediaPhoto(media=image_url))

            bot.send_media_group(message.chat.id, media)
            bot.send_message(message.chat.id, "✅ Альбом отправлен!")

        elif submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            bot.send_message(message.chat.id, "⌛️ Загружаю изображение...")
            response = requests.get(submission.url)
            bot.send_photo(message.chat.id, response.content)
            bot.send_message(message.chat.id, "✅ Изображение отправлено!")
        
        else:
            bot.send_message(message.chat.id, "❌ Эта ссылка не содержит поддерживаемое изображение или альбом.")

    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {e}")

if __name__ == '__main__':
    print("Бот запущен. Ожидаю ссылки...")
    bot.polling(none_stop=True)