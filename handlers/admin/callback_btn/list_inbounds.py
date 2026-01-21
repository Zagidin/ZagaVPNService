from aiogram import Router, F, types
from api.api_core import get_auth_api

router = Router()


@router.callback_query(F.data == "list_inbounds")
async def show_all_data(callback: types.CallbackQuery):
    await callback.answer()

    api = await get_auth_api()

    try:
        inbounds = await api.inbound.get_list()

        if not inbounds:
            await callback.message.answer("❌ Инбаунды не найдены.")
            return

        msg = "<b>📊 СТРУКТУРА ПАНЕЛИ:</b>\n\n"

        for i in inbounds:
            msg += f"🔌 <b>[{i.protocol.upper()}] {i.remark}</b> (ID: {i.id})\n"

            if i.settings.clients:
                msg += "👥 <i>Список пользователей:</i>\n"
                for index, client in enumerate(i.settings.clients, 1):
                    client_info = f"  {index}. 📧 <code>{client.id}</code>"
                    used = round(client.total_gb / (1024 ** 3), 2) if client.total_gb else 0
                    msg += f"  {index}. 📧 {client.email} (Лимит: {used} GB)\n🆔{client.id}\n"
            else:
                msg += "  ⚠️ <i>Клиентов пока нет</i>\n"

            msg += "──────────────────\n"

        await callback.message.answer(msg, parse_mode="HTML")

    except Exception as e:
        await callback.message.answer(f"❌ Ошибка получения данных: {e}")
