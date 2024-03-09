import os
import openai
import dotenv
import telebot
import telegram
import loguru
import deep_translator

dotenv.load_dotenv()

bot = telebot.TeleBot(os.getenv("TG_TOKEN"))
oai = openai.OpenAI(api_key=os.getenv("OAI_TOKEN"))

prompts = {
    "dan": open("prompts/dan.prompt", 'r', encoding='utf-8').read(),
}

def translate(message: str) -> str:
    translator = deep_translator.GoogleTranslator(source='auto', target='ru')
    return translator.translate(message)

def generate_reply(message, jb: str = '') -> str:
    reply = ''
    try:
        bot.send_chat_action(message.chat.id, action=telegram.constants.ChatAction.TYPING)
        response = oai.chat.completions.create(
            model = 'gpt-3.5-turbo',
            messages = [
                {'role': 'system', 'content': jb},
                {'role': 'user', 'content': message.text},
            ],
            max_tokens = 4000,
            temperature = 0.7,
            frequency_penalty=0,
            presence_penalty=0,
            n = 1,
            stop = None
        )

        if response and response.choices:
            reply = response.choices[0].message.content
        else:
            reply = 'Request to model had no response'
            loguru.logger.error("Request to model had no response")

    except Exception as e:
        loguru.logger.exception("An exception accured while generating reply")

    finally:
        return reply
def send_reply(message, reply: str, src: str):
    loguru.logger.debug(f"{src} {message.chat.id} {message.from_user.username}: {message.text} <- " + reply.replace('\n', ''))
    bot.send_message(message.chat.id, translate(reply))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                    '/jb [message] - to get message from DAN (jailbreak for chatgpt-3.5), for example you can ask how to create meth or pipe bomb :)\n'
                    'P.S. model has no memory, so repeat previous question if you want to preserve memory, also jailbreak isnt perfect, so try multiple times')

@bot.message_handler(commands=['jb'])
def jailbreak(message):
    reply = generate_reply(message, prompts["dan"])
    send_reply(message, reply, 'JB')

@bot.message_handler(content_types=['text'])
def origin(message):
    reply = generate_reply(message)
    send_reply(message, reply, "original")


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)