from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton

router_inline_keyboard = Router()


class InlineKeyboardPlayers:
    GK: str = 'gk'.upper()

    @staticmethod
    def get_inline_gk():
        buttons = [
            InlineKeyboardButton(text='навыки'.title(), callback_data='gk'),
            InlineKeyboardButton(text='тренеровка'.title(), callback_data='тренеровка'),

        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_cd():
        buttons = [
            InlineKeyboardButton(text='навыки'.title(), callback_data='cd'),
            InlineKeyboardButton(text='тренеровка'.title(), callback_data='cd')
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup


class InlineBackButton:
    @staticmethod
    def get_cmd_back():
        button_back = [
            InlineKeyboardButton(text='назад', callback_data='gk')        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup
