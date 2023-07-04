import config
from aiogram import Bot, types, executor, Dispatcher
import openai
import telebot

openai.api_key = "***********************"

bot = telebot.TeleBot(token=config.token)
#dp = Dispatcher(bot)


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=2100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(message.chat.id, text=response['choices'][0]['text'])



bot.polling()

# @dp.message_handler(commands=["start", "help"])
# async def start(message: types.Message):
#     await message.answer("Hello, how can I help you?")

#if __name__ == "__main__":
#    executor.start_polling(dp)