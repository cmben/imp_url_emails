#!/usr/bin/python
import os


def loadAndExtractMessage(filename):
	email = open(filename, "r")
	message = email.readlines()
	first_blank_index = message.index('\n')
	message = message[(first_blank_index+1): ]
	return ''.join(message)

def getEmailsFromDir(path):
	filelist = os.listdir(path)
	filelist = filter(lambda x: x != 'cmds', filelist)
	all_messages = [loadAndExtractMessage(os.path.join(path, f)) for f in filelist]
	return all_messages

if __name__ == '__main__':
	path = "../easy_ham/"
	all_messages = []
	if os.path.exists(path):
		all_messages = getEmailsFromDir(path)
