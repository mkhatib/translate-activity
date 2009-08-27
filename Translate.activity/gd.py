#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
import sys

def detect_lang(text):
  base_url="http://www.google.com/uds/GlangDetect?callback=google.language.callbacks.id100&"
  params=urlencode( (('v',2.0),('q',text)))
  url=base_url+params
  content=urlopen(url).read()
  start_idx=content.find('"language":"')+12
  language=content[start_idx:]
  end_idx=language.find('","')
  language=language[:end_idx]
  return language  

if __name__ == "__main__":
  if sys.argv[1] == '--file':
    text=open(sys.argv[2]).read()
  else: text = ' '.join(sys.argv[1:])  
  print detect_lang(text)
