from itertools import product


class SkillsCoach:
    def __init__(self):
        pass

    def __repr__(self):
        print('Класс-модуль!\n'
              'Скиллы и тренировка игроков!')


# Скиллы и тренировка игрока(вратарь GK)
@property
def skills_gk(self):
    skill_gk_1 = {

        'ЗАЩИТА ВОРОТ': ['[1]Рефлексы(светлый)''\n'
                         '[2]Ловкость(светлый)''\n'
                         '[3]Чутье(светлый)''\n'
                         '[4]Спешка(светлый)''\n'
                         '[5]Общение(светлый)''\n'
                         '[6]Бросок(светлый)''\n'
                         ]
    }

    skill_gk_2 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(серый)''\n'
                        '[4]Скорость(серый)''\n'
                        '[5]Креативность(серый)'
                        ]
    }

    skill_gk = [skill_gk_1.items(), skill_gk_2.items()]

    for sk_gk_1, sk_gk_2 in product(*skill_gk):
        return f"{sk_gk_1[0]}:\n{''.join(sk_gk_1[1])}\n" \
               f"{sk_gk_2[0]}:\n{''.join(sk_gk_2[1])}"


@property
def couching_gk(self):
    couch_gk = {

        'УПРАЖНЕНИЯ': ['[1]Тренировка вратаря-6упр.,''\n'
                       '[a](Защита ворот сред.,(105%))''\n'
                       '[b](Психофизика сред.,(51%))''\n'
                       '-------------------------------\n'
                       '[2]Один на один-6упр.,''\n'
                       '[a](Защита ворот сред.,(118%))''\n'
                       '[b](Психофизика сред.,(51%))''\n'
                       '-------------------------------\n'
                       '[3]Держать линию-6упр.,''\n'
                       '[a](Защита ворот сред.,(134%))''\n'
                       '[b](Психофизика сред.,(51%))''\n'
                       '-------------------------------\n'
                       '[4]Игра флангами-6упр.,''\n'
                       '[a](Защита ворот сред.,(146%))''\n'
                       '[b](Психофизика сред.,(51%))''\n'
                       '-------------------------------\n'
                       '[5]Пас рывок удар-3упр.,''\n'
                       'тренеровка техники-3упр.,''\n'
                       '[a](Защита ворот сред.,(155%))''\n'
                       '[b](Психофизика сред.,(55%))''\n'
                       '----------------------------\n'
                       '[6]Спортзал-6упр.,''\n'
                       '[a](Защита ворот сред.,(156%))''\n'
                       '[b](Психофизика сред.,(64%))''\n'
                       '-------------------------------\n'
                       '[7]Слалом-6упр.,''\n'
                       '[a](Защита ворот сред.,(156%)''\n'
                       '[b](Психофизика сред.,(68%))''\n'
                       '-------------------------------\n'
                       '[8]Собачка-3упр.,слалом-3упр.,''\n'
                       '[a](Защита ворот сред.,(156%))''\n'
                       '[b](Психофизика сред.,(81%))''\n'
                       '----------------------------\n'
                       '[9]Защита от навесов-6упр.,.''\n'
                       '[a](Защита ворот сред.,(157%))''\n'
                       '[b](Психофизика сред.,(81%))''\n'
                       ]
    }

    for couch in couch_gk.items():
        return f"{couch[0]}:\n{''.join(couch[1])}"


# Скиллы и тренировка(левый,правый защитник DL-DR)
@property
def skills_dl_dr(self):
    skill_dl_dr_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(светлый)''\n'
                   '[2]Опека(светлый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(серый)''\n'
                   '[5]Храбрость(светлый)''\n'
                   ]
    }

    skill_dl_dr_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(серый)''\n'
                      '[2]Дриблинг(серый)''\n'
                      '[3]Навес(светлый)''\n'
                      '[4]Удары(серый)''\n'
                      '[5]Завершение(серый)''\n'
                      ]
    }

    skill_dl_dr_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(светлый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(серый)'
                        ]
    }

    skill_dl_dr = [skill_dl_dr_1.items(), skill_dl_dr_2.items(), skill_dl_dr_3.items()]

    for sk_dl_dr_1, sk_dl_dr_2, sk_dl_dr_3 in product(*skill_dl_dr):
        return f"{sk_dl_dr_1[0]}:\n{''.join(sk_dl_dr_1[1])}\n" \
               f"{sk_dl_dr_2[0]}:\n{''.join(sk_dl_dr_2[1])}\n" \
               f"{sk_dl_dr_3[0]}:\n{''.join(sk_dl_dr_3[1])}"


