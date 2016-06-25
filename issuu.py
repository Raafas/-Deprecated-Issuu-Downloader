import sys, urllib, wget, httplib
from urllib import FancyURLopener
from random import choice

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
]

class MyOpener(FancyURLopener, object):
    version = choice(user_agents)

base = ""
tag = '<link rel="image_src" href='
pageNum = 1

if len(sys.argv) > 1:
    base = str(sys.argv[1])
    resp = urllib.urlopen(base)
    content = resp.read()

    with open("foo.txt", "w") as f:
        f.write(content)
        f.close()
    with open('foo.txt') as f:
        for i, line in enumerate(f, 1):
            if tag in line:
                break
    line = line.replace('<link rel="image_src" href="', '')
    line = line.replace('1.jpg">', '')

    page_loader = MyOpener()
    while True:
        code = page_loader.retrieve(line.strip()+str(pageNum)+".jpg", str(pageNum)+".jpg")
        pageNum += 1
        if code[1]["Content-Type"] != 'image/jpeg':
            print pageNum
            print code[1]
            break
else:
    print("Usage: python issuu.py http://issuu.com/user/docs/file")
    sys.exit(2)
