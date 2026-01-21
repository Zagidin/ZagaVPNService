import os
from py3xui import AsyncApi
from dotenv import load_dotenv

load_dotenv()


xui_api = AsyncApi(
    os.getenv("PANEL_URL"),
    os.getenv("PANEL_LOGIN"),
    os.getenv("PANEL_PASSWORD")
)

async def get_auth_api():

    await xui_api.login()

    return xui_api
