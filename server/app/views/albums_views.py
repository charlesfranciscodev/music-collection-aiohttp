from aiohttp import web

import db


async def get_albums_view(request):
    async with request.app["db"].acquire() as conn:
        artist_id = request.match_info["artist_id"]
        result = await conn.execute(db.artists.select().where(db.artists.c.id == artist_id))
        if not await result.fetchone():
            raise web.HTTPBadRequest(text="Invalid foreign key: Artist id {}".format(artist_id))

        cursor = await conn.execute(db.albums.select().where(db.albums.c.artistId == artist_id))
        records = await cursor.fetchall()
        albums = [dict(record) for record in records]
        return web.json_response(albums)


async def get_album_view(request):
    async with request.app["db"].acquire() as conn:
        album_id = request.match_info["id"]
        result = await conn.execute(db.albums.select().where(db.albums.c.id == album_id))
        album = await result.fetchone()
        if not album:
            raise web.HTTPNotFound(text="Album with id {} does not exist".format(album_id))

        cursor = await conn.execute(db.albums_tracks.select().where(db.albums_tracks.c.albumId == album_id))
        albums_tracks = await cursor.fetchall()
        tracks = []
        for albums_track in albums_tracks:
            result = await conn.execute(db.tracks.select().where(db.tracks.c.id == albums_track["trackId"]))
            track = await result.fetchone()
            track = dict(track)
            track["order"] = albums_track["order"]
            tracks.append(track)
        album = dict(album)
        album["tracks"] = tracks

        return web.json_response(dict(album))


async def post_albums_view(request):
    async with request.app["db"].acquire() as conn:
        data = await request.json()

        artist_id = data.get("artistId")
        if artist_id:
            result = await conn.execute(db.artists.select().where(db.artists.c.id == artist_id))
            if not await result.fetchone():
                raise web.HTTPBadRequest(text="Invalid foreign key: Artist id {}".format(artist_id))

        result = await conn.execute(
            db.albums.insert().values(
                name=data["name"],
                websiteUrl=data["websiteUrl"],
                coverArtFileUrl=data.get("coverArtFileUrl"),
                description=data.get("description"),
                artistId=artist_id
            )
        )
        album = await result.fetchone()
        return web.json_response({
            "id": album["id"],
            "message": "Album created successfully"
        })


async def put_albums_view(request):
    async with request.app["db"].acquire() as conn:
        # update albums table
        data = await request.json()
        result = await conn.execute(
            db.albums.update()
            .returning(*db.albums.c)
            .where(db.albums.c.id == data["id"])
            .values(
                name=data["name"],
                websiteUrl=data["websiteUrl"],
                artistId=data.get("artistId"),
                coverArtFileUrl=data.get("coverArtFileUrl"),
                description=data.get("description"),
            )
        )
        album = await result.fetchone()
        if not album:
            raise web.HTTPNotFound(text="Album with id {} does not exist".format(data["id"]))

        # delete all tracks for this album (we will add back tracks to avoid conflicts between the track orders)
        # this works if we want to delete all tracks, delete some of them, or update them
        await conn.execute(db.albums_tracks.delete().where(db.albums_tracks.c.albumId == data["id"]))

        # update albums_tracks table
        if data["tracks"]:
            cursor = await conn.execute(db.albums_tracks.select().where(db.albums_tracks.c.albumId == data["id"]))
            prev_album_tracks = await cursor.fetchall()
            for track in data["tracks"]:
                # check if the track exists
                result = await conn.execute(db.tracks.select().where(db.tracks.c.id == track["id"]))
                record = await result.fetchone()
                if not record:
                    raise web.HTTPBadRequest(text="Invalid foreign key: Track id {}".format(track["id"]))

                # create a new albums_tracks entry
                await conn.execute(db.albums_tracks.insert().values(
                    albumId=data["id"],
                    trackId=track["id"],
                    order=track["order"]
                ))

        return web.json_response({"message": "Album updated successfully"})


async def delete_albums_view(request):
    async with request.app["db"].acquire() as conn:
        album_id = request.match_info["id"]
        result = await conn.execute(db.albums.select().where(db.albums.c.id == album_id))
        album = await result.fetchone()
        if not album:
            raise web.HTTPNotFound(text="Album with id {} does not exist".format(album_id))

        await conn.execute(db.albums.delete().where(db.albums.c.id == album_id))
        return web.HTTPNoContent()
