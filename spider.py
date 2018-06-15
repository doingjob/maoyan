import requests
from requests.exceptions import RequestException
import re
def get_one_page(url):
    headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17" 
            }
    try:
        response=requests.get(url,headers=headers,timeout=2)
        if response.status_code==200:
            return response.text
        return None
    except RequestException as e:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    return items



def main():
    url="http://maoyan.com/board/4"
    html=get_one_page(url)
    items=parse_one_page(html)

    print(items)

if __name__=="__main__":
    main()
