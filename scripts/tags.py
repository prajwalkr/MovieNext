from os.path import *
def tag_dictionary():
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\\taglist.txt')
	f = open(filepath,'r')
	tags = dict()
	for line in iter(f):
		id,name,val = map(str,line.split('\t'))
		id = int(id)
		val = int(val)
		tags[id] = (name,val)
		tags[name] = (id,val)
	f.close()
	return tags

def tag_order_by_popularity():
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\ordered_tags.txt')
	f = open(filepath,'r')
	tags = []
	for line in iter(f):
		id,name,val = map(str,line.split('\t'))
		id = int(id)
		tags.append([id,name])
	return tags

def get_tags_for_each_movie():
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\movies_tagged.txt')
	f = open(filepath,'r')
	movies = dict()
	for line in iter(f):
		if '\t' in line:
			id,tags = map(str,line.split('\t'))
			id = int(id)
			tags = map(int,tags.split())
			movies[id] = tags
	return movies

def movies_for_each_tag(movies):
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\movies_tagged.txt')
	f = open(filepath,'r')
	Tags = [[] for i in range(1128)]
	for line in iter(f):
		if '\t' in line:
			mov,tags = map(str,line.split('\t'))
			mov = int(mov)
			tags = map(int,tags.split())
			for tag in tags:
				Tags[tag].append(mov)
	f.close()
	for i in range(1128):
		pairs = [(movies[t][1],t) for t in Tags[i]]
		pairs.sort()
		pairs.reverse()
		Tags[i] = [x for (y,x) in pairs]
	return Tags
