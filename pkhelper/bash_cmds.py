from asyncio.subprocess import PIPE as asyncPIPE
from asyncio import create_subprocess_shell as asyncrunapp
import subprocess


async def bash_async(cmd):
  fetch = await asyncrunapp(
            cmd,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
          )
  stdout, stderr = await fetch.communicate()
  result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
  return result

def bash(cmd):
 cmd=cmd.split()
 #r = subprocess.run(['mediainfo', '--output=HTML', file], stdout=subprocess.PIPE).stdout.decode('utf-8')
 r = subprocess.run(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 stdout,stderr= r.stdout,r.stderr
 resu=str(stdout.decode().strip()) + str(stderr.decode().strip())
 return resu
