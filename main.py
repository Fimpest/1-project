from aiogram import executor, Dispatcher, Bot, types
from aiogram.dispatcher.filters import Text
from Keyboards import kb, kb1, kb2
from config import token
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class Test(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()


bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

answer1 = ''


# @dp.message_handler(Text(equals="AaA"))
# async def Test_123(message: types.Message):
#     print(message)


@dp.message_handler(Text(equals="Получить лучшие условия"))
async def kb_4(message: types.Message):
    await message.answer(text='Благодарим за обращение в транспортную компанию <b>«ЭКСПРЕСС»</b>!\n'
                              'Наш менеджер свяжется с Вами в ближайшее время.\n'
                              '<b>Хорошего</b> дня!', parse_mode='HTML', reply_markup=kb2)


@dp.message_handler(commands=['start'], state='*')
@dp.message_handler(Text(equals='Главное меню'), state='*')
async def start_and_kb_5(message: types.Message, state: FSMContext):
    await message.answer(text="Спасибо за обращение в Транспортную компанию <b>«ЭКСПРЕСС»</b>!\n"
                              "\nДля расчета стоимости выберите тип контейнера:", parse_mode="HTML", reply_markup=kb)
    await state.finish()


@dp.message_handler(Text(equals='20’DC'))
@dp.message_handler(Text(equals='40’DC'))
@dp.message_handler(Text(equals='40’HC'))
@dp.message_handler(Text(equals='Перезвоните мне'))
async def application_data(message: types.Message):
    global answer1
    answer1 = message.text
    await message.answer(text='Как вас зовут:', reply_markup=kb2)
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def number_data(message: types.Message, state: FSMContext):
    await state.update_data(
        {"answer1": message.text})
    await message.answer(text=f"Рады сотрудничеству, {message.text}!"
                              "\nВаш номер телефона?")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def number_data(message: types.Message, state: FSMContext):
    await state.update_data(
        {"answer2": message.text})
    await message.answer(f"Ваш номер - {message.text}!"
                         "\nНазвание вашей организации:")
    await Test.next()


@dp.message_handler(state=Test.Q3)
async def number_data(message: types.Message, state: FSMContext):
    await state.update_data(
        {"answer3": message.text})
    data = await state.get_data()
    application = [answer1, data.get("answer1"), data.get("answer2"), data.get("answer3")]
    print(application)
    await message.answer(text=f"Название вашей организации - {message.text}!"
                              "\nЗаявка закончена", reply_markup=kb1)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
