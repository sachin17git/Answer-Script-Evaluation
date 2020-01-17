#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:53:48 2019

@author: sachin
"""

from __main__ import *
import logging
from gensim import corpora, similarities
from gensim.models import LsiModel
from nltk.corpus import stopwords
from pattern.en import sentiment

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# id2word = gensim.corpora.Dictionary.load_from_text('wiki_wordids.txt.bz2')

# mm = gensim.corpora.MmCorpus('wiki_tfidf.mm.bz2')

# lsi = gensim.models.lsimodel.LsiModel(corpus=mm, id2word=id2word)

# lsi.save('/home/sachin/Downloads/wiki/LSI_MODEL')

# with open('ans1.txt') as f1:
#   file1 = f1.read()

# Upload MARKING scheme now.
with open("social mark scheme 2.txt") as f1:
    mark_all = f1.read()

# Upload Student Answer now.
with open('social ans sheet2.txt') as f2:
    ans_all = f2.read()

anssheet = ans_all.split('~\n\n')
anssheet = [d for d in anssheet if d]

if len(anssheet) == 0:
    print("student is absent for the test !")
    exit()

markscheme = mark_all.split('~\n\n')
markscheme = [d for d in markscheme if d]

new_list_ans = []
new_list_mar = []

with open('written_ans.txt') as wa:
    fwa = wa.readlines()

written_answers = fwa[0].split(',')

with open('marks_allot.txt') as ma:
    fma = ma.readlines()

marks_allotment = []
mmm = []

for r in fma:
    t = r.strip()
    t = t.split('-')
    marks_allotment.append((t[0], t[1]))
    mmm.append(t[1])

marks_allotment = dict(marks_allotment)
max_marks = 0
for i in mmm:
    j = int(i)
    max_marks = max_marks + j

for j in written_answers:
    for ans in anssheet:
        if ans.startswith(j):
            ans = ans[2:]
            new_list_ans.append(ans)

    for mar in markscheme:
        if mar.startswith(j):
            mar = mar[2:]
            new_list_mar.append(mar)

total_marks = 0


def marking_scheme(file1):
    global documents
    documents = file1.split('.')
    documents = [d.strip() for d in documents]
    documents = [d for d in documents if d]


# with open('MarkingScheme.txt') as f2:
#    file2 = f2.read()

def answer(file2):
    global new_documents
    new_documents = file2.split('.')
    new_documents = [dd.strip() for dd in new_documents]
    new_documents = [dd for dd in new_documents if dd]


# nltk.download('stopwords')


LSI = LsiModel.load('LSI_MODEL')


def pre_process():
    global t1, t2, index, len_doc, len_new_doc, len_temp_doc, len_temp_new_doc, dictionary, new_documents, documents, corpus
    texts = [[word for word in document.lower().split() if word not in set(stopwords.words('english'))] for document in
             documents]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    index = similarities.MatrixSimilarity(LSI[corpus])
    len_new_doc = [x for x in range(len(new_documents))]
    len_doc = [y for y in range(len(documents))]
    t1 = [x for x in range(len(new_documents))]
    t2 = [y for y in range(len(documents))]
    len_temp_new_doc = len_new_doc
    len_temp_doc = len_doc


def process_sim():
    global len_new_doc, sim_array, index, dictionary, new_documents, documents
    for sent in len_new_doc[:]:
        vec_bow = dictionary.doc2bow(new_documents[sent].lower().split())
        vec_lsi = LSI[vec_bow]
        sims = index[vec_lsi]
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        lg = []
        for o, p in sims:
            if p == 0.0:
                lg.append(p)
        if lg == [0.0] * len(documents):
            t1.remove(sent)
            len_new_doc.remove(sent)
        else:
            sim_array.append(sims)


def process_zero():
    global len_doc, indx
    for c in len_doc:
        max_sim = 0
        count = -1
        for m in sim_array:
            count = count + 1
            for e, k in m:
                if e == c:
                    if k > max_sim:
                        max_sim = k
                        indx = len_new_doc[count]
        avg_sim.append((c, indx, max_sim))


def process_one():
    global len_new_doc, len_temp_new_doc, len_temp_doc, len_doc, final_sim
    for n in len_new_doc:
        tem = 0
        added = None
        for a, b, c in avg_sim:
            if b == n:
                if c > tem:
                    tem = c
                    added = (a, b, c)
        if added is not None:
            final_sim.append(added)
    len_temp_new_doc = [w for q, w, e in final_sim]
    len_temp_doc = [r for r, t, y in final_sim]
    len_new_doc = [x for x in t1 if x not in len_temp_new_doc]
    len_doc = [y for y in t2 if y not in len_temp_doc]


def process_sim1():
    global len_doc, sim_array, index, dictionary, new_documents, documents
    sim_array = []
    for sent in len_new_doc[:]:
        vec_bow = dictionary.doc2bow(new_documents[sent].lower().split())
        vec_lsi = LSI[vec_bow]
        sims = index[vec_lsi]
        sims = sorted(enumerate(sims), key=lambda item: -item[1])
        lg = []
        for o, p in sims:
            if p == 0.0:
                lg.append(p)
        if lg == [0.0] * len(documents):
            t1.remove(sent)
            len_new_doc.remove(sent)
        else:
            sim_array.append(sims)


def process_zero1():
    global len_new_doc, indx
    for c in len_doc:
        max_sim = 0
        count = -1
        indx = None
        for m in sim_array:
            count = count + 1
            for e, k in m:
                if e == c:
                    if k > max_sim:
                        max_sim = k
                        indx = len_new_doc[count]
        if indx is not None:
            avg_sim.append((indx, c, max_sim))


def process_two():
    global len_new_doc, len_temp_new_doc, len_temp_doc, len_doc, final_sim, avg_sim
    for n in len_new_doc:
        temp = 0
        added = None
        for a, b, c in avg_sim:
            if a == n:
                if c > temp:
                    temp = c
                    added = (a, b, c)
        if added is not None:
            final_sim.append(added)
    len_temp_new_doc = [q for q, w, e in final_sim]
    len_temp_doc = [t for r, t, y in final_sim]
    len_new_doc = [x for x in t1 if x not in len_temp_new_doc]
    len_doc = [y for y in t2 if y not in len_temp_doc]


"""
temp = new_list_mar[0]
temp1 = new_list_ans[0]
marking_scheme(temp)
answer(temp1)
pre_process()

