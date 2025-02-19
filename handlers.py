from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.types import FSInputFile
from aiogram.utils.formatting import as_list, as_marked_section, as_key_value, Bold

import config
from xlsx_logic import find_name, find_tel_name, find_name_n_ready, find_tel_cli, find_name_reamp, find_name_second

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Жду команду")


@router.message(Command("id"))
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")


@router.message(Command("file"))
async def file_handler(msg: Message):
    if msg.from_user.id in config.user_id_required:
        await msg.answer_document(FSInputFile(config.path_to_main))


@router.message(Command("f"))
async def find_handler(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_amp(find_name(command.args)))

@router.message(Command("s"))
async def find_handler(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_amp(find_name_second(command.args)))

@router.message(Command("r"))
async def find_handler_repr(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_reamp(find_name_reamp(command.args)))


@router.message(Command("t"))
async def find_handler(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_amp_tel(find_tel_name(command.args)))

@router.message(Command("n"))
async def find_handler_n_ready(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_amp_n_ready(find_name_n_ready(command.args)))

@router.message(Command("c"))
async def find_handler_cli_cont(msg: Message, command: CommandObject):
    if msg.from_user.id in config.user_id_required:
        if command.args is None:
            await msg.answer(
                "Ошибка: не переданы аргументы"
            )
            return

        await msg.answer(pretty_list_cli_cont(find_tel_cli(command.args)))


def pretty_list_amp(list_of_dict):
    final_str = ''
    for amp in list_of_dict:
        final_str += (as_list(
            as_marked_section(
                Bold("Найден:"),
                as_key_value("Пациент", amp['name']),
                as_key_value("Компания", amp['company']),
                as_key_value("Локализация", amp['localization']),
                as_key_value("Этап", amp['phase']),
                as_key_value("Группа", amp['group']),
                as_key_value("Место жительства", amp['live_loc']),
                marker="✅",
            ),
            sep="\n\n",
        ).as_html())

        final_str += "\n\n"

    if final_str == '':
        return "Не найдено"
    return final_str

def pretty_list_reamp(list_of_dict):
    final_str = ''
    for amp in list_of_dict:
        final_str += (as_list(
            as_marked_section(
                Bold("Найден:"),
                as_key_value("Пациент", amp['name']),
                as_key_value("Компания", amp['company']),
                as_key_value("Локализация", amp['localization']),
                as_key_value("Этап", amp['phase']),
                as_key_value("Группа", amp['group']),
                as_key_value("Номер культеприемной гильзы", amp['count_shell']),
                as_key_value("Место жительства", amp['live_loc']),
                marker="🔩",
            ),
            sep="\n\n",
        ).as_html())

        final_str += "\n\n"

    if final_str == '':
        return "Не найдено"
    return final_str

def pretty_list_cli_cont(list_of_dict):
    final_str = ''
    for amp in list_of_dict:
        final_str += (as_list(
            as_marked_section(
                Bold("Найден:"),
                as_key_value("Клиника", amp['name']),
                as_key_value("Сокращённо", amp['cli']),
                as_key_value("Контакты", amp['con']),
                as_key_value("Улица", amp['adr']),
                marker="📘",
            ),
            sep="\n\n",
        ).as_html())

        final_str += "\n\n"

    if final_str == '':
        return "Не найдено"
    return final_str


def pretty_list_amp_tel(list_of_dict):
    final_str = ''
    for amp in list_of_dict:
        final_str += (as_list(
            as_marked_section(
                Bold("Найден:"),
                as_key_value("Пациент", amp['name']),
                as_key_value("Дата рождения", amp['bd']),
                as_key_value("Локализация", amp['localization']),
                as_key_value("Клиника", amp['clinic']),
                as_key_value("Тел", amp['tel']),
                marker="📝",
            ),
            sep="\n\n",
        ).as_html())

        final_str += "\n\n"

    if final_str == '':
        return "Не найдено"
    return final_str

def pretty_list_amp_n_ready(list_of_dict):
    final_str = ''
    for amp in list_of_dict:
        final_str += (as_list(
            as_marked_section(
                Bold("Найден:"),
                as_key_value("Пациент", amp['name']),
                as_key_value("Локализация", amp['localization']),
                as_key_value("Компания", amp['company']),
                as_key_value("Причина", amp['reason']),
                as_key_value("План", amp['again']),
                marker="✍️",
            ),
            sep="\n\n",
        ).as_html())

        final_str += "\n\n"

    if final_str == '':
        return "Не найдено"
    return final_str

if __name__ == "__main__":
    print(pretty_list_amp(find_name("Иван")))
