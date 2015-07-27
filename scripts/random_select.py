from random import randint
def get_random_movie(watched,popular_movies,movies_with_tag = None):
	if movies_with_tag != None:
		movies = movies_with_tag
		l = len(movies)
		new_movie = False
		while l > 0 and new_movie == False:
			l = len(movies)
			r = randint(0,min(l - 1,10))
			new_movie = not watched[movies[r]]
			if new_movie == True:
				watched[movies[r]] = True
				return movies[r],watched
			del movies[r]
	rand_max = 101
	new_movie = False
	movies = [id for (id,name) in popular_movies]
	l = len(movies)
	while l > 0 and new_movie == False:
		l = len(movies)
		r = randint(0,min(l - 1,rand_max))
		new_movie = not watched[movies[r]]
		if new_movie == True:
			watched[movies[r]] = True
			return movies[r],watched
		del movies[r]
	return None,watched

def robot_check():
	a = randint(0,9)
	b = randint(0,9)
	return str(a),str(b),str(a*b)
