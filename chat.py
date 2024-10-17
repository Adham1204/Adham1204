import telebot
from textblob import TextBlob

# Telegram Bot tokenini kiriting
API_TOKEN = '7663219810:AAH9swXBcF8o60voMGgEvooZ8CH9wvLp_Ag'

bot = telebot.TeleBot(API_TOKEN)

# O‘zbek tilini tahlil qilish uchun TextBlob'dan foydalanamiz
def uzbek_text_analysis(text):
    # Bu yerda so‘zlarni o‘zbek tiliga moslab tahlil qilish mumkin
    blob = TextBlob(text)
    return blob.correct()  # Xato so‘zlarni to‘g‘rilaydi

# Murakkab javoblar tuzish uchun
def get_response(message):
    message_text = message.text.lower()
    
    if "Assalomu alaykum" in message_text:
        return "Assalomu alaykum✋! Yordam bera olamanmi?"

    if "salom" in message_text:
        return "Assalomu alaykum✋! Yordam bera olamanmi?"

    elif "ha" in message_text:
        return "Men sizga qanday yodam bera olaman😊?."
    
    elif "ismingiz kim" in message_text:
        return "Mening ismim ChatBot. O‘zbek tilida suhbatlashaman."

    elif "qalay" in message_text:
        return "Rahmat, yaxshi! Sizda qanday yangiliklar?"
    
    elif "isming nima" in message_text:
        return "Mening ismim ChatBot. O‘zbek tilida suhbatlashaman."
     
    elif "ismingiz nima" in message_text:
        return "Mening ismim ChatBot. O‘zbek tilida suhbatlashaman."

    elif "isming nima" in message_text:
        return "Mening ismim ChatBot. O‘zbek tilida suhbatlashaman."
    
    elif "ob-havo" in message_text:
        return "Afsuski, men hozir ob-havo ma'lumotlarini yetkazib bera olmayman, lekin ob-havo ilovasidan foydalanishingiz mumkin."
    
    elif "qayerdansan" in message_text:
        return "Men virtual botman va joylashuvim internetda."

    elif "nima qilayapsan" in message_text:
        return "Men siz bilan suhbatlashayapman. Siz-chi?"

    elif "bugun qanday kun" in message_text:
        return "Men kunlarni ko'rishni bilmayman, ammo qurilmangizdan tekshirishingiz mumkin."

    elif "qayerga borishim kerak" in message_text:
        return "Bu sizning rejalaringizga bog'liq, lekin sayr qilish yaxshi fikr bo'lishi mumkin."

    elif "seni kim yaratgan" in message_text:
        return "Meni ADHAM yaratdi lekin hali kamchiliklarim ko'p. Kelajakda yanada rivojlanishimga umid qilaman"

    elif "qachon tug'ilgansan" in message_text:
        return "Men virtualman, shuning uchun mening tug'ilgan kunim yo'q."

    elif "nimani yaxshi ko'rasan" in message_text:
        return "Men suhbatlashishni yaxshi ko'raman!"

    elif "borganmisan" in message_text:
        return "Men faqat virtual muhitte mavjudman, shuning uchun sayohat qilmayman."

    elif "nima yeyishing kerak" in message_text:
        return "Men ovqat yemayman, lekin siz sog'lom ovqat tanlashingiz mumkin."

    elif "kim bilan gaplashayapsan" in message_text:
        return "Men hozir siz bilan suhbatlashayapman."

    elif "kelajakni ko'ra olasanmi" in message_text:
        return "Afsuski, men kelajakni ko'ra olmayman, lekin yaxshi reja tuzishingizni maslahat beraman."

    elif "rahmat" in message_text:
        return "Marhamat! Yordam bera olganimdan mamnunman."
    
    else:
        return "Bu savolga javob bera olmayman. Yana biror narsa so'rang."

# /start va /help komandalariga javob
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Men o‘zbek tilidagi suhbatdosh botman. Savollaringizni yozing bilganlarimni aytaman!")

# Foydalanuvchining xabarlariga javob qaytarish
@bot.message_handler(func=lambda message: True)
def respond_to_message(message):
    user_message = message.text
    corrected_message = uzbek_text_analysis(user_message)
    response = get_response(message)
    bot.reply_to(message, response)

# Botni ishga tushirish
bot.polling()