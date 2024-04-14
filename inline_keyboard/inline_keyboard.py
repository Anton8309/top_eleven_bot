from aiogram import Router
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.handler_text import (HandlerTextGk, HandlerTextDc, HandlerTextDlDr, HandlerTextDmc, HandlerTextMc,
                                   HandlerTextMlMr, HandlerTextAmlAmr, HandlerTextAmc, HandlerTextSt)

router_inline_keyboard = Router()


class InlineKeyboardPlayers:

    @staticmethod
    def get_inline_gk():
        buttons = [
            InlineKeyboardButton(text=HandlerTextGk.SKILLS, callback_data=HandlerTextGk.SKILLS),
            InlineKeyboardButton(text=HandlerTextGk.TRAINING, callback_data=HandlerTextGk.TRAINING),

        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_cd():
        buttons = [
            InlineKeyboardButton(text=HandlerTextDc.SKILLS, callback_data=HandlerTextDc.SKILLS),
            InlineKeyboardButton(text=HandlerTextDc.TRAINING, callback_data=HandlerTextDc.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_dl_dr():
        buttons = [
            InlineKeyboardButton(text=HandlerTextDlDr.SKILLS, callback_data=HandlerTextDlDr.SKILLS),
            InlineKeyboardButton(text=HandlerTextDlDr.TRAINING, callback_data=HandlerTextDlDr.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_dmc():
        buttons = [
            InlineKeyboardButton(text=HandlerTextDmc.SKILLS, callback_data=HandlerTextDmc.SKILLS),
            InlineKeyboardButton(text=HandlerTextDmc.TRAINING, callback_data=HandlerTextDmc.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_mc():
        buttons = [
            InlineKeyboardButton(text=HandlerTextMc.SKILLS, callback_data=HandlerTextMc.SKILLS),
            InlineKeyboardButton(text=HandlerTextMc.TRAINING, callback_data=HandlerTextMc.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_ml_mr():
        buttons = [
            InlineKeyboardButton(text=HandlerTextMlMr.SKILLS, callback_data=HandlerTextMlMr.SKILLS),
            InlineKeyboardButton(text=HandlerTextMlMr.TRAINING, callback_data=HandlerTextMlMr.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_aml_amr():
        buttons = [
            InlineKeyboardButton(text=HandlerTextAmlAmr.SKILLS, callback_data=HandlerTextAmlAmr.SKILLS),
            InlineKeyboardButton(text=HandlerTextAmlAmr.TRAINING, callback_data=HandlerTextAmlAmr.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_amc():
        buttons = [
            InlineKeyboardButton(text=HandlerTextAmc.SKILLS, callback_data=HandlerTextAmc.SKILLS),
            InlineKeyboardButton(text=HandlerTextAmc.TRAINING, callback_data=HandlerTextAmc.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup

    @staticmethod
    def get_inline_st():
        buttons = [
            InlineKeyboardButton(text=HandlerTextSt.SKILLS, callback_data=HandlerTextSt.SKILLS),
            InlineKeyboardButton(text=HandlerTextSt.TRAINING, callback_data=HandlerTextSt.TRAINING)
        ]
        inline_markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        return inline_markup


class InlineBackButton:
    @staticmethod
    def get_cmd_gk_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextGk.BACK, callback_data=HandlerTextGk.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_cmd_dc_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextDc.BACK, callback_data=HandlerTextDc.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_cmd_dl_dr_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextDlDr.BACK, callback_data=HandlerTextDlDr.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_cmd_dmc_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextDmc.BACK, callback_data=HandlerTextDmc.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_inline_mc_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextMc.BACK, callback_data=HandlerTextMc.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_cmd_ml_mr_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextMlMr.BACK, callback_data=HandlerTextMlMr.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_inline_aml_amr_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextAmlAmr.BACK, callback_data=HandlerTextAmlAmr.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_inline_amc_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextAmc.BACK, callback_data=HandlerTextAmc.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup

    @staticmethod
    def get_inline_st_back():
        button_back = [
            InlineKeyboardButton(text=HandlerTextSt.BACK, callback_data=HandlerTextSt.BACK)
        ]
        back_markup = InlineKeyboardMarkup(inline_keyboard=[button_back])
        return back_markup
