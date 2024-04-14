from aiogram import F, Router
from aiogram.handlers.callback_query import CallbackQuery
from inline_keyboard.inline_keyboard import InlineBackButton

from inline_keyboard.inline_keyboard import InlineKeyboardPlayers
from handlers.handler_text import (HandlerTextGk, HandlerTextDc, HandlerTextDlDr, HandlerTextDmc, HandlerTextMc,
                                   HandlerTextMlMr, HandlerTextAmlAmr)
from top_eleven.top_eleven_skill import (GOALKEEPER, DEFENDER, DEFENDER_DLDR, SUPPORTING, MIDFIELDER, MIDFIELDER_ML_MR,
                                         MIDFIELDER_AML_AMR)

router_inline_handler = Router()


# -------------------------------------------------GK------------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextGk.SKILLS)
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{GOALKEEPER.skill_gk}</b>',
        reply_markup=InlineBackButton.get_cmd_gk_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextGk.TRAINING)
async def get_inline_gk(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{GOALKEEPER.couch_gk}</b>',
        reply_markup=InlineBackButton.get_cmd_gk_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextGk.BACK)
async def get_cmd_gk_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextGk.GK}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_gk(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# -------------------------------------------------DC------------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextDc.SKILLS)
async def get_inline_dc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{DEFENDER.skill_dc}</b>',
        reply_markup=InlineBackButton.get_cmd_dc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDc.TRAINING)
async def get_inline_dc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{DEFENDER.coach_dc}</b>',
        reply_markup=InlineBackButton.get_cmd_dc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDc.BACK)
async def get_inline_dc_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextDc.DC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_cd(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# -------------------------------------------------DLDR----------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextDlDr.SKILLS)
async def get_inline_dl_dr(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{DEFENDER_DLDR.skill_dl_dr}</b>',
        reply_markup=InlineBackButton.get_cmd_dl_dr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDlDr.TRAINING)
async def get_inline_dl_dr(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{DEFENDER_DLDR.coach_dl_dr}</b>',
        reply_markup=InlineBackButton.get_cmd_dl_dr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDlDr.BACK)
async def get_inline_dl_dr_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextDlDr.DLDR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_dl_dr(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# -------------------------------------------------DMC-----------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextDmc.SKILLS)
async def get_inline_dmc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{SUPPORTING.skill_dmc}</b>',
        reply_markup=InlineBackButton.get_cmd_dmc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDmc.TRAINING)
async def get_inline_dmc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{SUPPORTING.coach_dmc}</b>',
        reply_markup=InlineBackButton.get_cmd_dmc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextDmc.BACK)
async def get_inline_dmc_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextDmc.DMC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_dmc(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# -------------------------------------------------MC------------------------------------------------------------------#

@router_inline_handler.callback_query(F.data == HandlerTextMc.SKILLS)
async def get_inline_mc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER.skill_mc}</b>',
        reply_markup=InlineBackButton.get_inline_mc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextMc.TRAINING)
async def get_inline_mc(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER.coach_mc}</b>',
        reply_markup=InlineBackButton.get_inline_mc_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextMc.BACK)
async def get_inline_mc_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextMc.MC}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_mc(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# --------------------------------------------------MLMR---------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextMlMr.SKILLS)
async def get_inline_ml_mr(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER_ML_MR.skill_ml_mr}</b>',
        reply_markup=InlineBackButton.get_cmd_ml_mr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextMlMr.TRAINING)
async def get_inline_ml_mr(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER_ML_MR.coach_ml_mr}</b>',
        reply_markup=InlineBackButton.get_cmd_ml_mr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextMlMr.BACK)
async def get_inline_ml_mr_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextMlMr.MLMR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_ml_mr(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


# --------------------------------------------------AMLAMR---------------------------------------------------------------#
@router_inline_handler.callback_query(F.data == HandlerTextAmlAmr.SKILLS)
async def get_inline_aml_amr_skills(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER_AML_AMR.skill_aml_amr}</b>',
        reply_markup=InlineBackButton.get_inline_aml_amr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextAmlAmr.TRAINING)
async def get_inline_aml_amr_training(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{MIDFIELDER_AML_AMR.coach_aml_amr}</b>',
        reply_markup=InlineBackButton.get_inline_aml_amr_back(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)


@router_inline_handler.callback_query(F.data == HandlerTextAmlAmr.BACK)
async def get_inline_aml_amr_back(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'<b>{HandlerTextAmlAmr.AMLAMR}</b>',
        reply_markup=InlineKeyboardPlayers.get_inline_aml_amr(),
        parse_mode='HTML'
    )
    await callback.answer(text=None, show_alert=None)
