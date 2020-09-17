from aiohttp import web

from db import init_pg, close_pg
from settings import config
from routes import setup_routes


app = web.Application()
app["config"] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
setup_routes(app)
web.run_app(app)
