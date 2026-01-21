import uuid
import time
import random
from os import getenv
from py3xui import Client
from urllib.parse import quote
from dotenv import load_dotenv
from aiogram import Router, types
from aiogram.filters import Command
from api.api_core import get_auth_api


load_dotenv()

SERVER_IP = getenv("SERVER_IP")
SERVER_PORT = getenv("SERVER_PORT")
INBOUND_ID = int(getenv("INBOUND_ID"))
PUBLIC_KEY = getenv("PUBLIC_KEY")
SHORT_IDs = getenv("SHORT_IDs").split(",")
SNI = getenv("SNI")

router = Router()


@router.message(Command("add_user"))
async def add_user(message: types.Message):

    api = await get_auth_api()

    user_uuid = str(uuid.uuid4())
    user_email = str(message.from_user.username) # потом попросим юзера ввести имя

    # Срок действия: текущее время + 30 дней в миллисекундах
    # expiry_time = int((time.time() + 30 * 24 * 60 * 60) * 1000)
    expiry_time = int((time.time() + 60) * 1000)
    # Лимит трафика: 50 ГБ (в байтах)
    limit_traffic = 50 * 1024 * 1024 * 1024

    client = Client(
        enable=True,
        email=user_email,
        id=user_uuid,
        total_gb=limit_traffic,
        expiry_time=expiry_time,
        tg_id=message.from_user.id,
        comment="Zagidin Magamedragimov",
        flow="xtls-rprx-vision"
    )

    try:
        await api.client.add(INBOUND_ID, [client])

        random_sid = random.choice(SHORT_IDs)

        remark = f"VPN ZAGA-{user_email}"
        safe_remark = quote(remark)

        vless_link = (
            f"vless://{user_uuid}@{SERVER_IP}:{SERVER_PORT}?"
            f"type=tcp&"
            f"encryption=none&"
            f"security=reality&"
            f"pbk={PUBLIC_KEY}&"
            f"fp=chrome&"
            f"sni={SNI}&"
            f"sid={random_sid}&"
            f"spx=%2F&"
            f"flow=xtls-rprx-vision#{safe_remark}"
        )

        await message.answer(
            f"✅ <b>Клиент добавлен!</b>\n\n"
            f"📧 Email: <code>{user_email}</code>\n"
            f"🔑 UUID: <code>{user_uuid}</code>\n\n"
            f"🔗 <b>Ссылка для подключения:</b>\n"
            f"<code>{vless_link}</code>",
            parse_mode="HTML"
        )

    except Exception as e:
        await message.answer(f"❌ Ошибка при добавлении: {e}")