@property
def coaching_dl_dr(self):
    coach_dl_dr = {

        'УПРАЖНЕНИЯ': ['[1]Прессинг-3упр.,'
                       'кариока с лестницей-3упр.\n'
                       '[a](Защита сред.,(111%))\n'
                       '[b](Нападение сред.,(40%))\n'
                       '[c](Психофизика сред.,(85%))''\n'
                       '-------------------------------\n'
                       '[2]Собачка-3упр.,разминка-3упр.\n'
                       '[a](Защита сред.,(120%))\n'
                       '[b](Нападение сред.,(42%))\n'
                       '[c](Психофизика сред.,(101%))''\n'
                       '-------------------------------\n'
                       '[3]Долгий забег-6упр.,\n'
                       '[a](Защита сред.,(120%))\n'
                       '[b](Нападение сред.,(42%))\n'
                       '[c](Психофизика сред.,(114%))''\n'
                       '-------------------------------\n'
                       '[4]Ускорение-6упр.,\n'
                       '[a](Защита сред.,(120%))\n'
                       '[b](Нападение сред.,(46%))\n'
                       '[c](Психофизика сред.,(131%))''\n'
                       '-------------------------------\n'
                       '[5]Слалом-6упр.,\n'
                       '[a](Защита сред.,(120%))\n'
                       '[b](Нападение сред.,(50%))\n'
                       '[c](Психофизика сред.,(140%))''\n'
                       '-------------------------------\n'
                       '[6]Защита от навесов-6упр.,\n'
                       '[a](Защита сред.,(137%))\n'
                       '[b](Нападение сред.,(57%))\n'
                       '[c](Психофизика сред.,(140%))''\n'
                       '-------------------------------\n'
                       '[7]Стандарты-6упр.,\n'
                       '[a](Защита сред.,(142%))\n'
                       '[b](Нападение сред.,(62%))\n'
                       '[c](Психофизика сред.,(140%))''\n'
                       '---------------------------------\n'
                       '[8]Видеоанализ-4упр.,один на один-2упр.,\n'
                       '[a](Защита сред.,(143%))\n'
                       '[b](Нападение сред.,(62%))\n'
                       '[c](Психиофизика сред.,(140))'

                       ]
    }

    for coach_dldr in coach_dl_dr.items():
        return f"{coach_dldr[0]}:\n{''.join(coach_dldr[1])}"


# Скиллы и тренировка(центральный защитник-DC)
@property
def skills_dc(self):
    skill_dc_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(светлый)''\n'
                   '[2]Опека(светлый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(светлый)''\n'
                   '[5]Храбрость(светлый)''\n'
                   ]
    }

    skill_dc_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(серый)''\n'
                      '[2]Дриблинг(серый)''\n'
                      '[3]Навес(серый)''\n'
                      '[4]Удары(серый)''\n'
                      '[5]Завершение(серый)''\n'
                      ]
    }

    skill_dc_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(светлый)''\n'
                        '[2]Сила(светлый)''\n'
                        '[3]Агрессивность(светлый)''\n'
                        '[4]Скорость(серый)''\n'
                        '[5]Креативность(серый)'
                        ]
    }

    skill_dc = [skill_dc_1.items(), skill_dc_2.items(), skill_dc_3.items()]

    for skil_dc_1, skil_dc_2, skil_dc_3 in product(*skill_dc):
        return f"{skil_dc_1[0]}:\n{''.join(skil_dc_1[1])}\n" \
               f"{skil_dc_2[0]}:\n{''.join(skil_dc_2[1])}\n" \
               f"{skil_dc_3[0]}:\n{''.join(skil_dc_3[1])}"


