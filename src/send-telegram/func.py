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
        print(str(bot_sendMessage))
        logging.getLogger().info("Message sent successfully")

    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    return response.Response(
        ctx, response_data=json.dumps(
            {"result": "sent successfully"}),
        headers={"Content-Type": "application/json"}
    )
