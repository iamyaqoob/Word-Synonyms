import urllib2
import json


API_KEY =  'YOUR API KEY'
url = 'http://words.bighugelabs.com/{YOUR API KEY}/'
#---------------------------------------------------------------------------

#----------------------------------------------------------------------------
target = open('out_p.txt', 'w')
target.write("-+-+-+-+-+-+-+-+-+- WORD POWER -+-+-+-+-+-+-+-+-+-\n\n\n")

final_url = ''
word = ''
word_list = []
with open('in_p.txt') as f:
	for line in f:
		
		error = False
		
		print word_list
		final_url = line;
		length_of_final_url = len(final_url)
		word = final_url[68 : length_of_final_url-6]
		print '===> ' + word,
		target.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
		target.write(word+"\n")
		target.write('[')
		
		try:
			json_obj = urllib2.urlopen(final_url)
			data = json.load(json_obj)
		except urllib2.HTTPError:
			error = True
			print('Oops! Error when trying to fetch {}'.format(final_url))
			
		if error:
			target.write('NOT FOUND!')
		
		else:
			'''
			for key,value in data.items():
				target.write('Type: {}'.format(key))
				for prop, values in value.items():
					target.write('{}: {}'.format(prop, ', '.join(values)))
			'''	
			if 'noun' in data:
				for item in data['noun']['syn']:
					target.write(item + ", ")
					#word_list.append(item)
			
			if 'verb' in data:
				for item in data['verb']['syn']:
					target.write(item + ", ")
					#word_list.append(item)
				
			if 'adjective' in data:
				data_adj = data['adjective']
				if data_adj['sim']:
					#print '^^^^^^'
					for item in data_adj['sim']:
						target.write(item + ", ")
					
				elif data_adj['syn']:
					for item in data_adj['syn']:
						target.write(item + ", ")
						#word_list.append(item)
			
			'''	
			if word_list:
				for words in word_list:
					print words,
					target.write(words + ", ")
			del word_list[:]
			'''
		target.write("]\n\n")