@property
def coaching_dc(self):
    coach_dc = {

        'УПРАЖНЕНИЯ': ['[1]Прессинг-6упр.,\n'
                       '[a](Защита сред.,(115%))\n'
                       '[b](Психофизика сред.,(64%))''\n'
                       '--------------------------------\n'
                       '[2]Спорт зал-6упр.,\n'
                       '[a](Защита сред.,(115%))\n'
                       '[b](Психофизика сред.,(96%))''\n'
                       '--------------------------------\n'
                       '[3]Разминка-6упр.,\n'
                       '[a](Защита сред.,(118%))\n'
                       '[b](Психофизика сред.,(103%))''\n'
                       '--------------------------------\n'
                       '[4]Остановить нападение-6упр.,\n'
                       '[a](Защита сред.,(125%))\n'
                       '[b](Психофизика сред.,(105%))''\n'
                       '--------------------------------\n'
                       '[5]Защита от навесов 6упр.,\n'
                       '[a](Защита сред.,(139%))\n'
                       '[b](Психофизика сред.,(105%))''\n'
                       '--------------------------------\n'
                       '[6]Долгий забег-2упр.,''\n'
                       'кариока с лестницей-4упр.,\n'
                       '[a](Защита сред.,(139%))\n'
                       '[b](Психиофизика сред.,(116%))''\n'
                       '---------------------------------\n'
                       '[7]Техника ударов-6упр.,\n'
                       '[a](Защита сред.,(139%))\n'
                       '[b](Психофизика сред.,(119%))''\n'
                       '----------------------------------\n'
                       '[8]Тренеровка техники-4упр.,''\n'
                       'стандарты-2упр.,\n'
                       '[a](Защита сред.,(145%))\n'
                       '[b](Психофизика сред.,(120%))''\n'
                       '----------------------------------\n'
                       '[9]Работай головой-6упр.,\n'
                       '[a](Защита сред.,(152%))\n'
                       '[b](Психофизика сред.,(122%))''\n'
                       '----------------------------------\n'
                       '[10]Игра флангами-6упр.,\n'
                       '[a](Защита сред.,(154%))\n'
                       '[b](Психофизика сред.,(122%))'
                       ]
    }

    for coach_dc in coach_dc.items():
        return f"{coach_dc[0]}:\n{''.join(coach_dc[1])}"


# Скиллы и тренировка(опорного полузащитника DMC)
@property
def skills_dmc(self):
    skill_dmc_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(светлый)''\n'
                   '[2]Опека(светлый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(светлый)''\n'
                   '[5]Храбрость(светлый)''\n'
                   ]
    }

    skill_dmc_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(серый)''\n'
                      '[3]Навес(серый)''\n'
                      '[4]Удары(серый)''\n'
                      '[5]Завершение(серый)''\n'
                      ]
    }

    skill_dmc_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(светлый)''\n'
                        '[2]Сила(светлый)''\n'
                        '[3]Агрессивность(светлый)''\n'
                        '[4]Скорость(серый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_dmc = [skill_dmc_1.items(), skill_dmc_2.items(), skill_dmc_3.items()]

    for skil_dmc_1, skil_dmc_2, skil_dmc_3 in product(*skill_dmc):
        return f"{skil_dmc_1[0]}:\n{''.join(skil_dmc_1[1])}\n" \
               f"{skil_dmc_2[0]}:\n{''.join(skil_dmc_2[1])}\n" \
               f"{skil_dmc_3[0]}:\n{''.join(skil_dmc_3[1])}"


