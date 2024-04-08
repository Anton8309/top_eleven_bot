from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.handler_text import HandlerText, HandlerTextGk

router_inline_keyboard = Router()


class InlineKeyboardPlayers:
    GK: str = 'gk'.upper()
    CD: str = 'cd'.upper()

    @staticmethod
    def get_inline_gk():
        buttons = [
            InlineKeyboardButton(text=HandlerTextGk.SKILLS, callback_data=InlineKeyboardPlayers.GK),
            InlineKeyboardButton(text=HandlerTextGk.TRAINING, callback_data=HandlerTextGk.TRAINING),

        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_cd():
        buttons = [
            InlineKeyboardButton(text='навыки', callback_data=InlineKeyboardPlayers.CD),
            InlineKeyboardButton(text='треневка', callback_data=InlineKeyboardPlayers.CD)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup


class InlineBackButton:
    @staticmethod
    def get_cmd_gk_back():
        button_back = [
            InlineKeyboardButton(text=HandlerText.BACK, callback_data=HandlerText.BACK)]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup
