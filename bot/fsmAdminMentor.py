from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.id.set()
        await message.answer("Введите свой айди")
    else:
        await message.answer("Пишите в группу!")
        await FSMAdmin.next()


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await FSMAdmin.next()
    await message.answer("Как вас зовут?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await FSMAdmin.next()
    await message.answer("Направление")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Сколько вам лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какая группа?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
    await FSMAdmin.next()
    await message.answer("Все верно?")


async def submit(message: types.Message, state: FSMContext):
    if message.text == "Да":
        # Подключение БД
        await state.finish()
        await message.answer("Регистрация завершена!")
    elif message.text == "Нет":
        await state.finish()
        await message.answer("Жаль!")
    else:
        await message.answer("Да или Нет!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)