import requests
from requests.exceptions import RequestException
import re
import json


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
    for item in items:
        yield{
                'index':item[0],
                'image':item[1],
                'title':item[2],
                'actors':item[3].strip()[3:],
                'time':item[4].strip()[5:],
                'score':item[5]+item[6]       
        }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) +'\n')
        f.close()




def main(offset):
    url="http://maoyan.com/board/4?offset="+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)


if __name__=="__main__":
    for i in range(10):
        main(i*10)
