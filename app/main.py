import app.crawler.executor as crawler

DEFAULT_BATCH_SIZE = 250

if __name__ == '__main__':
    entered_batch_size = input("Enter test batch size: ")
    test_batch_size = DEFAULT_BATCH_SIZE if entered_batch_size == "" else int(entered_batch_size)

    test_query_str = input("Enter test query string: ")

    messages = crawler.run_task(test_query_str, test_batch_size)
    print(messages)
