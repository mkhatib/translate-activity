#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
import sys
from gd import detect_lang

MAX_TEXT_LENGTH = 680

def translate(text, to='en'):
	to_langs = to.split(' ')
	paragraphs = text.split('\n')
	lang1 = detect_lang(paragraphs[0][:MAX_TEXT_LENGTH])
	results = {}
	for lang in to_langs:
		langpair = '%s|%s'%(lang1,lang)
		base_url = 'http://ajax.googleapis.com/ajax/services/language/translate?'
		translation = ''
		index = 0
		for p in paragraphs:
			cut = False
			index += 1
			if isBlank(p): continue
			if len(p) > MAX_TEXT_LENGTH: 
				paragraphs.insert(index, p[680:])
				p = p[:680]
				cut = True
			params = urlencode((('v',1.0), ('q',p),('langpair',langpair)))
			url = base_url + params
			content = urlopen(url).read()
			start_idx = content.find('"translatedText":"')+18
			_translation = content[start_idx:]
			end_idx = _translation.find('"}, "')
			if cut: newline = ''
			else: newline = '\n'
			translation += _translation[:end_idx] + newline
			
		results[lang] = translation
	#if len(results) == 1: return results[lang[0]]
	
	return results

def isBlank(str):
	return len(str.strip()) == 0
	
def main():
	print translate('Hello World', 'ar es ja')

if __name__ == '__main__':
	main()