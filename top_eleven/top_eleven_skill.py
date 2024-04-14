from top_eleven.modul_skill_coach import skills_gk, skills_dl_dr, skills_dc  # Защита
from top_eleven.modul_skill_coach import couching_gk, coaching_dl_dr, coaching_dc  # Защита
from top_eleven.modul_skill_coach import skills_dmc, skills_mc, skills_ml_mr  # полузащита
from top_eleven.modul_skill_coach import coaching_dmc, coaching_mc, coaching_ml_mr  # полузащита
from top_eleven.modul_skill_coach import skills_aml_amr, skills_amc, skills_st  # атака
from top_eleven.modul_skill_coach import coaching_aml_amr, coaching_amc, coaching_st  # атака


class GK:
    # GK
    name_class = 'GK'
    skill_gk = skills_gk
    couch_gk = couching_gk


GOALKEEPER = GK()


class DLDR:
    # DL-DR
    name_class = 'DL-DR'
    skill_dl_dr = skills_dl_dr
    coach_dl_dr = coaching_dl_dr


DEFENDER_DLDR = DLDR()


class DC:
    # DC
    name_class = 'DC'
    skill_dc = skills_dc
    coach_dc = coaching_dc


DEFENDER = DC()


class DMC:
    # DMC
    name_class = 'DMC'
    skill_dmc = skills_dmc
    coach_dmc = coaching_dmc


SUPPORTING = DMC()


class MC:
    # MC
    name_class = 'MC'
    skill_mc = skills_mc
    coach_mc = coaching_mc


MIDFIELDER = MC()


class MLMR:
    # MLMR
    name_class = 'ML-MR'
    skill_ml_mr = skills_ml_mr
    coach_ml_mr = coaching_ml_mr


MIDFIELDER_ML_MR = MLMR()


class AMLAMR:
    # AMLAMR

    name_class = 'AML-AMR'
    skill_aml_amr = skills_aml_amr
    coach_aml_amr = coaching_aml_amr


MIDFIELDER_AML_AMR = AMLAMR()


class AMC:
    # AMC
    name_class = 'AMC'
    skill_amc = skills_amc
    coach_amc = coaching_amc


MIDFIELDER_AMC = AMC()


class ST:
    # ST
    name_class = 'ST'
    skill_st = skills_st
    coach_st = coaching_st


ATTACK = ST()
