from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


class KeyBoardPlayer:
    GK: str = 'gk'.upper()
    DC: str = 'dc'.upper()
    DLDR: str = 'dldr'.upper()
    DMC: str = 'dmc'.upper()
    MC: str = 'mc'.upper()
    MLMR: str = 'mlmr'.upper()
    AML_AMR: str = 'aml_amr'.upper()

    @staticmethod
    def get_player_position():
        kb = [
            [KeyboardButton(text=KeyBoardPlayer.GK)],
            [KeyboardButton(text=KeyBoardPlayer.DC)],
            [KeyboardButton(text=KeyBoardPlayer.DLDR)],
            [KeyboardButton(text=KeyBoardPlayer.DMC)],
            [KeyboardButton(text=KeyBoardPlayer.MC)],
            [KeyboardButton(text=KeyBoardPlayer.MLMR)],
            [KeyboardButton(text=KeyBoardPlayer.AML_AMR)],

        ]
        markup_keyboards = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                               input_field_placeholder='Выберите позицию игрока!')
        return markup_keyboards
