#!/usr/bin/python3

import asyncio
from asyncio.tasks import FIRST_COMPLETED
import aiohttp

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

async def main(urls):
	async with aiohttp.ClientSession() as session:
		return await asyncio.wait(
			[*[asyncio.create_task(get(url, session)) for url in urls]],
			return_when=asyncio.FIRST_COMPLETED,
			timeout = 5)

for r in asyncio.run(main(providers))[0]:
	print(r.result().rstrip())
	break