final_sim = []
sim_array = []
process_sim1()
avg_sim = []
process_zero1()
process_two()

sim_array = []
process_sim()
avg_sim = []
process_zero()
process_one()

sim_array = []
process_sim()
avg_sim = []
process_zero()
process_one()

sim_array = []
process_sim()
avg_sim = []
process_zero()
process_one()

"""
for i in range(len(written_answers)):
    temp = new_list_mar[i]
    temp1 = new_list_ans[i]
    marking_scheme(temp)
    answer(temp1)
    pre_process()
    if len(documents) > len(new_documents):
        final_sim = []
        while len(len_new_doc) > 0:
            sim_array = []
            process_sim()
            avg_sim = []
            process_zero()
            process_one()
        dop = final_sim
        for g, h, l in dop:
            if l > 0.80:
                s1 = sentiment(documents[g])
                s2 = sentiment(new_documents[h])
                diff = abs(s1[0] - s2[0])
                if s1[0] < 0 and s2[0] < 0:
                    pass
                elif s1[0] > 0 and s2[0] > 0:
                    pass
                else:
                    if diff > 0.4:
                        final_sim.remove((g, h, l))

        sum1 = [j for g, h, j in final_sim]
        avg = (sum(sum1)) / len(documents)
        marks = round(((avg * 100) * int(marks_allotment[written_answers[i]])) / 100)
    else:
        final_sim = []
        while len(len_doc) > 0 and len(len_new_doc) > 0:
            sim_array = []
            process_sim1()
            avg_sim = []
            process_zero1()
            process_two()
        dop = final_sim
        for g, h, l in dop:
            if l > 0.80:
                s1 = sentiment(documents[h])
                s2 = sentiment(new_documents[g])
                diff = abs(s1[0] - s2[0])
                if s1[0] < 0 and s2[0] < 0:
                    pass
                elif s1[0] > 0 and s2[0] > 0:
                    pass
                else:
                    if diff > 0.4:
                        final_sim.remove((g, h, l))
        sum1 = [j for g, h, j in final_sim]
        avg = (sum(sum1)) / len(documents)
        marks = round(((avg * 100) * int(marks_allotment[written_answers[i]])) / 100)

    print(" Question", written_answers[i], "=", marks, "/", int(marks_allotment[written_answers[i]]))
    total_marks = total_marks + marks

kk = marks_allotment.keys()
ky = marks_allotment.values()

mar = [int(marks_allotment[d]) for d in kk if d in written_answers]
print("total marks out of", max_marks, "=", total_marks)

ttm = sum(mar)
summarks = total_marks


def get_value():
    s = "marks obtained: " + str(max_marks) + " / " + str(ttm)
    return s


