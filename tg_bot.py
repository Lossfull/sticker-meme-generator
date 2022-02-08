from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5298127450:AAG6r3CPGTphtVAzmLw-cqBQcTXOvY6GLeU'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text) # По факту просто сюда функцию вставить и в нее отправлять message.text


executor.start_polling(dp, skip_updates=True)