@property
def coaching_dmc(self):
    coach_dmc = {

        'УПРАЖНЕНИЯ': ['[1]Прессинг-2упр., Собачка-4упр.,\n'
                       '[a](Защита сред.,(101%))\n'
                       '[b](Нападение сред.,(60%))\n'
                       '[c](Психофизика сред.,(79%))''\n'
                       '--------------------------------\n'
                       '[2]Прессинг-3упр., Спорт зал-3упр.,\n'
                       '[a](Защита сред.,(117%))\n'
                       '[b](Нападение сред.,(60%))\n'
                       '[c](Психофизика сред.,(112%))''\n'
                       '-------------------------------------\n'
                       '[3]Работай головой-2упр.,'
                       'Видеоанализ-4упр.,\n'
                       '[a](Защита сред.,(134%))\n'
                       '[b](Нападение сред.,(64%))\n'
                       '[c](Психофизика сред.,(120%))''\n'
                       '--------------------------------\n'
                       '[4]Остановить нападение-6упр.,\n'
                       '[a](Защита сред.,(148%))\n'
                       '[b](Нападение сред.,(66%))\n'
                       '[c](Психофизика сред.,(125%))''\n'
                       '----------------------------------------\n'
                       '[5]Кариока с лестницей-4упр.,'
                       'долгий забег-2упр.,\n'
                       '[a](Защита сред.,(148%))\n'
                       '[b](Нападение сред.,(66%))\n'
                       '[c](Психофизика сред.,(146%))''\n'
                       '--------------------------------\n'
                       '[6]Быстрые контратаки-6упр.,\n'
                       '[a](Защита сред.,(148%))\n'
                       '[b](Нападение сред.,(74%))\n'
                       '[c](Психофизика сред.,(151%))''\n'
                       '--------------------------------\n'
                       '[7]Стандарты-6упр.,\n'
                       '[a](Защита сред.,(161%))\n'
                       '[b](Нападение сред.,(81%))\n'
                       '[c](Психофизика сред.,(151%))''\n'
                       '------------------------------------------\n'
                       '[8]Техника ударов-4упр.,'
                       'быстрые контратаки-2упр.,\n'
                       '[a](Защита сред.,(161%))\n'
                       '[b](Нападение сред.,(95%))\n'
                       '[c](Психофизика сред.,(161%))''\n'
                       '---------------------------------\n'
                       '[9]Слалом-6упр.,\n'
                       '[a](Защита сред.,(161%))\n'
                       '[b](Нападение сред.,(97%))\n'
                       '[c](Психофизика сред.,(163%))'
                       ]
    }

    for coach_dmc in coach_dmc.items():
        return f"{coach_dmc[0]}:\n{''.join(coach_dmc[1])}"


