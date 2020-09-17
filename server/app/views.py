from aiohttp import web

import db


async def test_view(request):
    return web.json_response({
        "message": "Yo mamma so fat even penguins are jealous of the way she waddles."
    })


async def get_artists_view(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(db.artists.select())
        records = await cursor.fetchall()
        artists = [dict(record) for record in records]
        return web.json_response(artists)
