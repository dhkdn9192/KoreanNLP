
from konlpy.tag import Twitter

twitter = Twitter()
malist = twitter.pos("아버지가방에들어가신다", norm=True, stem=True)
print(malist)