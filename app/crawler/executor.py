from app.crawler.entity.context import EntityContext
from app.crawler.entity.handler import EntityHandler
from app.crawler.search.context import SearchContext
from app.crawler.search.handler import SearchHandler
import asyncio
import aiohttp
import json


def run_task(query_str, batch_size):
    loop = asyncio.get_event_loop()

    ctx = SearchContext(batch_size, query_str)

    async def getting_ids():
        search_handler = SearchHandler()
        async with aiohttp.ClientSession() as client:
            return await search_handler.get_search_result(ctx, client)

    entities = loop.run_until_complete(getting_ids())

    messages = []
    for entity_guid in entities:
        entity_ctx = EntityContext(batch_size, entity_guid)

        async def getting_messages():
            entity_handler = EntityHandler()
            async with aiohttp.ClientSession() as client:
                return await entity_handler.get_entity_result(entity_ctx, client)

        messages.extend(loop.run_until_complete(getting_messages()))

    return json.dumps(messages)
