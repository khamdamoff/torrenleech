#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    await message.reply_text(
        "please read the <a href='https://t.me/c/1434259219/99'>Pinned Message</a>",
        quote=True
    )
