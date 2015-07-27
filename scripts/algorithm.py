from math import log
def learn(userdata,like,t):
	tags = t
	if like == True:
		like = 1
	else:
		like = -1
	for i in range(len(userdata)):
		if userdata[i][1] in tags:
			userdata[i][0] += (len(tags) - tags.index(userdata[i][1]))*like
			del tags[tags.index(userdata[i][1])]
	for tag in tags:
		userdata.append([like*tags.index(tag),tag])
	userdata.sort()
	userdata.reverse()
	return userdata

def get_closeness(fav,b):
	movtags = b
	favtags = fav
	val = 0
	for i in range(len(favtags)):
		if favtags[i][0] == 0:
			continue
		if favtags[i][1] in movtags:
			val += (favtags[i][0]*(len(movtags) - movtags.index(favtags[i][1])))
	return float(val)

def get_best_movie(userdata,watched,movies,tags_of_mov):
	i = 0
	val = 0.0
	id = None
	while i < len(movies):
		if watched[movies[i]] == True:
			i += 1
			continue
		closeness = get_closeness(userdata,tags_of_mov[movies[i]])
		if i > 1:
			closeness /= log(i)
		if closeness > val:
			val = closeness
			id = movies[i]
		i += 1
	watched[id] = True
	return id,watched

def recommend_movie(userdata,watched,popular_movies,tags_of_mov,movies_with_tag = None):
	if movies_with_tag == None:
		popular_movies_id_only = [id for (id,name) in popular_movies]
		return get_best_movie(userdata,watched,popular_movies_id_only,tags_of_mov)
	return get_best_movie(userdata,watched,movies_with_tag,tags_of_mov)