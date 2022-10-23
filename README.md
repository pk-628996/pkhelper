# Pkhelper
Just something to get my work done<br><br><br>

## Installation
```
pip install pkhelper
```
#### Can download direct link from Command Line.
  <br>**Usage:**<br>
```bash
$ pkhelper --ddl your direct link
```

#### Can download gdrive files from command line.
<br>**Usage:**<br>
```bash 
$ pkhelper --gdrive your link
```
<br><br>

You can also use it in script.<br>
```python
from pkhelper import gdrivedownload
file=gdrivedownload(url)
```

As Simple as this<br>
```python
from pkhelper import direct_dl
file=direct_dl(url)
```
As  simple as this.
```python
from pkhelper import direct_dl_async as ddl_a
file=ddl_a(url)
```
As Simple as this.
<br>
You can run bash commands in python and get output
```python
from pkhelper import bash
output=bash("ffmpeg")
```
As simple as this 
If you want async bash command then
```python
from pkhelper import bash_async
output=await bash_async("ffmpeg")
```
You can generate direct download links of all branches of a public github repo
```python
from pkhelper import repo_ddl_link_gen
ddl_list=repo_ddl_link_gen("repository link")
```
To upload to gofile
```python
from pkhelper import *
json_text,download_page=await gofi_uploader(file)
print(download_page)
```