# Скиллы и тренировка (полузащитника MC)
@property
def skills_mc(self):
    skill_mc_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(светлый)''\n'
                   '[2]Опека(светлый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(серый)''\n'
                   '[5]Храбрость(светлый)''\n'
                   ]
    }

    skill_mc_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(светлый)''\n'
                      '[3]Навес(серый)''\n'
                      '[4]Удары(светлый)''\n'
                      '[5]Завершение(серый)''\n'
                      ]
    }

    skill_mc_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ. форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(серый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_mc = [skill_mc_1.items(), skill_mc_2.items(), skill_mc_3.items()]

    for skil_mc_1, skil_mc_2, skil_mc_3 in product(*skill_mc):
        return f"{skil_mc_1[0]}\n{''.join(skil_mc_1[1])}\n" \
               f"{skil_mc_2[0]}\n{''.join(skil_mc_2[1])}\n" \
               f"{skil_mc_3[0]}\n{''.join(skil_mc_3[1])}"


@property
def coaching_mc(self):
    coach_mc = {

        'УПРАЖНЕНИЯ': ['[1]Видеоанализ-6упр.,''\n'
                       '[a](Защита сред.,(64%))''\n'
                       '[b](Нападение сред.,(73%))''\n'
                       '[c](Психофизика сред.,(72%))''\n'
                       '--------------------------------\n'
                       '[2]Тренировка техники-3упр.,'
                       'Работай головой-3упр.,''\n'
                       '[a](Защита сред.,(69%))''\n'
                       '[b](Нападение сред.,(77%))''\n'
                       '[c](Психофизика сред.,(76%))''\n'
                       '--------------------------------\n'
                       '[3]Быстрые контратаки-6упр.,''\n'
                       '[a](Защита сред.,(69%))''\n'
                       '[b](Нападение сред.,(90%))''\n'
                       '[c](Психофизика сред.,(82%))''\n'
                       '--------------------------------\n'
                       '[4]Долгий забег-6упр.,''\n'
                       '[a](Защита сред.,(69%))''\n'
                       '[b](Нападение сред.,(90%))''\n'
                       '[c](Психофизика сред.,(112%))''\n'
                       '--------------------------------\n'
                       '[5]Ускорение-6упр.,''\n'
                       '[a](Защита сред.,(69%))''\n'
                       '[b](Нападение сред.,(94%))''\n'
                       '[c](Психофизика сред.,(120%))''\n'
                       '--------------------------------\n'
                       '[6]Спорт зал-2упр.,'
                       'Кариока с лестницей-4упр.,''\n'
                       '[a](Защита сред.,(69%))''\n'
                       '[b](Нападение сред.,(94%))''\n'
                       '[c](Психофизика сред.,(139%))''\n'
                       '--------------------------------\n'
                       '[7]Прессинг-6упр.,''\n'
                       '[a](Защита сред.,(93%))''\n'
                       '[b](Нападение сред.,(94%))''\n'
                       '[c](Психофизика сред.,(142%))''\n'
                       '--------------------------------\n'
                       '[8]Стандарты-2упр.,Один на один-2упр.,'
                       'Остановить нападение-2упр.,''\n'
                       '[a](Защита сред.,(119%))''\n'
                       '[b](Нападение сред.,(114%))''\n'
                       '[c](Психофизика сред.,(144%))''\n'
                       '--------------------------------\n'
                       '[9]Техника ударов-2упр.,Стандарты-2упр.,'
                       'Игра флангами-2упр.,''\n'
                       '[a](Защита сред.,(122%))''\n'
                       '[b](Нападение сред.,(125%))''\n'
                       '[c](Психофизика сред.,(145%))''\n'
                       ]
    }

    for coach_mc in coach_mc.items():
        return f"{coach_mc[0]}\n{''.join(coach_mc[1])}"


# Скиллы и тренировка (крайний полузащитник ML/MR)
@property
def skills_ml_mr(self):
    skill_ml_mr_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(серый)''\n'
                   '[2]Опека(серый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(серый)''\n'
                   '[5]Храбрость(серый)''\n'
                   ]
    }

    skill_ml_mr_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(светлый)''\n'
                      '[3]Навес(светлый)''\n'
                      '[4]Удары(серый)''\n'
                      '[5]Завершение(серый)''\n'
                      ]
    }

    skill_ml_mr_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ. форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(серый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_ml_mr = [skill_ml_mr_1.items(), skill_ml_mr_2.items(), skill_ml_mr_3.items()]

    for skil_ml_mr_1, skil_ml_mr_2, skil_ml_mr_3 in product(*skill_ml_mr):
        return f"{skil_ml_mr_1[0]}\n{''.join(skil_ml_mr_1[1])}\n" \
               f"{skil_ml_mr_2[0]}\n{''.join(skil_ml_mr_2[1])}\n" \
               f"{skil_ml_mr_3[0]}\n{''.join(skil_ml_mr_3[1])}"


@property
def coaching_ml_mr(self):
    coach_ml_mr = {

        'УПРАЖНЕНИЯ': ['[1]Видеоанализ-6упр.,''\n'
                       '[a](Защита сред.,(39%)''\n'
                       '[b](Нападение сред.,(65%))''\n'
                       '[c](Психофизика сред.,(65%))''\n'
                       '-----------------------------\n'
                       '[2]Быстрые контратаки-6упр.,''\n'
                       '[a](Защита сред.,(39%))''\n'
                       '[b](Нападение сред.,(75%))''\n'
                       '[c](Психофизика сред.,(69%))''\n'
                       '-------------------------------\n'
                       '[3]Ускорение-6упр.,''\n'
                       '[a](Защита сред.,(39%))''\n'
                       '[b](Нападение сред.,(87%))''\n'
                       '[c](Психофизикка сред.,(94%))''\n'
                       '---------------------------------\n'
                       '[4]Долгий забег-6упр.,''\n'
                       '[a](Защита сред.,(39%))''\n'
                       '[b](Нападение сред.,(87%))''\n'
                       '[c](Психофизика сред.,(99%))''\n'
                       '-----------------------------------\n'
                       '[5]Спортивный зал-2упр.,'
                       'Кариока с лесницей-4упр.,''\n'
                       '[a](Защита сред.,(39%))''\n'
                       '[b](Нападение сред.,(87%))''\n'
                       '[c](Психофизика сред.,(122%))''\n'
                       '---------------------------------------\n'
                       '[6]Стандарты-3упр.,Игра флангами-3упр.,''\n'
                       '[a](Защита сред.,(45%))''\n'
                       '[b](Нападение сред.,(102%))''\n'
                       '[c](Психофизика сред.,(122%))''\n'
                       '---------------------------------------\n'
                       '[7]Держать линию-6упр.,''\n'
                       '[a](Защита сред.,(53%))''\n'
                       '[b](Нападение сред.,(102%))''\n'
                       '[c](Психофизика сред.,(122%))''\n'
                       ]
    }

    for coach_ml_mr in coach_ml_mr.items():
        return f"{coach_ml_mr[0]}\n{''.join(coach_ml_mr[1])}"


# Скиллы и тренировка(AML/AMR)
@property
def skills_aml_amr(self):
    skill_aml_amr_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(серый)''\n'
                   '[2]Опека(серый)''\n'
                   '[3]Выбор позиции(серый)''\n'
                   '[4]Удар головой(серый)''\n'
                   '[5]Храбрость(серый)''\n'
                   ]
    }

    skill_aml_amr_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(светлый)''\n'
                      '[3]Навес(светлый)''\n'
                      '[4]Удары(светлый)''\n'
                      '[5]Завершение(светлый)''\n'
                      ]
    }

    skill_aml_amr_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(серый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_aml_amr = [skill_aml_amr_1.items(), skill_aml_amr_2.items(), skill_aml_amr_3.items()]

    for skil_aml_amr_1, skil_aml_amr_2, skil_aml_amr_3 in product(*skill_aml_amr):
        return f"{skil_aml_amr_1[0]}\n{''.join(skil_aml_amr_1[1])}\n" \
               f"{skil_aml_amr_2[0]}\n{''.join(skil_aml_amr_2[1])}\n" \
               f"{skil_aml_amr_3[0]}\n{''.join(skil_aml_amr_3[1])}"


@property
def coaching_aml_amr(self):
    coach_aml_amr = {

        'УПРАЖНЕНИЯ': ['[1]Тренеровка техники-2упр.,''\n'
                       'Работай головой-2упр.,''\n'
                       'Видеоанализ-2упр.,''\n'
                       '[a](Защита сред.,(55%))''\n'
                       '[b](Нападение сред.,(76%))''\n'
                       '[c](Психофизика сред.,(76%))''\n'
                       '--------------------------------------------\n'
                       '[2]Быстрые контратаки-6упр.,''\n'
                       '[a](Защита сред.,(55%))''\n'
                       '[b](Нападение сред.,(99%))''\n'
                       '[c](Психофизика сред.,(84%))''\n'
                       '----------------------------------\n'
                       '[3]Долгий забег-6упр.,''\n'
                       '[a](Защита сред.,(55%))''\n'
                       '[b](Нападение сред.,(99%))''\n'
                       '[c](Психофизика сред.,(116%))''\n'
                       '-------------------------------------\n'
                       '[4]Спортивный зал-2упр.,'
                       'Кариока с лестницей-4упр.,''\n'
                       '[a](Защита сред.,(55%))''\n'
                       '[b](Нападение сред.,(100%))''\n'
                       '[c](Психофизика сред.,(146%))''\n'
                       '---------------------------------------\n'
                       '[5]Собачка-4упр.,'
                       'Кариока с лесницей-2упр.,''\n'
                       '[a](Защита сред.,(58%))''\n'
                       '[b](Нападение сред.,(103%))''\n'
                       '[c](Психофизика сред.,(154%))''\n'
                       '----------------------------------------\n'
                       '[6]Стандарты-4упр.,Игра флангами-2упр.,''\n'
                       '[a](Защита сред.,(72%))''\n'
                       '[b](Нападение сред.,(142%))''\n'
                       '[c](Психофизика сред.,(154%))''\n'
                       '-------------------------------------------\n'
                       '[7]Один на один-6упр.,''\n'
                       '[a](Защита сред.,(78%))''\n'
                       '[b](Нападение сред.,(158%))''\n'
                       '[c](Психофизика сред.,(155%))''\n'
                       ]
    }

    for coach_aml_amr in coach_aml_amr.items():
        return f"{coach_aml_amr[0]}\n{''.join(coach_aml_amr[1])}"


# Скиллы и тренировка(AMC)
@property
def skills_amc(self):
    skills_amc_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(серый)''\n'
                   '[2]Опека(серый)''\n'
                   '[3]Выбор пазиции(серый)''\n'
                   '[4]Удар головой(светлый)''\n'
                   '[5]Хоабрость(светлый)''\n'
                   ]
    }

    skills_amc_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(светлый)''\n'
                      '[3]Навес(серый)''\n'
                      '[4]Удары(светлый)''\n'
                      '[5]Завершение(светлый)''\n'
                      ]
    }

    skills_amc_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ. форма(светлый)''\n'
                        '[2]Сила(серый)''\n'
                        '[3]Агрессивность(светлый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_amc = [skills_amc_1.items(), skills_amc_2.items(), skills_amc_3.items()]

    for skil_amc_1, skil_amc_2, skil_amc_3 in product(*skill_amc):
        return f"{skil_amc_1[0]}\n{''.join(skil_amc_1[1])}\n" \
               f"{skil_amc_2[0]}\n{''.join(skil_amc_2[1])}\n" \
               f"{skil_amc_3[0]}\n{''.join(skil_amc_3[1])}"


