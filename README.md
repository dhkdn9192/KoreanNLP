Korean NLP with Python
======================
# 1. Korean NLP Project
## 1.1. 프로젝트 개요
- 한국어 텍스트에 대한 자연어 처리 프로젝트이다. 
- 한국어 형태소 분석, Word2Vec 모델 학습, 인공신경망 기반 텍스트 분류, 미니 챗봇 설계 등을 포함한다. 
- 본 프로젝트의 코드는 "파이썬을 이용한 머신러닝, 딥러닝 실전 개발 입문"(쿠지라 히코우즈쿠에 저, 윤인성 옮김, 위키북스)를 참조하였음

## 1.2. 디렉토리 설명
### data
Word2Vec 모델을 학습시키기 위한 학습용 데이터 디렉토리. (한국어 텍스트 및 json 파일)
    
### model
생성된 Word2Vec 모델이 저장되는 디렉토리

### w2v_with_kowiki
한국어 위키 텍스트 데이터로 Word2Vec 모델을 생성하는 코드 디렉토리. 텍스트 데이터는 위키 덤프 URL( https://dumps.wikimedia.org/kowiki/latest )에서 다운로드하였음

    - kowiki_w2v_01-make_wakati.py : 위키 텍스트를 형태소 분석하여 wakati 파일로 만드는 코드
    - kowiki_w2v_02-make_w2v.py : Word2Vec 모델 생성 코드
    - kowiki_w2v_load_model.ipynb : 생성된 Word2Vec 모델을 로드하는 주피터 노트북 코드
    

### w2v_with_news
뉴스 크롤링 데이터(디지털타임스)로 Word2Vec 모델을 생성하는 코드 디렉토리. 뉴스 데이터의 경우, 뉴스 크롤링 코드( https://github.com/dhkdn9192/NewsCrawling )를 이용하여 준비하였음

    - word2vec_make_model-digitaltimes.py : Word2Vec 모델 생성 코드
    - word2vec_load_model-digitaltimes.ipynb : 생성된 Word2Vec 모델을 로드하는 주피터 노트북 코드
    - digitaltimes.wakati : 학습용 데이터를 형태소 분석한 텍스트를 wakati 파일로 저장한 것
    
### w2v_with_novel
소설 텍스트본("토지", 박경리)으로 Word2Vec 모델을 생성하는 코드 디렉토리

    - word2vec_make_model-toji.py : Word2Vec 모델 생성 코드
    - word2vec_load_model-toji.ipynb : 생성된 Word2Vec 모델을 로드하는 주피터 노트북 코드
    - toji.wakati : 학습용 데이터를 형태소 분석한 텍스트를 wakati 파일로 저장한 것

## 1.3. 기능 설명
### Word2Vec 모델 학습 과정
먼저 학습 데이터를 전처리한 후, konlpy의 Twitter 형태소 분석기를 이용하여 형태소 분석을 수행한다. 분석 결과 텍스트는 wakati 파일로 저장되며,
Word2Vec 모델은 이 wakati 파일을 학습하여 생성된다.

    1) 학습 데이터 전처리 : 특수문자, 문장이 아닌 line 제거 등 수행
    2) 한국어 형태소 분석 : konlpy-Twitter 분석기를 이용하여 형태소 분석
    3) wakati 파일로 저장 : 형태소 분석된 텍스트를 line 단위로 wakati 파일에 저장
    4) Word2Vec 모델 학습 : wakati 파일을 입력하여 Word2Vec 모델을 학습, 모델 생성 
    

### (추가 예정)

## 1.4. 개발환경
    파이썬 버전 : Python3.6.3
    필요 패키지 : konlpy, jpype1, gensim
     * 설치 방법(윈도우,리눅스 공통) : pip install {패키지명}
     * jpype1의 경우, 환경에 따라서 수동으로 설치해야 할 수 있음

