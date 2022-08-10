import urllib.request
import json

TOKEN = '1178934754:AAGUR5T93yTA7ncs_r3m0b_Hxw8h_8fb4y0'

def request(url):
    """지정한 url의 웹 문서를 요청하여, 본문을 반환한다."""
    response = urllib.request.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode()
    return text_data


def build_url(method, query):
    """텔레그램 챗봇 웹 API에 요청을 보내기 위한 URL을 만들어 반환한다."""
    return f'http://api.telegram.org/bot{TOKEN}/{method}?{query}'


def request_to_chatbot_api(method, query):
    """메서드와 질의조건을 전달받아 텔레그램 챗봇 웹 API에 요청을 보내고 응답 결과를 사전 객체로 해석해 반환한다."""
    url = build_url(method, query)
    response = request(url)
    return json.loads(response)


def simplify_message(response):

    result = response['result']

    if not result:
        return None, []

    last_update_id = max(item['update_id'] for item in result)
    messages = [item['message'] for item in result]
    simplified_messages = [
        {'from_id': message['message_id'],
        'text': message['text']} for message in messages
    ]

    return last_update_id, simplified_messages


def get_updates(update_id):
    """챗봇 API로 update_id 이후에 수신한 메시지를 조회하여 반환한다."""
    query = f'offset={update_id}'
    response = request_to_chatbot_api(method='getUpdates', query=query)
    return simplify_message(response)


response = request_to_chatbot_api('getUpdates', 'offset=0')
last_update_id, simplified_message = simplify_message(response)
print(simplified_message)
print(get_updates(32))
text = urllib.parse.quote('안녕~~')
request_to_chatbot_api('sendMessage', f'chat_id=219819940&text={text}')