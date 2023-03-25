from aiohttp import web

import db


async def get_track_view(request):
    async with request.app["db"].acquire() as conn:
        track_id = request.match_info["id"]
        result = await conn.execute(db.tracks.select().where(db.tracks.c.id == track_id))
        track = await result.fetchone()
        if not track:
            raise web.HTTPNotFound(text="Track with id {} does not exist".format(track_id))
        return web.json_response(dict(track))


async def post_tracks_view(request):
    async with request.app["db"].acquire() as conn:
        data = await request.json()

        artist_id = data.get("artistId")
        if artist_id:
            result = await conn.execute(db.artists.select().where(db.artists.c.id == artist_id))
            if not await result.fetchone():
                raise web.HTTPBadRequest(text="Invalid foreign key: Artist id {}".format(artist_id))

        result = await conn.execute(
            db.tracks.insert().values(
                name=data["name"],
                musicFileUrl=data["musicFileUrl"],
                artistId=artist_id
            )
        )
        track = await result.fetchone()
        return web.json_response({
            "id": track["id"],
            "message": "Track created successfully"
        })


async def put_tracks_view(request):
    async with request.app["db"].acquire() as conn:
        data = await request.json()

        artist_id = data.get("artistId")
        if artist_id:
            result = await conn.execute(db.artists.select().where(db.artists.c.id == artist_id))
            if not await result.fetchone():
                raise web.HTTPBadRequest(text="Invalid foreign key: Artist id {}".format(artist_id))

        result = await conn.execute(
            db.tracks.update()
            .returning(*db.tracks.c)
            .where(db.tracks.c.id == data["id"])
            .values(
                name=data["name"],
                musicFileUrl=data["musicFileUrl"],
                artistId=artist_id
            )
        )
        track = await result.fetchone()
        if not track:
            raise web.HTTPNotFound(text="Track with id {} does not exist".format(data["id"]))
        return web.json_response({
            "message": "Track updated successfully"
        })


async def delete_tracks_view(request):
    async with request.app["db"].acquire() as conn:
        track_id = request.match_info["id"]
        result = await conn.execute(db.tracks.select().where(db.tracks.c.id == track_id))
        track = await result.fetchone()
        if not track:
            raise web.HTTPNotFound(text="Track with id {} does not exist".format(track_id))

        await conn.execute(
            db.tracks.delete()
            .where(db.tracks.c.id == track_id)
        )
        return web.HTTPNoContent()
