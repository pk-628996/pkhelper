import gdown,asyncio
from pytube import YouTube
def link2id(url):
 if "view?usp=" in url:
   re=url.split("file/d/")[-1].split("/view")[-2]
   return re
 elif "&export=" in url:
   re=url.split("uc?id=")[-1].split("&exp")[-2]
   return re
 elif "uc?id=" in url:
   u=url.split("uc?id=")[-1]
   return u
 else:
   return url
"""
from pkhelper import gdrivedownload
   file=gdrivedownload(url)
"""

def gdrivedownload(url):
   tr=link2id(url)
   name=gdown.download(id=tr)
   return f"""{name}"""
