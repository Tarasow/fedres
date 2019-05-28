import json


def get_result_json(data):
    return json.loads(data)


def is_empty_page_result(result_json):
    return result_json['pageData'] == [] and result_json['found'] == 0


def get_result_ids(result_json):
    items = result_json['pageData']
    ids = map(lambda item: item['guid'], items)
    return list(ids)
