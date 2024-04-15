class HandlerText:
    HELLO: str = 'привет'.title()

    TITLE: str = 'Выберите позицию(кнопку) игрока!'

    HELP: str = ('<b>Ответы на возможные вопросы.</b>''\n''\n'
                 'Что, означает <b>(серый)</b> - это обозначает,''\n'
                 'что прокачка этого навыка у игрока на этой ''\n'
                 'позиции плохо влияет на его развитие.''\n''\n'
                 'Что, означает <b>(светлый)</b> - это обозначает, '
                 'что прокачка этого''\n'
                 'навыка у игрока на этой позиции хорошо влияет на его развите.''\n''\n'
                 'Что означает в упражнениях <b>(прессинг -6 упр.,</b> или <b>спортзал - 6 упр.,)</b>'
                 ' это означает количество установленных упражнений для прокачки игрока.''\n''\n'
                 'Что означает <b>(защита сред(115%) или меньше)</b> - '
                 'это означает до какого процентного '
                 'соотношения прокачивать тем или иным упражнением игрока.''\n''\n'
                 'Что, означаает цифра <b>[1]</b> на против упражения - это обозначает какое упражнение '
                 'по счету назначать игроку для прокачки навыков.')

    INFO: str = ('<b>name program: top_eleven_bot</b>''\n'
                 '<b>version: 1.0</b>''\n'
                 '<b>language: python 3.11 </b>''\n'
                 '<b>author: anton demidov</b>''\n'
                 '<b>link: https://github.com/Anton8309</b>'.title())


class HandlerTextGk:
    GK: str = 'голкипер 🥅'.title()
    SKILLS: str = 'навыки'.title()
    TRAINING: str = 'тренеровка'.title()
    BACK: str = 'назад'.title()


class HandlerTextDc:
    DC: str = 'центральный защитник ⚽'.title()
    SKILLS: str = '\tнавыки'.title()
    TRAINING: str = '\tтренеровка'.title()
    BACK: str = '\tназад'.title()


class HandlerTextDlDr:
    DLDR: str = ('правый и левый защитник ⚽'.title().
                 replace('И', 'и').
                 replace('З', 'з'))
    SKILLS: str = '\t\tнавыки'.title()
    TRAINING: str = '\t\tтренеровка'.title()
    BACK: str = '\t\tназад'.title()


class HandlerTextDmc:
    DMC: str = 'опорный полузащитник ⚽'.title()
    SKILLS: str = '\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\tтренеровка'.title()
    BACK: str = '\t\t\tназад'.title()


class HandlerTextMc:
    MC: str = 'центральный полузащитник ⚽'.title()
    SKILLS: str = '\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\tтренеровка'.title()
    BACK: str = '\t\t\t\tназад'.title()


class HandlerTextMlMr:
    MLMR: str = ('левый и правый полузащитник ⚽'.title().
                 replace('И', 'и').
                 replace('П', 'п').
                 replace('правый', 'Правый'))

    SKILLS: str = '\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\tтренеровка'.title()
    BACK: str = '\t\t\t\t\tназад'.title()


class HandlerTextAmlAmr:
    AMLAMR: str = (('левый и правый атакующий полузащитник ⚽'.title().
                    replace('И', 'и').
                    replace('П', 'п').
                    replace('правый', 'Правый')).
                   replace('А', 'а'))

    SKILLS: str = '\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\tтренеровка'.title()
    BACK: str = '\t\t\t\t\t\tназад'.title()


class HandlerTextAmc:
    AMC: str = (('центральный аткующий полузащитник ⚽'.title().
                 replace('А', 'а')).
                replace('П', 'п'))

    SKILLS: str = '\t\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\t\tтренеровка'.title()
    BACK: str = '\t\t\t\t\t\t\tназад'.title()


class HandlerTextSt:
    ST: str = 'нападающий ⚽'.title()

    SKILLS: str = '\t\t\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\t\t\tтренеровка'.title()
    BACK: str = '\t\t\t\t\t\t\t\tназад'.title()
