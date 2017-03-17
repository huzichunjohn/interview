#/usr/bin/env python
# -*- coding: utf-8 -*-

words_freq = {}

with open("word.txt") as f:
    data = f.read()
    words = data.split()
    for word in words:
        if word not in words_freq:
            words_freq[word] = 1
        else:
            words_freq[word] += 1

# words_freq_list = [(words_freq[word], word) for word in words_freq]
# words_freq_list.sort(reverse=True)
#
# for word_freq in words_freq_list:
#     print "%-15s %d" % (word_freq[1], word_freq[0])

# words_freq_sorted_keys = sorted(words_freq, key=words_freq.get, reverse=True)
# for key in words_freq_sorted_keys:
#     print key, words_freq[key]

# words_freq_list = sorted(words_freq.iteritems(), key=lambda (k, v): (v, k), reverse=True)
words_freq_list = sorted(words_freq.iteritems(), key=lambda kv: kv[1], reverse=True)
print words_freq_list

from collections import Counter

word_counter = Counter()
with open("word.txt", 'r') as f:
    data = f.read()
    words = data.split()
    # print Counter(words).most_common()
    word_counter.update(words)

for word, count in word_counter.most_common():
    print word, count

with open("word.txt") as f:
    for line in f:
        print line.strip()

with open("word.txt") as f:
    line = f.readline()
    while line:
        print line.strip()
        line = f.readline()
