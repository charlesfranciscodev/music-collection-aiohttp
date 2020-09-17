import aiopg.sa

from sqlalchemy import (
    MetaData, Table, Column, Integer, String, Text, ForeignKey, PrimaryKeyConstraint, UniqueConstraint
)


meta = MetaData()

artists = Table(
    "artists",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("websiteUrl", Text, nullable=True),
    Column("location", Text, nullable=True),
)

tracks = Table(
    "tracks",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("musicFileUrl", Text, nullable=False),
    Column("artistId", Integer, ForeignKey("artists.id", onupdate="CASCADE", ondelete="CASCADE")),
)

albums = Table(
    "albums",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255), nullable=False),
    Column("websiteUrl", Text, nullable=False),
    Column("artistId", Integer, ForeignKey("artists.id", onupdate="CASCADE", ondelete="CASCADE")),
    Column("coverArtFileUrl", Text, nullable=True),
    Column("description", Text, nullable=True),
)

albums_tracks = Table(
    "albums_tracks",
    meta,
    Column("albumId", Integer, ForeignKey("albums.id", onupdate="CASCADE", ondelete="CASCADE")),
    Column("trackId", Integer, ForeignKey("tracks.id", onupdate="CASCADE", ondelete="CASCADE")),
    Column("order", Integer, nullable=False),
    PrimaryKeyConstraint("albumId", "trackId"),
    UniqueConstraint("albumId", "order"),
)


async def init_pg(app):
    conf = app["config"]["postgres"]
    engine = await aiopg.sa.create_engine(
        database=conf["database"],
        user=conf["user"],
        password=conf["password"],
        host=conf["host"],
        port=conf["port"],
        minsize=conf["minsize"],
        maxsize=conf["maxsize"]
    )
    app["db"] = engine


async def close_pg(app):
    app["db"].close()
    await app["db"].wait_closed()
