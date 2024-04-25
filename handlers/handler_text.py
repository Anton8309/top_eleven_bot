class HandlerText:
    HELLO: str = 'привет'.title()

    DESCRIPTION: str = ('Добро пожаловать в бота!''\n'
                        'Если будут вопросы загляни в menu >> help!')

    TITLE: str = 'Выберите позицию(кнопку) игрока!'

    HELP: str = ('<b>Как пользоваться ботом!</b>''\n''\n'
                 'Выбираем кнопку GK - в ней есть две кнопки,\n'
                 'навыки и тренировка.''\n'
                 'Нам нужна кнопка тренировка.''\n'
                 'В кнопке тренировка мы видим (УПРАЖЕНИНИЯ)!''\n'
                 '\t⚽ <b>Тренировка вратаря - 6упр.</b>''\n'
                 '\t⚽ <b>Заходим в игру</b>, и выбираем из списка состава''\n'
                 '\tнеобходимого нам по позиции игрока (голкипера),''\n'
                 '\tназначаем ему упражнения (тренировка вратаря)''\n'
                 '\tи ставим ему 6 упражнений.''\n'
                 '\t⚽ <b>Проводим тренировку</b> до тех пор, пока мы не''\n'
                 '\tполучим результат средний по проценту,''\n'
                 '\tа именно должно получиться так.''\n'
                 '\t<b>(Защита ворот сред.,(105%))</b>''\n'
                 '\t<b>(Психофизика сред.,(51%))</b>''\n'
                 '\t⚽ <b>Далее</b> все делаем по порядку как у казано в боте,''\n'
                 '\tвыбираем следующие упражнение под номером <b>2</b>''\n'
                 'и проводим тренировку игрока до тех процентных показателей,'
                 'как показано во втором упражнении.''\n'
                 '<b>Так выполняем все 9 упражнений.</b>''\n'
                 'В итоге у нас выходит довольно неплохой игрок.''\n'
                 'Приблизительная затрата игровых ресурсов составит от <b>300 до 500 аптек.</b>''\n'
                 '<b>Если игрок оказался талантливым</b>, то все процентные показатели достигнет быстро,''\n'
                 'и затраты могут быть ниже, приблизительно <b>300-350</b> игровых ресурсов.''\n'
                 '\t⚽ <b>Качать игроков необходимо от 3-х звезд, от 40% и с возрастом от 18 до 20 лет.</b>')

    INFO: str = ('<b>Name program: Top_Eleven_bot_24</b>''\n'
                 '<b>Version: 1.0</b>''\n'
                 '<b>Language: python 3.11 </b>''\n'
                 '<b>Library: aiogram 3.4.1</b>''\n'
                 '<b>Author: Anton Demidov</b>''\n'
                 '<b>link: https://github.com/Anton8309</b>')


class HandlerTextGk:
    GK: str = 'голкипер 🥅'.title()
    SKILLS: str = 'навыки'.title()
    TRAINING: str = 'тренировка'.title()
    BACK: str = 'назад'.title()


class HandlerTextDc:
    DC: str = 'центральный защитник ⚽'.title()
    SKILLS: str = '\tнавыки'.title()
    TRAINING: str = '\tтренировка'.title()
    BACK: str = '\tназад'.title()


class HandlerTextDlDr:
    DLDR: str = ('правый и левый защитник ⚽'.title().
                 replace('И', 'и').
                 replace('З', 'з'))
    SKILLS: str = '\t\tнавыки'.title()
    TRAINING: str = '\t\tтренировка'.title()
    BACK: str = '\t\tназад'.title()


class HandlerTextDmc:
    DMC: str = 'опорный полузащитник ⚽'.title()
    SKILLS: str = '\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\tтренировка'.title()
    BACK: str = '\t\t\tназад'.title()


class HandlerTextMc:
    MC: str = 'центральный полузащитник ⚽'.title()
    SKILLS: str = '\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\tтренировка'.title()
    BACK: str = '\t\t\t\tназад'.title()


class HandlerTextMlMr:
    MLMR: str = ('левый и правый полузащитник ⚽'.title().
                 replace('И', 'и').
                 replace('П', 'п').
                 replace('правый', 'Правый'))

    SKILLS: str = '\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\tтренировка'.title()
    BACK: str = '\t\t\t\t\tназад'.title()


class HandlerTextAmlAmr:
    AMLAMR: str = (('левый и правый атакующий полузащитник ⚽'.title().
                    replace('И', 'и').
                    replace('П', 'п').
                    replace('правый', 'Правый')).
                   replace('А', 'а'))

    SKILLS: str = '\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\tтренировка'.title()
    BACK: str = '\t\t\t\t\t\tназад'.title()


class HandlerTextAmc:
    AMC: str = (('центральный атакующий полузащитник ⚽'.title().
                 replace('А', 'а')).
                replace('П', 'п'))

    SKILLS: str = '\t\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\t\tтренировка'.title()
    BACK: str = '\t\t\t\t\t\t\tназад'.title()


class HandlerTextSt:
    ST: str = 'нападающий ⚽'.title()

    SKILLS: str = '\t\t\t\t\t\t\t\tнавыки'.title()
    TRAINING: str = '\t\t\t\t\t\t\t\tтренировка'.title()
    BACK: str = '\t\t\t\t\t\t\t\tназад'.title()
