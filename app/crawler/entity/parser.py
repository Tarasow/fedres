from app.crawler.common.parser_helper import get_result


def get_result_data(result_json):
    return get_result(result_json, extract_item_data)


def extract_item_data(item):
    guid = item['guid']

    item_type = item['type']
    if item_type != 'BankruptcyMessage':
        raise RuntimeError(f"Unknown type {item_type} for message with guid {guid}")

    return {
        'id': guid,
        'url': create_item_url(guid),
        'text': item['title'],
        'date': item['datePublish']
    }


def create_item_url(guid):
    return f"https://bankrot.fedresurs.ru/MessageWindow.aspx?ID={guid}"
