class HandlerText:
    HELLO: str = 'привет'.title()

    DESCRIPTION: str = ('Добро пожаловать в бота!''\n'
                        'Если будут вопросы загляни в menu >> help!')

    TITLE: str = 'Выберите позицию(кнопку) игрока!'

    HELP: str = 'Временно не работает!'

    INFO: str = ('<b>Name program: Top_Eleven_bot_24</b>''\n'
                 '<b>Version: 1.0</b>''\n'
                 '<b>Language: python 3.11 </b>''\n'
                 '<b>Library: aiogram 3.4.1</b>''\n'
                 '<b>Author: Anton Demidov</b>''\n'
                 '<b>link: https://github.com/Anton8309</b>')


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
