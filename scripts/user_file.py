from os.path import *

def get_data_for(username):
	if username == None:
		return None,None
	filepath = join(dirname(dirname(__file__)),'data/' + username + '.txt')
	if isfile(filepath) == False:
		return None,None
	f = open(filepath,'r')
	favorite_tags = []
	w = dict()
	for line in iter(f):
		id,val = map(str,line.split('\t'))
		if id == 'watched':
			pairs = map(str,val.split())
			for pair in pairs:
				id,v = pair.split(',')
				if id == 'None' or v == 'None':
					continue
				else:
					id = int(id)
					if v == '0':
						w[id] = False
					else:
						w[id] = True
			break
		else:
			val = int(val)
			id = int(id)
			favorite_tags.append([val,id])
	f.close()
	return favorite_tags,w

def update_data_with(username,userdata,watched):
	f = open(join(dirname(dirname(__file__)),'data/' + username + '.txt'),'w')
	userdata.sort()
	userdata.reverse()
	for tag in userdata:
		f.write(str(tag[1]) + '\t' + str(tag[0]) + '\n')
	f.write('watched\t')
	for id in watched:
		f.write(str(id) + ',' + str(int(watched[id])) + ' ')
	f.close()

def is_new(username):
	if username == None:
		return False
	filepath = join(dirname(dirname(__file__)),'data/' + username + '.txt')
	return (not isfile(filepath))