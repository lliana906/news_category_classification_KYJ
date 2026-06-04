from bs4 import BeautifulSoup #html느낌으로 바꿔준다.
import requests
import re
import pandas as pd
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']
df_titles = pd.DataFrame()

#뉴스 제목 따오기 위한 작업
for i in range(6):
    url = 'https://news.naver.com/section/10{}'.format(i)

    resp = requests.get(url)
    # print(list(resp))

    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)
    title_tag = soup.select('.sa_text_strong')
    print(title_tag)
    titles = []
    for title in title_tag:
        titles.append(title.text)

    print(titles) #텍스트만 빼 온다.

    df_section_titles = pd.DataFrame(titles)
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([ df_titles,df_section_titles], ignore_index=True)
print(df_titles.head())
df_titles.info()
df_titles.to_csv('./data/naver_headline_news_{}.csv'.format(
            datetime.datetime.now().strftime('%Y%m%d')), index=False)
