from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.data.requests import get_keyboard

async def get_main_kb():
    main_kb = InlineKeyboardBuilder()
    kb_buttons = await get_keyboard()
    for button in kb_buttons:
        main_kb.add(InlineKeyboardButton(text=button.button_name, callback_data=f'button_{button.id}'))
    main_kb.adjust(2, 2, 2, 1)
    return main_kb.as_markup()

