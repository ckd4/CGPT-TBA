import os
import openai
import telebot
import telegram
from aiogram import Bot, types

#Here is the token for ur bot
bot = telebot.TeleBot('6002185430:AAH9Sy1z2rHStVumXNGDA_hBre_OXEOhLtw')

#chatgpt token
openai.api_key = "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"

'''
#Theb.ai api key
openai.api_key = os.getenv(" ")

completion = openai.ChatCompletion.create(
  model="claude-instant-1",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=False,
  model_params={
    "temperature": 0.8
  }
)

print(completion.choices[0].message)
'''

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
