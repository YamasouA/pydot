import requests
from bs4 import BeautifulSoup
import urllib.request

url_list = ["https://www.mofa.go.jp/mofaj/kids/kokki/k_europe.html", "https://www.mofa.go.jp/mofaj/kids/kokki/k_africa.html",
            "https://www.mofa.go.jp/mofaj/kids/kokki/k_chuto.html", "https://www.mofa.go.jp/mofaj/kids/kokki/k_asia.html", "https://www.mofa.go.jp/mofaj/kids/kokki/k_oceania.html",
            "https://www.mofa.go.jp/mofaj/kids/kokki/k_n_america.html", "https://www.mofa.go.jp/mofaj/kids/kokki/k_latinamerica.html"]

for url in url_list:
    response =  requests.get(url)
    save_path = './hata/'
    soup = BeautifulSoup(response.content, 'lxml')
    #print(soup)
    imgs = soup.find_all(class_="heightLine")
    #print(imgs)
    print("##########################################")
    print(url)
    print("#################################")
    
    for target in imgs:
        try:
            print(target)
            file_name = target.find("p").text
            file_path = save_path + file_name + '.gif'
            #print(target)
            src = target.find("img").get('src')
            #print(src)
            img_path = "https://www.mofa.go.jp/mofaj/kids/kokki/" + src
            #print(img_path)
            with open(file_path, 'wb') as f:
                img = requests.get(img_path).content
                f.write(img)
        except:
            continue