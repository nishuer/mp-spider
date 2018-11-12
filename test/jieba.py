import jieba.analyse
from gensim import corpora, models, similarities
import difflib


# word_list = [
#     "1875年的甘肃兰州 左宗棠率湖湘子弟镇守边关",
#     "1875年的甘肃兰州 陕甘总督左宗棠率湖湘子弟镇守边关",
# ]

# word_list1 = [
#     "这种被很多中国人丢掉的东西，在美国竟然要卖到几千美元一斤！",
#     "这东西在美国一斤要卖几千美元，在中国，不认识都被丢了",
# ]

word_list2 = [
    "炎亚纶出柜又出轨？发长文道歉：没有处理好自己的私人生活",
    "承认出柜？炎亚纶发长文道歉：很抱歉没有处理好我自己的私人生活",
]

# word_list3 = [
#     "搞笑GIF：虽然早已做好心理准备，可还是被击碎了心理防线",
#     "俘虏守口如瓶，八路军还是攻破了俘虏心理防线，得到信报",
# ]

# print(word_list[0])
# print(word_list[1])
# print("相似度：%s" % difflib.SequenceMatcher(None, word_list[0], word_list[1]).quick_ratio())
# print("")
# print(word_list1[0])
# print(word_list1[1])
# print("相似度：%s" % difflib.SequenceMatcher(None, word_list1[0], word_list1[1]).quick_ratio())
# print("")
print(word_list2[0])
print(word_list2[1])
print("相似度：%s" % difflib.SequenceMatcher(None, word_list2[0], word_list2[1]).quick_ratio())
print("")
# print(word_list3[0])
# print(word_list3[1])
# print("相似度：%s" % difflib.SequenceMatcher(None, word_list3[0], word_list3[1]).quick_ratio())

corpus = []

for i in word_list2:
    corpus.append(jieba.analyse.extract_tags(i))

print(corpus)

dictionary = corpora.Dictionary(corpus)

# print(dictionary)

# print(dictionary.keys())

# print(dictionary.token2id)

doc_vectors = [dictionary.doc2bow(text) for text in corpus]

print(doc_vectors)

tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]

# print(tfidf_vectors)

index = similarities.SparseMatrixSimilarity(tfidf_vectors, num_features=len(dictionary.keys()))

# new_doc = dictionary.doc2bow(jieba.analyse.extract_tags("这东西在美国一斤要卖几千美元，在中国，不认识都被丢了"))

sim = index[tfidf[doc_vectors[0]]]

print(list(enumerate(sim)))