from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


class KeyBoardPlayer:
    GK: str = 'gk'.upper()
    CD: str = 'cd'.upper()

    @staticmethod
    def get_player_position():
        button_gk = KeyboardButton(text='gk'.upper())
        button_cd = KeyboardButton(text='cd'.upper())
        markup = ReplyKeyboardMarkup(keyboard=[[button_gk, button_cd]], resize_keyboard=True)
        return markup
