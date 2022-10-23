from aiohttp import FormData
import aiohttp,asyncio,requests,json

timeout = aiohttp.ClientTimeout(total=1600)
async def gofi_uploader(file):
  ser=requests.get("https://api.gofile.io/getServer")
  server=ser.json()["data"]["server"]
  host=f"https://{server}.gofile.io/uploadFile"
  async with aiohttp.ClientSession(timeout=timeout) as session:
   
    data = FormData()
    data.add_field('file', open(file, 'rb'))
    async with session.post(host,data=data) as resp:
      res=await resp.json()
      return res,res["data"]["downloadPage"]
