from pyrogram.types.messages_and_media import Messagefrom pyrogram import Client, filtersimport time

@client.on(events.NewMessage(pattern='^/botreklam ?(.*)'))async def duyuru(event): global grup_sayi,ozel_list sender = await event.get_sender() if sender.id not in ozel_list: return reply = await event.get_reply_message() await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...") for x in grup_sayi: try: await client.send_message(x,f"📣 Sponsor\n\n{reply.message}") except: pass await event.respond(f"Gönderildi.")
