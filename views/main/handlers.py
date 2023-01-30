from fastapi.responses import HTMLResponse
from fastapi import Request
from typing import Union


async def site_init():
    return {"Hello": "World"}


async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}