#!/usr/bin/python3

import asyncio
from asyncio.tasks import FIRST_COMPLETED
import aiohttp
import httpx
import time

providers = [
	'https://ident.me',
	'https://ipv4.icanhazip.com',
	'https://checkip.amazonaws.com/'
]

async def get(url, session):
	r = None
	while r is None:
		try:
			async with session.get(url=url) as response:
				r = await response.text()
		except Exception as e:
			pass
	return r

async def main(urls): # returns the tuple of sets of tasks (finished,unfished)
	async with aiohttp.ClientSession() as session:
		return await asyncio.wait([*[asyncio.create_task(get(url, session)) for url in urls]], return_when=asyncio.FIRST_COMPLETED)

#for r in asyncio.get_event_loop().run_until_complete(main(providers))[0]:
for r in asyncio.run(main(providers))[0]:
	print(r.result().rstrip())
	break
