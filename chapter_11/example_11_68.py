import urllib.request
def request(url):
    """지정한 url의 웹 문서를 요청하여, 본문을 반환한다."""
    response = urllib.request.urlopen(url)
    byte_date = response.read()
    text_data = byte_date.decode('utf-8')
    return text_data


