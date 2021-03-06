# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from . import *

START = """
πͺ **Help Menu** πͺ

β  /start : Check I am Alive or not.
β  /help : Get This Message.
β  /repo : Get Bot's Repo..

π§βπ» Join **@isIam07**
"""

ADMINTOOLS = """β **AdminTools** β

β’ /pin : Pinsπ the Replied Message
β’ /pinned : Get Pinned message in chat.
β’ /unpin : Unpin the Replied message
β’ /unpin all : Unpin all Pinned Messages.

β’ /ban (username/id/reply) : Ban the User
β’ /unban (username/id/reply) : UnBan the User.

β’ /mute (username/id/reply) : Mute the User.
β’ /unmute (username/id/reply) : Unmute the User.

β’ /tban (username/id/reply) (time) : Temporary ban a user
β’ /tmute (username/id/reply) (time) : temporary Mutes a User.

β’ /purge (purge messages)

β’ /setgpic (reply photo) : keep Chat Photo of Group.
β’ /delgpic : remove current chat Photo."""

UTILITIES = """
β ** Utilities ** β

β’ /info (reply/username/id) : get detailed info of user.
β’ /id : get chat/user id.
β’ /tr : Translate Languages..

β’ /paste (reply file/text) : paste content on Spaceb.in
β’ /meaning (text) : Get Meaning of that Word.
β’ /google (query) : Search Something on Google..

β’ /suggest (query/reply) : Creates a Yes / No Poll.
"""

LOCKS = """
β ** Locks ** β

β’ /lock (query) : lock particular content in chat.
β’ /unlock (query) : Unlock some content.

β’ All Queries
- `msgs` : for messages.
- `inlines` : for inline queries.
- `media` : for all medias.
- `games` : for games.
- `sticker` : for stickers.
- `polls` : for polls.
- `gif` : for gifs.
- `pin` : for pins.
- `changeinfo` : for change info right.
"""

MISC = """
β  **Misc**  β

β’ /joke : Get Random Jokes.
β’ /decide : Decide Something..
"""

STRINGS = {"Admintools": ADMINTOOLS, "locks": LOCKS, "Utils": UTILITIES, "Misc": MISC}

MNGE = udB.get("MNGR_EMOJI") or "β’"


def get_buttons():
    BTTS = []
    keys = STRINGS.copy()
    while keys:
        BT = []
        for i in list(keys)[:2]:
            text = MNGE + " " + i + " " + MNGE
            BT.append(Button.inline(text, "hlp_" + i))
            del keys[i]
        BTTS.append(BT)
    url = "https://t.me/" + asst.me.username + "?startgroup=true"
    BTTS.append([Button.url("Add me to Group", url)])
    return BTTS


@asst_cmd(pattern="help")
async def helpish(event):
    if not event.is_private:
        url = f"https://t.me/{asst.me.username}?start=start"
        return await event.reply(
            "Contact me in PM for help!", buttons=Button.url("Click me for Help", url)
        )
    if str(event.sender_id) in owner_and_sudos() and (
        udB.get("DUAL_MODE") and (udB.get("DUAL_HNDLR") == "/")
    ):
        return
    BTTS = get_buttons()
    await event.reply(START, buttons=BTTS)


@callback("mngbtn", owner=True)
async def ehwhshd(e):
    buttons = get_buttons()
    buttons.append([Button.inline("<< Back", "open")])
    await e.edit(buttons=buttons)


@callback("mnghome")
async def home_aja(e):
    await e.edit(START, buttons=get_buttons())


@callback(re.compile("hlp_(.*)"))
async def do_something(event):
    match = event.pattern_match.group(1).decode("utf-8")
    await event.edit(STRINGS[match], buttons=Button.inline("<< Back", "mnghome"))
