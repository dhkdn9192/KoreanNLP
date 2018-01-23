
"""
한국어 위키백과 텍스트 데이터를 이용한 word2vec 학습 - (1)
    - 위키 텍스트를 읽고 형태소 분석된 wakati 파일 만들기
"""
from konlpy.tag import Twitter


# 형태소 분석된 라인을 wakati 파일에 append하는 함수
def append_to_file(input, file):
    with open(file, 'a', encoding='utf-8') as writeFp:
        writeFp.write(input + " ")


wakati_file = "wiki.wakati"     # wakati 파일 이름
line_cnt = 0                    # 위키 텍스트 라인 인덱스 변수
twitter = Twitter()             # 형태소 분석기 인스턴스

# with open(wakati_file, 'a', encoding='utf-8') as writeFp:
# 파일 열기
with open('../data/wiki.txt', 'r', encoding='utf-8') as readFp:
    for line in readFp:
        if not line:
            print("\n>> [INFO] not line, break : line_cnt=%.f" % line_cnt)
            break

        if line_cnt % 1000 == 0:
            print("current - " + str(line_cnt))

        # 라인 단위 형태소 분석
        malist = twitter.pos(line, norm=True, stem=True)

        # 필요한 어구만 대상으로 하기
        for word in malist:
            if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                append_to_file(word[0], wakati_file)
                # writeFp.write(word[0] + " ")
        line_cnt += 1

