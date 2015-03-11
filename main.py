#coding:UTF-8
_author_ = 'Derek.S'
import string
import codecs
import re
import os
import urllib
import requests
import ssl
import urllib3
urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()
verify='/etc/ssl/certs/ca-certificates.crt'
#url string
f = open('/home/Derek.S/py/1.html')
restr = r'[a-z]+:+\\+\/+\\+\/\w*.\w*.\w*.\/\d\\\/\d*\\\/\d*\w{12}[o].[jpg]*'
url = f.read()
strlist = re.findall(restr,url)
f.close
f = open(r'temp.txt','a')
for i in range(0,len(strlist)):
    f.write(strlist[i]+"\n")
f.close
rows = str( len(strlist) )
url = open('url.txt','a')
f = open('temp.txt','r')
urlstr = f.readlines()
urlrestr = r'\/'
for x in range(0,len(urlstr)):
	urlist = re.sub(urlrestr,"",urlstr[x])
	down = urlist.replace("\\","/")
	local_file = down.split('/')[-1]
	filename = local_file.split('.')[0]
	local_dir = '/home/Derek.S/Flickr/'
	down_dir = str(local_dir) + str(filename)+".jpg"
	url.write(down+"\n")
	print ("DownFile: " + down_dir)
	if os.path.exists(down_dir) == True:
		print ("-----Pic already exists-----")
	elif  os.path.exists(down_dir) == False:
	 r = requests.get(down, verify=False)
	 with open(down_dir, "wb") as code:
	  code.write(r.content)
	 print('\nDownload ' +filename+".jpg"+" Done")
f.close
url.close