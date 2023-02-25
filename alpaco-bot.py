from telegram.ext import Updater, CommandHandler

import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm

import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import time

import pandas as pd


def help(update, context):
    # 설명
    update.message.reply_text("안녕하세요, 뉴스요약봇입니다. /keyword [뉴스를 요약받고자 하는 키워드] 로 사용가능합니다.")
  
def crawling(keyword):

    binary = 'chromedriver.exe'
    browser = webdriver.Chrome(binary)
    browser.get("https://www.yna.co.kr/search/index?query={0}&ctype=A&scope=title".format(keyword))

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")

    a_tags = soup.select("div.cts_atclst a")
    titles, texts = [], []
    for a_tag in a_tags:
        href = a_tag['href']

        browser.get('https:' + href)

        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        title = soup.select('h1.tit')[0].text
        text = soup.select('article.story-news.article')[0].text.replace('\n', ' ').replace('ADVERTISEMENT', '')
        
        titles.append(title)
        texts.append(text)
        print(title)
        print('------------------------')

    browser.quit()

    return titles, texts

def keyword(update, context):
    keyword = context.args[0]

    return_result = """
* 인공지능 챗봇으로 숙제하는 美 학생들…교육현장선 차단 고심
미국의 교사들이 최근 출시된 인공지능(AI) 챗봇 '챗GPT'(ChatGPT)를 악용해 부정행위를 저지르는 학생들 때문에 큰 고민이라고 워싱턴포스트(WP)가 28일(현지시간) 보도했다. 표절 감지 프로그램을 판매하는 업체들은 AI가 작성한 글을 포착할 수 있는 프로그램 개발에 착수했다.

* 태안군 인공지능융합산업진흥원 '노인 가정환경 개선' 호응
충남 태안군 인공지능융합산업진흥원이 노인 가정을 대상으로 벌이고 있는 \'리홈(Re-Home) 가정환경 개선 사업\'이 좋은 반응을 얻고 있다. 진흥원은 작업치료사 2명과 소프트웨어 기술자 1명을 배치해 지난 10월부터 노인 가정 20곳에 시범 서비스를 했다. 진흥원 관계자는 "어르신들의 건강하고 독립적인 일상생활을 위해 가정환경개선 사업을 비롯해 가상현실(VR)·인공지능(AI)에 기반한 건강관리 등 다양한 서비스를 확대할 예정"이라고 밝혔다.

* 특허청 올해 10대 뉴스 1위는 '인공지능은 발명자 될 수 없다'
인공지능(AI)이 발명했다는 특허에 대해 특허청이 무효처분한 뉴스가 올해 특허청 10대 뉴스 1위로 선정됐다. 28일 특허청에 따르면 올해 10대 뉴스는 언론에 많이 보도된 뉴스 가운데 국민과 언론인 투표를 통해 선정했다. 이대원 특허청 대변인은 "내년에도 국민이 더욱 공감할 수 있도록 다양한 방식으로 소통하는 특허청이 되겠다"고 말했다.

* [동정] 이주호 부총리, 인공지능 교육 선도학교 방문
이 부총리는 "앞으로 인공지능을 학교 수업에 활용해 학생 맞춤형 학습을 돕고, 교사는 학생의 창의적·비판적 사고를 키우는 조력자로서 교육 혁신을 이룰 수 있도록 하겠다"고 전했다.

* 광주 인공지능 영재고 설립 '첫발'…정부 예산에 기획비 반영
26일 광주시에 따르면 최근 국회에서 확정한 내년도 정부 예산에 '광주 과학기술원(GIST) 부설 인공지능 영재고 설립' 기획 용역비 10억원이 반영됐다. 이 사업비는 국회 예산 심사 막바지까지 반영 여부가 불투명했지만, 막판에 극적으로 포함됐다고 광주시는 전했다.

* [게시판] 서울대, 네이버TV서 인공지능 무료 강의
AI연구원 소속 27명이 인공지능의 원리와 딥러닝 등 AI 핵심 개념과 자율주행, 금융, 패션 등 다양한 분야 AI 활용에 관해 강의한다. 강연은 네이버TV '서울대의 모두를 위한 AI 강의' 채널에서 매주 화요일과 목요일 공개된다.

* KT ""내년 인공지능 인프라·솔루션·서비스 모아 해외 진출""
KT[030200]는 내년 인공지능(AI) 인프라와 솔루션, 서비스를 모아 '한국형 AI 풀스택'을 구축한다고 22일 밝혔다. KT는 전날 서울 종로구 KT 이스트빌딩에서 열린 'AI 반도체 사업협력위원회 워크숍'에서 이런 계획을 공개했다.

* 구글, 인공지능 챗봇 '챗GPT' 등장에 '비상'
세계 최대 검색엔진 업체 구글이 인공지능(AI) 대화형 메신저 '챗GPT'(ChatGPT) 등장에 비상이 걸렸다. 구글은 최근 오픈AI가 개발한 챗GPT에 대해 심각한 위기 경고를 뜻하는 '코드 레드'(code red)를 발령했다고 뉴욕타임스(NYT)가 21일(현지시간) 보도했다.

* 미래에셋증권, '인공지능' 투자정보 제공 서비스 선보여
미래에셋증권[006800]은 지난 9일 자사 모바일트레이딩시스템(MTS)과 홈페이지를 통해 국내 주식 인공지능 리포트 서비스인 '시장 읽어주는 인공지능(AI)'과 '종목 읽어주는 AI'를 선보였다고 20일 밝혔다. 인공지능 리포트는 데이터와 인공지능을 투자정보 제공에 접목해 리서치 보고서를 출판하는 데 드는 시간을 줄여 고객이 빠르게 폭넓은 종목과 시황 정보를 접할 기회를 줄 것이라고 회사 측은 설명했다.

* [공연소식] 공연장서 벌어지는 인간과 인공지능의 갈등…연극 '가상피리'
한국문화예술위원회의 예술가 지원 사업인 '차세대열전 2022'의 연극 부문 예술가로 선정된 윤혜주 작가의 작품이다. 2040년을 배경으로 모차르트 오페라 '마술피리'를 무대에 올리려고 하는 인간 연출가 민호와 인공지능 조연출 미나의 갈등을 통해 예술의 의미에 대한 질문을 던진다.
    """


    update.message.reply_text(return_result) 
    
'''
if __name__ == "__main__":
    titles, texts = crawling('인공지능')  
    # save to text
    df = pd.DataFrame(list(zip(titles, texts)),columns =['original', 'summary'])
    df.to_csv('ai_titles.csv')
    # model.generate
'''

kairos_token = "5831761815:AAHoo_ZZ5TSg-3O7wvh-b3lw61NWmfLvm2s"
updater = Updater(kairos_token)
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('keyword', keyword, pass_args=True))

updater.start_polling()
updater.idle()


