from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram.methods import send_document


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
    print(f"Твой ID: {msg.from_user.id}")

@router.message(Command("file"))
async def file_handler(msg: Message):
    await msg.answer_document(FSInputFile(r"requirements.txt"))
