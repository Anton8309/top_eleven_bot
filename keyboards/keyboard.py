from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from handlers.handler_text import HandlerText


class KeyBoardPlayer:
    GK: str = 'gk'.upper()
    DC: str = 'dc'.upper()
    DLDR: str = 'dldr'.upper()
    DMC: str = 'dmc'.upper()
    MC: str = 'mc'.upper()
    MLMR: str = 'mlmr'.upper()
    AMLAMR: str = 'amlamr'.upper()

    @staticmethod
    def get_player_position():
        kb = [
            [KeyboardButton(text=KeyBoardPlayer.GK)],
            [KeyboardButton(text=KeyBoardPlayer.DC)],
            [KeyboardButton(text=KeyBoardPlayer.DLDR)],
            [KeyboardButton(text=KeyBoardPlayer.DMC)],
            [KeyboardButton(text=KeyBoardPlayer.MC)],
            [KeyboardButton(text=KeyBoardPlayer.MLMR)],
            [KeyboardButton(text=KeyBoardPlayer.AMLAMR)],

        ]
        markup_keyboards = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                               input_field_placeholder=HandlerText.TITLE)
        return markup_keyboards
