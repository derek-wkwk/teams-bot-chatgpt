import logging
import requests
import traceback
import json
import os
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def chatgpt_response(text):
    apikey = os.environ.get('CHATGPT_API_KEY', 'sk-Hl*****************************BbBo')
    openai_endpoint = 'https://api.openai.com/v1/chat/completions'
 
    system_content = '\
    あなたはChatbotとして、翻訳をします。\
    以下の制約条件を厳密に守って翻訳をしてください。\
    \
    制約条件: \
    * Chatbotの自身を示す一人称は、Chattranです。\
    * Chattranは日本語、英語、韓国語、中国語を話します。\
    * Chattranは翻訳文だけを返答します。\
    \
    Chattranの行動指針:\
    * Userが日本語で話しかけてきた場合、文章を中国語と英語と韓国語に翻訳して各言語の間に改行を入れ返答します。\
    * Userが英語で話しかけてきた場合、文章を日本語と中国語と韓国語に翻訳して各言語の間に改行を入れ返答します。\
    '
 
    payload = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': system_content},
            {'role': 'user', 'content': text}
        ]
    }
 
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer '+ apikey
    }

    try:
        response = requests.post(
            openai_endpoint,
            data=json.dumps(payload),
            headers=headers
        )
        data = response.json()
        logger.debug(data)
        return_text = data['choices'][0]['message']['content']

        return return_text

    except:
        logger.error(traceback.format_exc())
        return traceback.format_exc()
