from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo

from app.kb import *


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение", reply_markup = user_main)

@router.message(F.text == ('❓узнать о боте'))
async def help_cmd(msg: Message):
    await msg.answer("иди отсюда")

@router.message(F.text == ('💩ара какиш'))
async def help_cmd(msg: Message):
    await msg.answer("ара иди отсюда")

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")