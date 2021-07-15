import telebot

from transformers import pipeline
#import PyTelegramBotAPI
#1651619128:AAE2O43uCalfjyxPA8_nFedm2luvz00Ljlc
bot = telebot.TeleBot("1651619128:AAE2O43uCalfjyxPA8_nFedm2luvz00Ljlc")
text_generation = pipeline('text-generation', model='./rugpt3', tokenizer='sberbank-ai/rugpt3medium_based_on_gpt2', config={'max_length':1000, 'temperature': .5})
text = "Родина"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Приветствую. Предоставьте боту загатовку - слово или фразу - и он сочинит вам стих.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    result = text_generation(message.text, max_length=70, top_k=50, top_p=0.92, do_sample=True, temperature=1.7)[0]['generated_text']
    bot.reply_to(message,result)


# bot.reply_to(message, message.text)

bot.polling()