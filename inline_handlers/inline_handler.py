from aiogram import F, Router
from aiogram.handlers.callback_query import CallbackQuery

from inline_keyboard.inline_keyboard import InlineBackButton
from inline_keyboard.inline_keyboard import InlineKeyboardPlayers
from keyboards.keyboard import KeyBoardPlayer
from handlers.handler_text import HandlerText, HandlerTextGk
router_inline_handler = Router()


@router_inline_handler.callback_query(F.data == KeyBoardPlayer.GK)
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.answer(text=HandlerTextGk.SKILLS, reply_markup=InlineBackButton.get_cmd_gk_back())
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextGk.TRAINING)
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.answer(text=HandlerTextGk.TRAINING, reply_markup=InlineBackButton.get_cmd_gk_back())
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerText.BACK)
async def get_cmd_gk_back(callback: CallbackQuery):
    await callback.message.answer(text=f'{KeyBoardPlayer.GK}', reply_markup=InlineKeyboardPlayers.get_inline_gk())
    await callback.answer(text=None, show_alert=None)