@property
def coaching_amc(self):
    coach_amc = {

        'УПРАЖНЕНИЯ': ['[1]Долгий забег-6упр.,''\n'
                       '[a](Нападение сред.,(41%))''\n'
                       '[b](Защита сред.,(54%))''\n'
                       '[c](Психофизика сред(80%))''\n'
                       '--------------------------\n'
                       '[2]Тренеровка техники-6упр.,''\n'
                       '[a](Нападение сред.,(48%))''\n'
                       '[b](Защита сред.,(61%))''\n'
                       '[c](Психофизика сред.,(88%))''\n'
                       '----------------------------\n'
                       '[3]Работай головой-6упр.,''\n'
                       '[a](Нападение сред.,(57%))''\n'
                       '[b](Защита сред.,(66%))''\n'
                       '[c](Психофизика сред.,(93%))''\n'
                       '----------------------------\n'
                       '[4]Быстрые контратаки-6упр.,''\n'
                       '[a](Нападение сред.,(57%))''\n'
                       '[b](Защита сред.,(80%))''\n'
                       '[c](Психофизика сред.,(99%))''\n'
                       '----------------------------\n'
                       '[4]Пас рывок удар-6упр..''\n'
                       '[a](Нападение сред.,(57%))''\n'
                       '[b](Защита сред.,(93%))''\n'
                       '[c](Психофизика сред.,(105%))''\n'
                       '----------------------------\n'
                       '[5]Спорт зал-2упр.,''\n'
                       'Кариок с лестнице-4упр.,''\n'
                       '[a](Нападение сред.,(57%))''\n'
                       '[b](Защита сред.,(93%))''\n'
                       '[c](Психофизика сред.,(120%))''\n'
                       '----------------------------\n'
                       '[6]Техника ударов-6упр.,''\n'
                       '[a](Нападение сред.,(57%))''\n'
                       '[b](Защита сред.,(108%))''\n'
                       '[c](Психофизика сред.,(123%))''\n'
                       '----------------------------\n'
                       '[7]Стандарты-2упр.,''\n'
                       'Игра флангами-1упр.,''\n'
                       'Один на один-3упр.,''\n'
                       '[a](Нападение сред.,(64%))''\n'
                       '[b](Защита сред.,(122%))''\n'
                       '[c](Психофизика сред.,(123%))''\n'
                       '----------------------------\n'
                       '[8]Техника ударов-3упр.,''\n'
                       'Остановить нападение-3упр''\n'
                       '[a](Нападение сред.,(66%))''\n'
                       '[b](Защита сред.,(125%))''\n'
                       '[c](Психофихика сред.,(124%))'
                       ]
    }

    for coach_amc in coach_amc.items():
        return f"{coach_amc[0]}\n{''.join(coach_amc[1])}"


