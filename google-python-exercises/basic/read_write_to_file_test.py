#!/usr/bin/python
# Testting the open file functions of python

f = open('small.txt', 'rU')
word_dict = {}
for line in f:
	words = line.split()
	for word in words:
		word = word.lower()
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]

items = sorted(word_dict.items(), key=get_count, reverse=True)
print items
for item in items[:20]:
	print item[0], item[1]

f.close()
