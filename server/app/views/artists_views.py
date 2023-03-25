from aiohttp import web

import db


async def get_artists_view(request):
    async with request.app["db"].acquire() as conn:
        cursor = await conn.execute(db.artists.select())
        records = await cursor.fetchall()
        artists = [dict(record) for record in records]
        return web.json_response(artists)


async def post_artists_view(request):
    async with request.app["db"].acquire() as conn:
        data = await request.json()
        result = await conn.execute(
            db.artists.insert().values(
                name=data["name"],
                websiteUrl=data.get("websiteUrl"),
                location=data.get("location")
            )
        )
        artist = await result.fetchone()
        return web.json_response({
            "id": artist["id"],
            "message": "Artist created successfully"
        })


async def put_artists_view(request):
    async with request.app["db"].acquire() as conn:
        data = await request.json()
        result = await conn.execute(
            db.artists.update()
            .returning(*db.artists.c)
            .where(db.artists.c.id == data["id"])
            .values(
                name=data["name"],
                websiteUrl=data.get("websiteUrl"),
                location=data.get("location")
            )
        )
        artist = await result.fetchone()
        if not artist:
            raise web.HTTPNotFound(text="Artist with id {} does not exist".format(data["id"]))
        return web.json_response({
            "message": "Artist updated successfully"
        })


async def delete_artists_view(request):
    async with request.app["db"].acquire() as conn:
        artist_id = request.match_info["id"]
        result = await conn.execute(db.artists.select().where(db.artists.c.id == artist_id))
        artist = await result.fetchone()
        if not artist:
            raise web.HTTPNotFound(text="Artist with id {} does not exist".format(artist_id))

        await conn.execute(
            db.artists.delete()
            .where(db.artists.c.id == artist_id)
        )
        return web.HTTPNoContent()
