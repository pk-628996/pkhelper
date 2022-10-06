import json,os
from urllib.request import urlopen

def repo_ddl_link_gen(repo_url):
   to_rename="gy"
   if str(repo_url).startswith("https://"):
      pass
   else:
      repo_url=f"""https://{repo_url}"""
   ur=str(repo_url).replace('github.com','api.github.com/repos')
   if ur.endswith("/"):
       brurl=f"""{ur}branches"""
       to_rename=ur.split("/")[-2]
   else:
      brurl=f"""{ur}/branches"""
      to_rename=ur.split("/")[-1]
   f=urlopen(brurl)
   branches=json.loads(f.readline())
   br_list=[]
   for brnch in branches:
     name=brnch['name']
     if str(repo_url).endswith("/"):
        dd=f"""{repo_url}archive/refs/heads/{name}.zip"""
        br_list.append(dd)
     else:
        dd=f"""{repo_url}/archive/refs/heads/{name}.zip"""
        br_list.append(dd)
   return br_list,to_rename
