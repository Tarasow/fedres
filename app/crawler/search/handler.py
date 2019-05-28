from app.crawler.common.handler_base import HandlerBase
import app.crawler.common.parser_helper as parse_helper
import app.crawler.search.parser as parser
import json


class SearchHandler(HandlerBase):
    request_url = "https://fedresurs.ru/backend/companies/search"

    def create_post_data(self, ctx):
        post_data = {
            'entitySearchFilter': {
                'startRowIndex': ctx.current_index,
                'pageSize': ctx.batch_size,
                'name': ctx.query
            }
        }
        return json.dumps(post_data)

    async def get_search_result(self, ctx, client):
        all_ids = []
        while True:
            response = await self.get_result_page(ctx, client)
            json_data = parse_helper.get_result_json(response)
            if parse_helper.is_empty_page_result(json_data):
                break
            ctx.update_for_next_page()
            ids = parser.get_result_ids(json_data)
            all_ids.extend(ids)

        return all_ids
