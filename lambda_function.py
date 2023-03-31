import logging
import traceback
import os
import get_message
import azure_bot
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def lambda_handler(event, context):
    try:
        logger.debug(event)
        bot_name = os.environ.get('BOT_NAME', '')
        text = event['text'].replace(bot_name, '').replace('@', '').strip()
        # ChatGPTへの指示文
        order_text = '以下の文章を日本語、英語、中国語、韓国語に翻訳してください。それぞれの言語の間は改行をいれてください。\n'
        msg = order_text + text
        msg = get_message.chatgpt_response(msg)

        azure_bot.response_azure(event, msg)

        response = {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

        return response

    except:
        logger.error(traceback.format_exc())
        return traceback.format_exc()
