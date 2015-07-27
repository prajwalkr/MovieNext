from os.path import *
def movie_order_by_popularity():
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\ordered_movies.txt')
	f = open(filepath,'r')
	movies = []
	for line in iter(f):
		id,name = map(str,line.split('\t'))
		movies.append([int(id),name])
	f.close()
	return movies

def movie_dictionary():
	filepath = join(dirname(dirname(__file__)),'movie-tag-files\movies.txt')
	f = open(filepath,'r')
	movies = dict()
	for line in iter(f):
		id,name,val = map(str,line.split('\t'))
		id = int(id)
		val = int(val)
		movies[id] = (name,val)
		movies[name] = (id,val)
	f.close()
	return movies

def empty(movies,watched):
	for id in movies:
		if watched[id] == False:
			return False
	return True




	
