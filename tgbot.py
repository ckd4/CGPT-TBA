import os
import telebot
from openai import OpenAI
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# tg bot API key
bot = telebot.TeleBot(os.getenv("TG_bot_key"))

# ChatGPT API key
client = OpenAI(api_key=os.getenv("ChatGPT_API_key"))

# decorator for start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} to start just type message or generate image with /img prompt')

@bot.message_handler(content_types=['text']) # main decorator for text
def main(message):
    reply = ''

    try:
        response = client.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': message.text}],
            max_tokens = 4000, # max symbols in response
            temperature = 0.7, # adjust for creativity
            frequency_penalty=0,  # fine-tune word frequency
            presence_penalty=0,  # fine-tune word presence
            n = 1, # responses amount
            stop = None
        )

        if response and response.choices:
            reply = response.choices[0].message.content
            print(f"{message.from_user.first_name} ({message.chat.id}):\n{message.text}")
        else:
            reply = 'No response from the model'
            print("No response from the model")

    except Exception as e:
        print(f"Error: {e}\n\n API ERROR")
        reply = 'Error processing your request'

    # response from gpt
    bot.send_message(message.chat.id, reply)

bot.polling(none_stop=True, interval=0) # bot looking for new messages non stop     