# Скиллы и тренирвка игрока нападающий(ST)
@property
def skills_st(self):
    skill_st_1 = {

        'ЗАЩИТА': ['[1]Отбор мяча(серый)''\n'
                   '[2]Опека(серый)''\n'
                   '[3]Выбор позиции(светлый)''\n'
                   '[4]Удар головой(светлый)''\n'
                   '[5]Храбрость(серый)'
                   ]
    }

    skill_st_2 = {

        'НАПАДЕНИЕ': ['[1]Передача(светлый)''\n'
                      '[2]Дриблинг(светлый)''\n'
                      '[3]Навес(серый)''\n'
                      '[4]Удары(светлый)''\n'
                      '[5]Завершение(светлый)'
                      ]
    }

    skill_st_3 = {

        'ПСИХОФИЗИКА': ['[1]Физ.форма(серый)''\n'
                        '[2]Сила(светлый)''\n'
                        '[3]Агрессивность(серый)''\n'
                        '[4]Скорость(светлый)''\n'
                        '[5]Креативность(светлый)'
                        ]
    }

    skill_st = [skill_st_1.items(), skill_st_2.items(), skill_st_3.items()]

    for skil_st_1, skil_st_2, skil_st_3 in product(*skill_st):
        return f"{skil_st_1[0]}\n{''.join(skil_st_1[1])}\n" \
               f"{skil_st_2[0]}\n{''.join(skil_st_2[1])}\n" \
               f"{skil_st_3[0]}\n{''.join(skil_st_3[1])}"


