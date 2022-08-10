import urllib.request

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


import json
from pprint import pprint

def request_to_chatbot_api(method, query):
    """메서드와 질의조건을 전달받아 텔레그램 챗봇 웹 API에 요청을 보내고 응답 결과를 사전 객체로 해석해 반환한다."""
    url = build_url(method, query)
    response = request(url)
    return json.loads(response)


response = request_to_chatbot_api('getUpdates', 'offset=0')
pprint(response)



