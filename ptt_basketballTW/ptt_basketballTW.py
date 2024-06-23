# 模仿使用者爬蟲
import requests

url = "https://www.ptt.cc/bbs/basketballTW/index.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("寫入成功")
else:
    print("沒有抓到網頁")
