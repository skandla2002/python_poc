from bs4 import BeautifulSoup
from urllib.request import urlopen


response = urlopen('https://datalab.naver.com/keyword/realtimeList.naver?age=all')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("새파일.txt", 'w')
for anchor in soup.select("span.item_title"):
    data = str(i) + "위 : " + anchor.get_text()
    print(data)
    i = i + 1
    f.write(data)
    f.write(str(i))
f.close()

# f.open()
# for anchor in soup.select("span.ah_k"):
#     data = str(i) + "위 : " + anchor.get_text() + "\n"
#     i = i + 1
#     f.write(data)
# f.close()