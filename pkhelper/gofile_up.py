from aiohttp import FormData
import aiohttp,asyncio

timeout = aiohttp.ClientTimeout(total=1600)
async def uploader(file,host):
  async with aiohttp.ClientSession(timeout=timeout) as session:
   
    data = FormData()
    data.add_field('file', open(file, 'rb'))
    async with session.post(host,data=data) as resp:
      res=await resp.json()
      return res,res["data"]["downloadPage"]
