import io
import json
import logging
import telegram

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    apiKEY = chatID = textMessage = ""
    try:
        body = json.loads(data.getvalue())
        apiKEY = body.get("api_key")
        chatID = body.get("chat_id")
        textMessage = body.get("text")

        tele_bot = telegram.Bot(token=apiKEY)
        bot_sendMessage = tele_bot.send_message(chat_id=chatID, text=textMessage)
        logging.getLogger().info("Message sent successfully")
        logging.getLogger().info(bot_sendMessage)
        send_status = 'succeed'

    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))
        send_status = 'failed'

    return response.Response(
        ctx, response_data=json.dumps({"status": format(send_status), "message_id" : format(bot_sendMessage.message_id)}),
        headers={"Content-Type": "application/json"}
    )