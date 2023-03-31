import requests
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def response_azure(event, message):
    access_token = fetch_access_token()

    id = event['id']
    recipient_id = event['recipient']['id']
    recipient_name = event['recipient']['name']
    conversatoin_id = event['conversation']['id']
    base_url = event['serviceUrl']
    # conversatoin_name = event['conversation']['name']

    data = {
        "type": "message",
        "from": {
            "id": recipient_id,
            "name": recipient_name
        },
        "conversation": {
            "id": conversatoin_id        
        },
        "recipient": {
            "id": recipient_id,
            "name": recipient_name
        },
        "text": message,
        "replyToId" : id
        }
    json_data = json.dumps(data)

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-type': 'application/json'
    }

    url = f'{base_url}v3/conversations/{conversatoin_id}/activities/{id}'
    response = requests.post(url, data=json_data, headers=headers)
    logger.debug(response)

    print(response)

def fetch_access_token():
    tenant_id = '7d25*************************f325'
    params = {
        'grant_type': 'client_credentials',
        'client_id': '142f*****************************89b3',
        'client_secret': 'JMN8********************************ecgP',
        'scope': 'https://api.botframework.com/.default'
    }
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    response = requests.post(url, data=params)

    access_token = json.loads(response.text)['access_token']
    return access_token
