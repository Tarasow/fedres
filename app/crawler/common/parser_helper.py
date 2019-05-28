import json


def get_result_json(data):
    return json.loads(data)


def is_empty_page_result(result_json):
    return result_json['pageData'] == [] and result_json['found'] == 0


def get_result(result_json, extract_item_data):
    items = result_json['pageData']
    items_data = map(extract_item_data, items)
    return list(items_data)
