from aiogram import Router, F, types


router = Router()


@router.message(F.text)
async def ignore_message_usr(message: types.Message):
    await message.answer(
        f"Я вас не понял 😔\n"
        f"\nЕсли возникла проблема, попробуйте описать в обратной связи, администратор примяком вм поможет через некоторое время 😎"
    )
