from scripts.movies import *
from scripts.tags import *
from scripts.random_select import *
from scripts.user_file import *
from scripts.algorithm import *
from scripts.easygui import *
from scripts.help import *
global popular_movies,mov_dict,tag_dict,tags_of_mov,movies_with_tag,watched,none

popular_movies = movie_order_by_popularity()
popular_tags = tag_order_by_popularity()
mov_dict = movie_dictionary()
tag_dict = tag_dictionary()
tags_of_mov = get_tags_for_each_movie()
movies_with_tag = movies_for_each_tag(mov_dict)

watched = dict()
for [id,name] in popular_movies:
	watched[id] = False
global username,user_data
username = user_data = None
def printtags(id):
	tags = [tag_dict[t][0] for t in tags_of_mov[id]]
	res = '\n['
	for tag in tags[:min(len(tags),3)]:
		res += tag
		if tags.index(tag) != 2:
			res += ','
	return (res + ']')
def check(res,password):
	if password != res:
		msgbox('Robot test failed!','You might be a robot?!','Quit')
		exit(0)
def check_for_empty(username):
	if username == '':
		msgbox('Uh..the username tab was empty','Invalid Login - MovieNext','Quit')
		exit(0)
while 1:
	a,b,res = robot_check()
	choice = buttonbox('','MovieNext - Login',["New User","Help","Old User"])
	if choice == None:
		exit(0)
	if choice == "New User":
		username,password = multenterbox('','MovieNext - Login',["Username:","What's " + a + 'x' + b + '?'])
		check_for_empty(username)
		if is_new(username) == False:
			msgbox('Username exists already','Invalid Login - MovieNext','Quit')
			exit(0)
		check(res,password)
	elif choice == "Old User":
		username,password = multenterbox('','MovieNext - Login',["Username:","What's " + a + 'x' + b + '?'])
		check(res,password)
		user_data,watched = get_data_for(username)
		if user_data == None:
			msgbox('Username not found','Invalid Login - MovieNext','Quit')
			exit(0)
	else:
		help()
	while True:
		if user_data == None:
			user_data = []
			id = None
			tag = enterbox("Enter a genre(1100 kinds available)\nOr leave it blank if you have no specific genre in mind","MovieNext - Recommend",'').lower()
			if tag == '':
				id,watched = get_random_movie(watched,popular_movies)
			else:
				while tag != '' and (tag not in tag_dict or empty(movies_with_tag[tag_dict[tag][0]],watched)):
					tag = boolbox('Genre absent','MovieNext - Retry',['Enter a new genre','I dont have any specific genre in mind'])
					if tag == True:
						tag = enterbox("","MovieNext - Recommend",'').lower()
					else:
						tag = ''
				if tag == '':
					id,watched = get_random_movie(watched,popular_movies)
				else:
					tag = tag_dict[tag][0]
					id,watched = get_random_movie(watched,None,movies_with_tag[tag])
			like = boolbox(mov_dict[id][0] + '\n' + printtags(id),'How about this?',['I liked it','It was bleh.'])
			user_data = learn(user_data,like,tags_of_mov[id])
		else:
			id = None
			tag = enterbox("Enter a genre(1100 kinds available)\nOr leave it blank if you have no specific genre in mind","MovieNext - Recommend",'')
			if tag == '':
				id,w = recommend_movie(user_data,watched,popular_movies,tags_of_mov)
				if id == None:
					id,watched = get_random_movie(watched,popular_movies)
				else:
					watched = w
			else:
				while tag != '' and (tag not in tag_dict or empty(movies_with_tag[tag_dict[tag][0]],watched)):
					tag = boolbox('Genre absent','MovieNext - Retry',['Enter a new genre','I dont have any specific genre in mind'])
					if tag == True:
						tag = enterbox("","MovieNext - Recommend",'').lower()
					else:
						tag = ''
				if tag == '':
					id,w = recommend_movie(user_data,watched,popular_movies,tags_of_mov)
					if id == None:
						id,w = get_random_movie(watched,popular_movies)
					else:
						watched = w
				else:
					tag = tag_dict[tag][0]
					id,w = recommend_movie(user_data,watched,None,tags_of_mov,movies_with_tag[tag])
					if id == None:
						id,watched = get_random_movie(watched,None,movies_with_tag[tag])
					else:
						watched = w
			like = boolbox(mov_dict[id][0] + '\n' + printtags(id),'How about this?',['I liked it','It was bleh.'])
			user_data = learn(user_data,like,tags_of_mov[id])
		update_data_with(username,user_data,watched)
		repeat = boolbox('Continue?','MovieNext - Continue',["Gimme another movie","Quit"])
		if repeat == False:
			exit(0)
