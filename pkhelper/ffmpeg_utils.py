import os,json,subprocess,asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
def remove_streams(file,stream_choosen,out):
  stre=str(stream_choosen).split("@")
  stream=stre[0]
  s_=stre[-1]
  f=str(file).split(".")
  #name=f[0]
  #ext=f[-1]
  #out=f"""{name}re.{ext}"""
  if stream=='audio':
    os.system(f"""ffmpeg -i "{file}" -c copy -map 0 -map -0:a:{s_} -loglevel 0 "{out}" """)
  elif stream=='subtitle':
    os.system(f"""ffmpeg -i "{file}" -c copy -map 0 -map -0:s:{s_} -loglevel 0 "{out}" """)
  else:
    pass
  return out

def extract_streams(file,stream_choosen,out):
  stre=str(stream_choosen).split("@")
  stream=stre[0]
  s_=stre[-1]
  f=str(file).split(".")
  out1a=str(file).replace(f"{f[-1]}","mka")
  out1s=str(file).replace(f"{f[-1]}","srt")
  if stream=='audio':
    os.system(f"""ffmpeg -i "{file}" -c copy -map 0:a:{s_} -loglevel 0 "{out1a}" """)
    return out1a
  elif stream=='subtitle':
    os.system(f"""ffmpeg -i "{file}" -map 0:s:{s_} -loglevel 0 "{out1s}" """)
    return out1s
  else:
    pass
    return

def durationfunc(file):
 metadata = extractMetadata(createParser(f"""{file}"""))
 if metadata.has("duration"):
   duration = metadata.get('duration').seconds
 else:
     duration = 5
 return duration

st=[]
def list_streams(file):
  ffprobe_cmd = f"""ffprobe -hide_banner -show_entries stream=codec_type -show_entries stream_tags=language -print_format json -loglevel 0 -i {file} """
  cmd=ffprobe_cmd.split()
  r = subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode()
  #print(r)
  output = json.loads(r)
  for su in output["streams"]:
    #for k,v #in su.items():
    try:
      for i in range(1):
        st.append(su["codec_type"]+"@"+su["tags"]["language"]) 
    except KeyError:
      for i in range(1):
         st.append(su["codec_type"])
  v=[]
  a=[]
  s=[]
  for el in range(len(st)):
   if st[el].startswith('video'):
    v.append(st[el])
   elif st[el].startswith('audio'):
    a.append(st[el])
   elif st[el].startswith('subtitle'):
    s.append(st[el])
   else:
    pass
  v1=[]
  a1=[]  
  s1=[]
  for uy in range(len(v)):
    v1.append(f"{v[uy]}@{uy}")
  
  for uy in range(len(a)):
    a1.append(f"{a[uy]}@{uy}")
    
  for uy in range(len(s)):
    s1.append(f"{s[uy]}@{uy}")
  streams=a1+s1
  st.clear()
  return streams

def generate_sample(file):
  dur=durationfunc(file)
  ext=str(file).split(".")[-1]
  out=f"""{str(file).replace(ext,"")+'sample.'}{ext}"""
  if int(dur)<180:
     os.system(f"""ffmpeg -y -i "{file}" -ss 00:00:00 -t 30 -c copy -map 0 -loglevel 0 "{out}" """)
  else:
    os.system(f"""ffmpeg -y -i "{file}" -ss 00:00:00 -t 50 -c copy -map 0 -loglevel 0 "{out}" """)
  return out


