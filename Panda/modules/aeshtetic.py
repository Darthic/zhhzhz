# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from telethon import events

from .. import CMD_HANDLER as cmd
from .. import CMD_HELP
from ..misc import edit_or_reply, pandacute

PRINTABLE_ASCII = range(0x21, 0x7F)


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@pandacute(pattern="ae(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    text = "".join(aesthetify(text))
    await edit_or_reply(event, text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation


CMD_HELP.update(
    {
        "aeshtetic": f"**Plugin : **`aeshtetic`\
        \n\n  ➕  **Syntax :** `{cmd}ae <teks>`\
        \n  ➕  **Function : **Mengubah font teks Menjadi aeshtetic.\
    "
    }
)
