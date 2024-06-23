from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio
from aiohttp import web
from plugins import web_server

PORT = "8000"

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [    
    'https://telegra.ph/file/84321ef01763fcb981806.gif',
    'https://telegra.ph/file/84321ef01763fcb981806.gif'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**<b>Hello {}\n\n⚠️Access Denied!⚠️\n\nSubscribe My channel To Use me\n\n𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐇𝐃 𝐌𝐨𝐯𝐢𝐞𝐬\n👉 https://t.me/+4Fxg05W56SVkOTY1\n\n𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐌𝐨𝐯𝐢𝐞𝐬\n👉 https://t.me/+5MMPfVCCiAU5MjU1\n\nBollywood Hindi HD MOVIES\n👉 https://t.me/+sIUMbwiAsIo4Mjll\n\nTamil Telugu Malayalam Movies 🎥\n👉 https://t.me/+hJLWDbymVZsyOTk1\n\nHollywood action movie\n👉 https://t.me/+zHXxf4Y5ve03YThl\n\n18+ Baned Movies A Rated movie Only 🔞\n👉 https://t.me/+GwoURlq-hr1hOTc9\n\n𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐃\n👉 https://t.me/+EVHwFEL-OWdlMjM1\n\nSex Video porn video\n👉 https://t.me/+P-wgbt_2dlU3MTM1\n\nMovies 🎥\n👉https://t.me/+LpVX0gNfgEM5ZjE1\n\n©️@ROCKERSBACKUP.If you joined click check again button to confirm.</b>**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
 
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        await app.get_chat_member(cfg.CHID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:    
            add_user(m.from_user.id)
            await m.reply_text("**I'm an auto approve [Admin Join Requests]({}) Bot.I can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission join here for New Movie https://t.me/+D7L-rX9lKA43MGRl Backup channel :- @ROCKERSBACKUP**")
    
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="http://t.me/autorequistacceptnewbot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("** Hello start me private for more details @ROCKERSBACKUP**")
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔎 Check Again 🚀", "chk")
                ]
            ]
        )
        await m.reply_text("**<b>Hello {}\n\n⚠️Access Denied!⚠️\n\nSubscribe My channel To Use me\n\n𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐇𝐃 𝐌𝐨𝐯𝐢𝐞𝐬\n👉 https://t.me/+4Fxg05W56SVkOTY1\n\n𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐌𝐨𝐯𝐢𝐞𝐬\n👉 https://t.me/+5MMPfVCCiAU5MjU1\n\nBollywood Hindi HD MOVIES\n👉 https://t.me/+sIUMbwiAsIo4Mjll\n\nTamil Telugu Malayalam Movies 🎥\n👉 https://t.me/+hJLWDbymVZsyOTk1\n\nHollywood action movie\n👉 https://t.me/+zHXxf4Y5ve03YThl\n\n18+ Baned Movies A Rated movie Only 🔞\n👉 https://t.me/+GwoURlq-hr1hOTc9\n\n𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐃\n👉 https://t.me/+EVHwFEL-OWdlMjM1\n\nSex Video porn video\n👉 https://t.me/+P-wgbt_2dlU3MTM1\n\nMovies 🎥\n👉https://t.me/+LpVX0gNfgEM5ZjE1\n\n©️@ROCKERSBACKUP.If you joined click check again button to confirm.</b>**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb : CallbackQuery):
    try:
        await app.get_chat_member(cfg.CHID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:            
            add_user(cb.from_user.id)
            await cb.message.edit("**I'm an auto approve [Admin Join Requests]({}) Bot.I can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission Backup channel @ROCKERSBACKUP**")
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")
    app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

print("I'm Alive Now!")
app.run()
