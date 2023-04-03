#pip install openai
#pip install telebot
#pip install python-telegram-bot
#pip install aiogram

import openai
import telebot
import telegram
from aiogram import Bot, types

bot = telebot.TeleBot('6002185430:AAH9Sy1z2rHStVumXNGDA_hBre_OXEOhLtw')

openai.api_key = "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"

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}, to start just type message or generate image with /img \"prompt\"')

@bot.message_handler(commands=['img'])
def generate_image(message):
    bot.send_chat_action(message.chat.id, action=telegram.constants.ChatAction.TYPING) 
    response = openai.Image.create(
      prompt=str(message.text),
      n=1,
      size="1024x1024"
    )
    image_url = response['data'][0]['url']
    bot.reply_to(message, image_url)

@bot.message_handler()
def send(message : types.Message):
    bot.send_chat_action(message.chat.id, action=telegram.constants.ChatAction.TYPING)
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = message.text,
    temperature=0,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0
    )

    answer = response['choices'][0]['text']
    bot.send_message(message.chat.id, answer)

bot.infinity_polling()
