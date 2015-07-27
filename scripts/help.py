from easygui import *
from os.path import *
def help():
	while 1:
		list_of_help = ["About MovieNext","Logging in","How do I make the best use of this app?","Contact the developer"]
		choice = choicebox('Welcome to the Help Assistant!\nWhere do you need help?','MovieNext - Help Assistant',list_of_help)
		if choice == None:
			exit(0)
		if choice == 'About MovieNext' or choice == 'Logging in' or choice == 'Contact the developer':
			display_as_is(choice)
		if choice == list_of_help[2]:
			working()
		exit(0)
def display_as_is(title):
	filepath = join(dirname(dirname(__file__)),'helpdocs/' + title + '.txt')
	f = open(filepath,'r')
	data = f.readlines()
	textbox('',title,data)

def working():
	list_of_help = [
	"The general way",
	"I wonder whether I should enter the genre",
	"I am worried about the data you collect about me",
	"I am surprised that MovieNext asks me whether I like or dislike a movie every time",
	]
	title = choicebox("Let's narrow down.",'MovieNext - Help Assistant',list_of_help)
	filepath = join(dirname(dirname(__file__)),'helpdocs\\' + title + '.txt')
	f = open(filepath,'r')
	data = f.readlines()
	textbox('',title,data)

	
