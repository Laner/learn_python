#!/usr/bin/python -tt
# import re 
# teststring = '<h3 align="center">Popularity in 1990</h3><p align="center"><table width="48%" border="1" bordercolor="#aaabbb" cellpadding="2" cellspacing="0" summary="Popularity for top 1000"><tr align="center" valign="bottom">  <th scope="col" width="12%" bgcolor="#efefef">Rank</th>  <th scope="col" width="41%" bgcolor="#99ccff">Male name</th><th scope="col" bgcolor="pink" width="41%">Female name</th></tr><tr align="right"><td>1</td><td>Michael</td><td>Jessica</td><tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td><tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td><tr align="right"><td>4</td><td>Joshua</td><td>Amanda</td><tr align="right"><td>5</td><td>Daniel</td><td>Samantha</td><tr align="right"><td>6</td><td>David</td><td>Sarah</td><tr align="right"><td>7</td><td>Andrew</td><td>Stephanie</td>'
# babynames = re.findall('(?<=<td>).+?(?=</td>)', teststring)
# print babynames
# print babynames[0::3]
# print babynames[1::3]
# print babynames[2::3]
# alt = ()
# alt = zip(babynames[0::3], babynames[1::3], babynames[2::3])
# print "------", alt
# print alt[4][1]


# Begin solution
import re
def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]

def extract_names(filename):
	inputfile = open(filename, 'rU')
	fullhtml = inputfile.read()
	babynames = re.findall('(?<=<td>).+?(?=</td>)', fullhtml)
	year = re.findall('(?<=Popularity in )\d\d\d\d',fullhtml)
	boyNamesWithRank = dict(zip(babynames[1::3], babynames[0::3]))
	girlNamesWithRank = dict(zip(babynames[2::3], babynames[0::3]))
	allNamesWithRank = {}
	allNamesWithRank.update(boyNamesWithRank)
	allNamesWithRank.update(girlNamesWithRank)
	namesWithRankList = [''.join(year)]
	for name, rank in sorted(allNamesWithRank.items(), key=get_count):
		nameRank = name + ' ' + rank
		namesWithRankList.append(nameRank)
	text = '\n'.join(namesWithRankList) + '\n'
	f = open('foo.txt', 'w')
	f.write(text)
	f.close()
	print type(text)
	# print namesWithRankList
extract_names('baby1990.html')