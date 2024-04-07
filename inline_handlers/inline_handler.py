from aiogram import F, Router
from aiogram.handlers.callback_query import CallbackQuery
from inline_keyboard.inline_keyboard import InlineBackButton


router_inline_handler = Router()


@router_inline_handler.callback_query(F.data == 'gk')
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.answer(text='навыки'.title(),reply_markup=InlineBackButton.get_cmd_back())
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == 'тренеровка')
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.answer(text='тренеровка'.title(), reply_markup=InlineBackButton.get_cmd_back())
    await callback.answer(text=None, show_alert=None)
