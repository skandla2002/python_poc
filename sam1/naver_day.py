from bs4 import BeautifulSoup
from urllib.request import urlopen
with urlopen('https://datalab.naver.com') as response: # response = urlopen...
    soup = BeautifulSoup(response, 'html.parser')
    for idx1, keyword_rank in enumerate(soup.select('.keyword_rank')):
        print(idx1, keyword_rank.find('.title_cell'))
        for idx2, num_text in enumerate(keyword_rank.select('li')):
            # print(num_text)
            print(idx2 + 1, num_text.span.get_text(), num_text.a.get('href'))
        # for link in keyword_rank.find_all('a'):
        #     print(link)