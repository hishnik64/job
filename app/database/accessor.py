from aiohttp import web


# подключени и отключение от базы
class PostgresAccessor:
    def __init__(self) -> None:
        # TODO: почему импорт здесь?
        from app.routes.models import Users

        self.message = Users
        self.db = None

    # TODO: блять здесь есть типизация, а в main.py нет.
    #  И если метод ничего не возвращает не указывай "-> None", вообще ничего не пиши
    def setup(self, application: web.Application) -> None:
        application.cleanup_ctx.append(self._on_connect)
        # application.on_startup.append(self._on_connect)
        # application.on_cleanup.append(self._on_disconnect)

    # async def _on_connect(self, application: web.Application):
    #     from app.database.models import db
    #
    #     self.config = application["config"]["postgres"]
    #     await  db.se_bind(self.config["database_url"])
    #     self.db = db
    #
    # async def _on_disconnect(self, _) -> None:
    #     if self.db is not None:
    #         await  self.db.pop_bind().close()

    # TODO: используй такую конструкцию, почитай про yield. И что за ебучий двойной пробел, чумба?
    async def _on_connect(self, application: web.Application):
        # TODO: опять импорт хуй знает где
        from app.database.models import db

        self.config = application["config"]["postgres"]
        await db.se_bind(self.config["database_url"])
        self.db = db
        yield
        if self.db is not None:
            await self.db.pop_bind().close()
