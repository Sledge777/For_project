from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo
from app.kb import *


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Напиши мне любую просьбу связанную с моими командами и я тебе помогу! Для ознакомления с командами напиши команду help", reply_markup = user_main)
    

@router.message(Command("help"))
async def start_handler(msg: Message):
    await msg.answer("Список команд бота: help ; me ; clean ; start audio")

@router.message(F.text == ('узнать о боте'))
async def help_cmd(msg: Message):
    await msg.answer("Я робот который предназначен для помощи и уборке по дому...")

@router.message(F.text == ('💩ара какиш'))
async def help_cmd(msg: Message):
    await msg.answer("ара иди отсюда")

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")