import app.crawler.search.parser as parser
import json


COMPANIES_URL = "https://fedresurs.ru/backend/companies/search"


# FIXME better solution is to get user agent from set of different agents
def get_post_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.86 Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type': 'application/json'
    }


def create_post_data(ctx):
    post_data = {
        'entitySearchFilter': {
            'startRowIndex': ctx.current_index,
            'pageSize': ctx.batch_size,
            'name': ctx.query
        }
    }
    return json.dumps(post_data)


async def get_result_page(ctx, client):
    post_data = create_post_data(ctx)
    async with client.post(COMPANIES_URL, data=post_data, headers=get_post_headers()) as resp:
        assert resp.status == 200
        return await resp.text()


async def get_search_result(ctx, client):
    all_ids = []
    while True:
        response = await get_result_page(ctx, client)
        json_data = parser.get_result_json(response)
        if parser.is_empty_page_result(json_data):
            break
        ctx.update_for_next_page()
        ids = parser.get_result_ids(json_data)
        all_ids.extend(ids)

    return all_ids
