from app.crawler.entity.context import EntityContext
from app.crawler.entity.handler import EntityHandler
from app.crawler.search.context import SearchContext
from app.crawler.search.handler import SearchHandler
import json


def getting_ids(batch_size, query_str):
    ctx = SearchContext(batch_size, query_str)
    search_handler = SearchHandler()
    return search_handler.get_search_result(ctx)


def getting_messages(batch_size, entity_guid):
    ctx = EntityContext(batch_size, entity_guid)
    entity_handler = EntityHandler()
    return entity_handler.get_entity_result(ctx)


def run_task(query_str, batch_size):
    entities = getting_ids(batch_size, query_str)

    messages = []
    for entity_guid in entities:
        messages.extend(getting_messages(batch_size, entity_guid))

    return json.dumps(messages)
