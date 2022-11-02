from aiohttp import web
from app.settings import config, BASE_DIR
from app.database.accessor import PostgresAccessor

def setup_config(application):
    application["config"]=config


def setup_routes(application):
    from app.routes.routes import setup_routes as setup_app_routes
    setup_app_routes(application)

def setup_accessors(application):
    application['db']= PostgresAccessor()
    application['db'].setup(application)

def setup_app(application):
    setup_config(application)
    setup_accessors(application)
    set_external_libraries(application)
    setup_routes(application)


app = web.Application()  # run web server

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, port=config["con"]["port"])
