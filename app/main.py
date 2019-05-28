from app.crawler.search.handler import get_search_result
from app.crawler.search.context import SearchContext
import asyncio
import aiohttp


# FIXME temporary constants for testing, later should be extracted from job
BATCH_SIZE = 250
QUERY_STRING = 'ромашка'

if __name__ == '__main__':
    ctx = SearchContext(BATCH_SIZE, QUERY_STRING)


    async def main():
        async with aiohttp.ClientSession() as client:
            return await get_search_result(ctx, client)


    loop = asyncio.get_event_loop()
    response = loop.run_until_complete(main())
