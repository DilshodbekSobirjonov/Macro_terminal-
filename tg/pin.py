from tg.client import bot, CHANNEL_ID

def update_pin(text):
    try:
        bot.unpin_all_chat_messages(CHANNEL_ID)
    except:
        pass
    msg = bot.send_message(CHANNEL_ID, text)
    bot.pin_chat_message(CHANNEL_ID, msg.message_id)

