from app.crawler.entity.context import EntityContext
from app.crawler.entity.handler import EntityHandler
from app.crawler.search.context import SearchContext
from app.crawler.search.handler import SearchHandler
import asyncio
import aiohttp

DEFAULT_BATCH_SIZE = 250

if __name__ == '__main__':
    entered_batch_size = input("Enter test batch size: ")
    test_batch_size = DEFAULT_BATCH_SIZE if entered_batch_size == "" else int(entered_batch_size)

    test_query_str = input("Enter test query string: ")

    loop = asyncio.get_event_loop()

    ctx = SearchContext(test_batch_size, test_query_str)


    async def getting_ids():
        search_handler = SearchHandler()
        async with aiohttp.ClientSession() as client:
            return await search_handler.get_search_result(ctx, client)


    entities = loop.run_until_complete(getting_ids())
    print(entities)

    messages = []
    for entity_guid in entities:
        entity_ctx = EntityContext(DEFAULT_BATCH_SIZE, entity_guid)


        async def getting_messages():
            entity_handler = EntityHandler()
            async with aiohttp.ClientSession() as client:
                return await entity_handler.get_entity_result(entity_ctx, client)


        messages.extend(loop.run_until_complete(getting_messages()))

    print(messages)
