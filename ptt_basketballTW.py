import requests

url = "https://www.ptt.cc/bbs/basketballTW/index.html"

response = requests.get(url)

#print(response.text)
if response.status_code == 200:
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("寫入成功")
else:
    print("沒有抓到網頁")
