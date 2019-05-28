from app.crawler.common.parser_helper import get_result


def get_result_ids(result_json):
    return get_result(result_json, lambda item: item['guid'])
