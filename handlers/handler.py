from aiogram import Router, F
from aiogram.handlers.message import Message
from aiogram.filters.command import CommandStart
from handlers.handler_text import HandlerText
from keyboards.keyboard import KeyBoardPlayer
from inline_keyboard.inline_keyboard import InlineKeyboardPlayers

router_handler = Router()


@router_handler.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=f'<b>{HandlerText.HELLO} {message.from_user.full_name}!</b>', parse_mode='HTML',
                         reply_markup=KeyBoardPlayer.get_player_position())


@router_handler.message(F.text.lower() == 'gk')
async def cmd_gk(message: Message):
    await message.answer(text=f'{KeyBoardPlayer.GK}', reply_markup=InlineKeyboardPlayers.get_inline_gk())


@router_handler.message(F.text.lower() == 'cd')
async def cmd_cd(message: Message):
    await message.answer(text=f'{KeyBoardPlayer.CD}', reply_markup=InlineKeyboardPlayers.get_inline_cd())
