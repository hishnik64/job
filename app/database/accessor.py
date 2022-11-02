from aiohttp import web


# подключени и отключение от базы
class PostgresAccessor:
    def __init__(self) -> None:
        from app.routes.models import Users

        self.message = Users
        self.db = None

    def setup(self, application: web.Application) -> None:
        application.on_startup.append(self._on_connect)
        application.on_cleanup.append(self._on_disconnect)

    async def _on_connect(self, application: web.Application):
        from app.database.models import db

        self.config = application["config"]["postgres"]
        await  db.se_bind(self.config["database_url"])
        self.db = db

    async def _on_disconnect(self, _) -> None:
        if self.db is not None:
            await  self.db.pop_bind().close()
