#!/usr/bin/env python3
import asyncio
import functools

import odrive
from nicegui import ui

from controls import controls

ui.colors(primary='#6e93d6')

message = ui.markdown()


def show_message(text: str) -> None:
    message.content = text
    print(text, flush=True)


async def startup() -> None:
    try:
        show_message('# Searching for ODrive...')
        loop = asyncio.get_running_loop()
        odrv = await loop.run_in_executor(None, functools.partial(odrive.find_any, timeout=15))
        message.visible = False
        controls(odrv)
    except TimeoutError:
        show_message('# Could not find any ODrive...')
    await message.page.update()

ui.on_startup(startup)

ui.run(title='ODrive Motor Tuning')