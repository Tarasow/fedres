from aiohttp import web
import app.crawler.executor as crawler
import threading

DEFAULT_BATCH_SIZE = 250


class TaskServer:
    def __init__(self):
        self.tasks = set()
        self.results = {}
        app = web.Application()
        app.router.add_get('/create_task/{task}', self.handle)
        app.router.add_get('/tasks/{task}', self.handle)
        web.run_app(app, host='127.0.0.1', port=8081)

    def is_task_exists(self, task):
        return task in self.tasks or task in self.results.keys()

    def append_data(self, task, batch):
        self.tasks.add(task)
        self.results[task] = crawler.run_task(task, batch)
        self.tasks.remove(task)

    async def handle(self, request):
        task = request.match_info.get('task')
        if request.path.startswith('/create_task/'):
            if self.is_task_exists(task):
                return web.Response(text=f'Task with id "{task}" is already created')
            thread = threading.Thread(target=self.append_data, args=(task, DEFAULT_BATCH_SIZE,))
            thread.start()
            return web.Response(text=f'Successfully created task with id "{task}"')

        if request.path.startswith('/tasks/'):
            result = self.results.get(task, None)
            if result:
                return web.Response(text=result)
            else:
                return web.Response(text=f'Missing results for task with id "{task}"')
