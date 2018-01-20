
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter


# UTF-16 인코딩으로 파일을 열고 글자를 출력하기
fp = codecs.open("data/2BEXXX06.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text > body")
text = body.getText()


# 텍스트를 한 줄씩 처리하기
twitter = Twitter()
word_dic = {}
lines = text.split("\n")


for line in lines:
    malist = twitter.pos(line)

    for word in malist:
        if word[1] == "Noun":
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0       # 처음 보는 단어면 키-밸류쌍에 추가
            word_dic[word[0]] += 1


keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)

for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()
