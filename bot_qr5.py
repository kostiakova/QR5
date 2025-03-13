# Your bot token
API_TOKEN = "7682234620:AAF5mFM_WXKgff5mG749PxFq1QNozJUXlLg"
from aiogram import Bot, Dispatcher, executor, types
from coderv2.encoder_qr5V2 import *
from re import search

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """

    This handler will be called when user sends `/start` or `/help` command
    492313908 - Lera
    """
    if message.from_user.id ==6955652822 or message.from_user.id == 492313908 or message.from_user.id == 534881754:
        await message.reply("Hello, Lera! I'm QR5bot!\nKostia made me to show You something...\nType here code you've recived in previous part. \nOnly english OR numbers OR symbols:\n"+
            "⚫⚪🟥🟩🟦")
    else: await message.reply("Hi!\nI'm QR5Bot!\nPowered by aiogram, made by Kostinus")

@dp.message_handler()
async def echo(message: types.Message):
    str_utf = ""
    str_colored = ""
    str_quin = ""

    if search(r'[a-zA-Z]', message.text):                                   #latinica
        str_utf = message.text
        str_quin = str_to_quin(str_utf)
        print(str_quin)
        str_colored = quin_to_color(str_quin)
    elif "⚫" in message.text or "🟩" in message.text or "⚪" in message.text:              #colors
        str_colored=message.text
        str_quin = color_to_quin(str_colored)
        str_utf = get_char_from_code(quin_to_dec(str_quin))
    else:                                                       #quinary
        str_utf = quin_to_str(message.text)
        print(str_quin)
        str_colored = quin_to_color((message.text))
        str_quin = message.text
    
    print(str_utf    + "\n" + str(message.from_user.id) + "\n")
    await message.answer(message.text + " == " + str_utf)
    await message.answer(str_colored)
    await message.answer("".join(sym for sym in " ".join(el for el in str_quin)))
    await bot.send_message(534881754, str_utf + " --- " + str(message.from_user.first_name))



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
