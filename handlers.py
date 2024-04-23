from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.types import FSInputFile
from aiogram.methods import send_document
import config
from xlsx_logic import find_name

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


# @router.message()
# async def message_handler(msg: Message):
#     if msg.from_user.id in user_id_required:
#         await msg.answer(f"привет Вовка")
#         print(f"Твой ID: {msg.from_user.id}")
#
#     await msg.answer(f"Твой ID: {msg.from_user.id}")
#     print(f"Твой ID: {msg.from_user.id}")


@router.message(Command("file"))
async def file_handler(msg: Message):
    if msg.from_user.id in config.user_id_required:
        await msg.answer_document(FSInputFile(config.path_to_main))


@router.message(Command("f"))
async def find_handler(msg: Message, command: CommandObject):
    if command.args is None:
        await msg.answer(
            "Ошибка: не переданы аргументы"
        )
        return

    await msg.answer(str(find_name(command.args)))
# /media/samba/private/main_file.xlsx
