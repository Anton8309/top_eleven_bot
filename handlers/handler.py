from aiogram import Router, F
from aiogram.handlers.message import Message
from aiogram.filters.command import CommandStart

from handlers.handler_text import (HandlerText, HandlerTextGk, HandlerTextDc, HandlerTextDlDr, HandlerTextDmc,
                                   HandlerTextMc, HandlerTextMlMr, HandlerTextAmlAmr, HandlerTextAmc)
from keyboards.keyboard import KeyBoardPlayer
from inline_keyboard.inline_keyboard import InlineKeyboardPlayers

router_handler = Router()


@router_handler.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        text=f'<b>{HandlerText.HELLO} {message.from_user.full_name}!</b>',
        reply_markup=KeyBoardPlayer.get_player_position(), parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.GK)
async def cmd_gk(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextGk.GK}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_gk(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.DC)
async def cmd_cd(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextDc.DC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_cd(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.DLDR)
async def cmd_dl_dr(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextDlDr.DLDR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_dl_dr(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.DMC)
async def cmd_dmc(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextDmc.DMC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_dmc(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.MC)
async def cmd_mc(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextMc.MC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_mc(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.MLMR)
async def cmd_ml_mr(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextMlMr.MLMR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_ml_mr(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.AMLAMR)
async def cmd_aml_amr(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextAmlAmr.AMLAMR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_aml_amr(),
        parse_mode='HTML'
    )


@router_handler.message(F.text == KeyBoardPlayer.AMC)
async def cmd_amc(message: Message):
    await message.answer(
        text=f'<b>{HandlerTextAmc.AMC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_amc(),
        parse_mode='HTML'
    )
