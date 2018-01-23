
"""
한국어 위키백과 텍스트 데이터를 이용한 word2vec 학습 - (2)
    - wakati 파일을 이용하여 word2vec 모델 학습시키기
"""
from gensim.models import word2vec

wakati_file = 'wiki.wakati'
model_file = 'wiki.model'

data = word2vec.Text8Corpus(wakati_file)

model = word2vec.Word2Vec(data, size=100)
model.save('../model/' + model_file)

print("\n>> [INFO] Making Word2Vec model finished!")

