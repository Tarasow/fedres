from app.crawler.common.handler_base import HandlerBase
import app.crawler.common.parser_helper as parse_helper
import app.crawler.entity.parser as parser
import json


class EntityHandler(HandlerBase):
    request_url = "https://fedresurs.ru/backend/companies/publications"

    def create_post_data(self, ctx):
        post_data = {
            'guid': ctx.guid,
            'startRowIndex': ctx.current_index,
            'pageSize': ctx.batch_size,
            'searchFirmBankruptMessage': True
        }
        return json.dumps(post_data)

    async def get_entity_result(self, ctx, client):
        all_messages = []
        while True:
            response = await self.get_result_page(ctx, client)
            json_data = parse_helper.get_result_json(response)
            if parse_helper.is_empty_page_result(json_data):
                break
            ctx.update_for_next_page()
            entity_data = parser.get_result_data(json_data)
            all_messages.extend(entity_data)

        return all_messages
