import asyncio
import aiogram
from aiogram import types
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
import random
from aiogram import types

bot = Bot(token='7801342975:AAF7UUbsM75GwNve3U5BMysa4yAqlPUjJi0')
dp = Dispatcher()
router = Router()

f = open('советы.txt', 'r', encoding='UTF-8')
sov = f.read().split('\n')
f.close()

@router.message(Command('start'))
async def send_welcome(message: Message):
    username = message.from_user.first_name
    kb = [
            [types.KeyboardButton(text='❓ Что такое ВСН?'),
            types.KeyboardButton(text='🧑‍🎓 Как поступить на ВСН?')],
            [types.KeyboardButton(text='📕 Вступительный экзамен по математике'),
            types.KeyboardButton(text='📝 Примеры заданий по математике')],
            [types.KeyboardButton(text='📌 Проходной балл в прошлом году'),
            types.KeyboardButton(text='🖊 Получить совет')]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Задай вопрос'
    )
    await message.answer('👋 ' + username + ''', привет!
    
💬 Этот бот сделан для помощи тем, кто заинтересовался программой "Вычислительные социальные науки" и хочет на неё поступить.

👇 Нажимай на кнопки, чтобы получить ответы на самые важные вопросы.

❤ Успехов!''', reply_markup=keyboard)

@router.message(F.text.lower() == '❓ что такое всн?')
async def what_is_vsn(message: Message):
    username = message.from_user.first_name
    await message.answer(username + ''',
    
🧑‍💻 Программа «Вычислительные социальные науки» готовит профессионалов, сочетающих глубокие современные знания в выбранной области социальных наук (политология/социология/ психология/государственное и муниципальное управление) и продвинутые компетенции в области анализа данных и математического моделирования.
      
🦾 Простым языком, помимо своей родовой программы ты будешь прокачивать свои навыки в анализе данных и математическом моделировании, которые позволят тебе быть хорошим специалистом как в социальных науках, так и в программировании.
      
😎 Эта программа является уникальной в России, при этом, окончив её, ты сможешь продолжить обучение в лучших университетах России и мира. Подробнее можешь ознакомиться на страничке программы https://www.hse.ru/ba/compsocsci/ или здесь, нажав на одну из кнопок''')


@router.message(F.text.lower() == '🧑‍🎓 как поступить на всн?')
async def how_to_go(message: Message):
    username = message.from_user.first_name
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Государственное и муниципальное управление", url="https://www.hse.ru/ba/gmu/")
    )
    builder.row(types.InlineKeyboardButton(
        text="Политология", url="https://www.hse.ru/ba/political/")
    )
    builder.row(types.InlineKeyboardButton(
        text="Психология", url="https://www.hse.ru/ba/psy/")
    )
    builder.row(types.InlineKeyboardButton(
        text="Социология", url="https://www.hse.ru/ba/soc/")
    )
    await message.answer(username + ''',

🧑‍💻 Поступление на программу "Вычислительные социальные науки" состоит из двух этапов:

1️⃣ Сначала ты должен поступить на одну из родовых программ Факультета социальных наук Вышки: ГМУ (государственное и муниципальное управление), политологию, психологию или социологию. Для этого необходимо сдать один из наборов экзаменов ЕГЭ. Или ты можешь немного взломать систему, поступив по олимпиаде :)

Чтобы лучше понять, что надо сделать для поступления на родовую программу, выбери ту, на которую хочешь поступить.

2️⃣ После зачисления на одну из родовых программ Факультета социальных наук в конце августа пройдёт дополнительный экзамен по математике для тех, кто хочет поступить на программу "Вычислительные социальные науки". Именно по его результатам будет зависеть твое поступление на ВСН.

❗ ВАЖНО! Именно результаты дополнительного испытания по математике являются определяющими при поступлении на ВСН.''', reply_markup=builder.as_markup())

@router.message(F.text.lower() == '📕 вступительный экзамен по математике')
async def pass_exam(message: Message):
    username = message.from_user.first_name
    await message.answer(username + ''',

📃 Вступительный экзамен по математике состоит из двух частей:

1️⃣ В первой части тебя ждёт 6 заданий. Для задач этой части указывается только ответ — не приводите полные решения задач. Ответ записывается в виде целого числа или конечной десятичной дроби. Стоимость каждого задания - 2 балла.

2️⃣ Во второй части тебя также ждет 6 заданий. Для задач этой части пишите полные решения. Стоимость каждого задания – 4 балла.

❗ Во многом темы для заданий вступительного испытания пересекаются с ЕГЭ по профильной математике и информатике. Со списком тем можно ознакомиться на сайте, посвященном вступительному испытанию: https://www.hse.ru/ba/compsocsci/maths.''')

@router.message(F.text.lower() == '📝 примеры заданий по математике')
async def choose_year(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="❓ Задания 2022", url="https://www.hse.ru/mirror/pubs/share/831050356.pdf")
    )
    builder.row(types.InlineKeyboardButton(
        text="✅ Ответы 2022", url="https://www.hse.ru/mirror/pubs/share/846208150.pdf")
    )
    builder.row(types.InlineKeyboardButton(
        text="❓ Задания 2023", url="https://www.hse.ru/mirror/pubs/share/889199172.pdf")
    )
    builder.row(types.InlineKeyboardButton(
        text="✅ Ответы 2023", url="https://www.hse.ru/mirror/pubs/share/889199294.pdf")
    )
    builder.row(types.InlineKeyboardButton(
        text="❓ Демоверсия 2024", url="https://www.hse.ru/data/2022/04/15/1789639529/demo_main.pdf")
    )
    builder.row(types.InlineKeyboardButton(
        text="✅ Ответы демоверсии", url="https://www.hse.ru/data/2022/04/15/1789638897/CSS_exam_demo_ans.pdf")
    )

    await message.answer(
        '🖊 Выбери год, за который ты хочешь прорешать задания/увидеть ответы',
        reply_markup=builder.as_markup()
    )

@router.message(F.text.lower() == '📌 проходной балл в прошлом году')
async def pass_exam(message: Message):
    username = message.from_user.first_name
    await message.answer(username + ''', проходной балл в прошлом году составил 17 баллов на бюджетные и 12 баллов - на коммерческие места.''')

@router.message(F.text.lower() == "🖊 получить совет")
async def give_sovet(message):
    username = message.from_user.first_name
    answer = random.choice(sov)
    await message.answer(username + ''', 

''' + answer)

@router.message(F.text)
async def repeat_text(message: Message):
    username = message.from_user.first_name
    await message.answer('🙏 ' + username + ''', пожалуйста, воспользуйся одной из кнопок ниже для работы с ботом. Если ты не смог получить ответ на свой вопрос, ты можешь присоединиться к общему чату абитуриентов ВСН по ссылке https://t.me/abitura_vsn. Там обязательно ответят!
    
С любовью, создатель бота❤''')

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())