@property
def coaching_st(self):
    coach_st = {

        'УПРАЖНЕНИЯ': ['[1]Видеоанализ-6упр.,''\n'
                       '[a](Защита сред.,(62%))''\n'
                       '[b](Нападение сред.,(53%))''\n'
                       '[c](Психофизика сред.,(62%))''\n'
                       '-------------------------------\n'
                       '[2]Тренировка техники-3упр.,'
                       'Работай головой-3упр.,''\n'
                       '[a](Защита сред.,(72%))''\n'
                       '[b](Нападение сред.,(60%))''\n'
                       '[c](Психофизика сред.,(69%))''\n'
                       '-------------------------------\n'
                       '[3]Быстрые контратаки-6упр.,''\n'
                       '[a](Защита сред.,(72%))''\n'
                       '[b](Нападение сред.,(81%))''\n'
                       '[c](Психофизика сред.,(77%))''\n'
                       '-------------------------------\n'
                       '[4]Техника ударов-6упр.,''\n'
                       '[a](Защита сред.,(72%))''\n'
                       '[b](Нападение сред.,(108%))''\n'
                       '[c](Психофизика сред.,(90%))''\n'
                       '-------------------------------\n'
                       '[5]Пас рывок удар-6упр.,''\n'
                       '[a](Защита сред.,(72%))''\n'
                       '[b](Нападение сред.,(117%))''\n'
                       '[c](Психофизика сред.,(95%))''\n'
                       '----------------------------\n'
                       '[6]Челночный бег-6упр.,''\n'
                       '[a](Защита сред.,(76%))''\n'
                       '[b](Нападение сред.,(117%))''\n'
                       '[c](Психофизика сред.,(111%))''\n'
                       '----------------------------\n'
                       '[7]Ускорение-6упр.,''\n'
                       '[a](Защита сред.,(76%))''\n'
                       '[b](Нападение сред.,(129%))''\n'
                       '[c](Психофизика сред.,(129%))''\n'
                       '--------------------------------\n'
                       '[8]Остановить нападение-6упр.,''\n'
                       '[a](Защита сред.,(80%))''\n'
                       '[b](Нападение сред.,(132%))''\n'
                       '[c](Психофизика сред.,(132%))''\n'
                       '--------------------------------\n'
                       '[9]Спортивный зал-2упр.,'
                       'Кариока с лестницей-4упр.,''\n'
                       '[a](Защита сред.,(80%))''\n'
                       '[b](Нападение сред.,(132%))''\n'
                       '[c](Психофизика сред.,(139%))''\n'
                       '----------------------------\n'
                       '[10]Стандарты-6упр.,''\n'
                       '[a](Защита сред.,(88%))''\n'
                       '[b](Нападение сред.,(140%))''\n'
                       '[c](Психофизика сред.,(139%))''\n'
                       ]
    }

    for coach_st in coach_st.items():
        return f"{coach_st[0]}\n{''.join(coach_st[1])}"


def main():
    r = SkillsCoach()
    r.__repr__()


if __name__ == '__main__':
    main()
