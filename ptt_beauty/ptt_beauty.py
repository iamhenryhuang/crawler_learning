import requests
from bs4 import BeautifulSoup
import os

def download_img(url, save_path):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    print(f"正在下載圖片:{url}")
    #response = requests.get(url)
    response = requests.get(url, headers=headers)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print("-" * 30)

def main():
    url = "https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html"
    headers = {"Cookie": "over18=1"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())
    spans = soup.find_all("span", class_="article-meta-value")
    title = spans[2].text.strip()

    # 建立圖片資料夾
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        
    # 找尋網頁中所有圖片
    links = soup.find_all("a")
    allow_file_name = ["jpg", "png", "jpeg", "gif"]
    for link in links:
        href = link.get("href")
        if not href:
            continue
        file_name = href.split("/")[-1]
        extension = href.split(".")[-1].lower()
        if extension in allow_file_name:
            print(f"檔案型態:{extension}")
            print(f"url:{href}")
            download_img(url, f"{dir_name}/{file_name}")
        
if __name__ == "__main__":
    main()
