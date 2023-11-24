from aiogram import types, Router, F
from aiogram import types, Dispatcher, Bot
from aiogram.utils.markdown import hcode
from aiogram.filters import CommandStart

from tgbot.keyboards import inline

router = Router()

@router.message()
async def bot_echo(message: types.Message):
    text = [
        "Эхо без состояния.",
        "Сообщение:",
        message.text
    ]

    await message.answer('\n'.join(text))
    await message.answer("Some text here", reply_markup=await inline.get_main_kb())

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer('Hello')