
"""
한국어 위키백과 텍스트 데이터를 이용한 word2vec 학습 - (1)
    - 위키 텍스트를 읽고 형태소 분석된 wakati 파일 만들기
"""
import codecs
# from bs4 import BeautifulSoup
from konlpy.tag import Twitter
# from gensim.models import word2vec


# 파일 열기
readFp = codecs.open('../data/wiki.txt', 'r', encoding='utf-8')
wakati_file = "wiki.wakati"
writeFp = open(wakati_file, 'w', encoding='utf-8')

# 형태소 분석
twitter = Twitter()

i = 0
while True:
    line = readFp.readline()
    if not line:
        break

    if i % 20000 == 0:
        print("current - " + str(i))

    # 라인 단위 형태소 분석
    malist = twitter.pos(line, norm=True, stem=True)

    # 필요한 어구만 대상으로 하기
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            writeFp.write(word[0] + " ")
    i += 1

writeFp.close()

