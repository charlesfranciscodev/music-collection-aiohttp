from views.artists_views import get_artists_view, post_artists_view, put_artists_view, delete_artists_view
from views.tracks_views import get_track_view, post_tracks_view, put_tracks_view, delete_tracks_view
from views.albums_views import get_albums_view, get_album_view, post_albums_view, put_albums_view, delete_albums_view


async def test_view(request):
    return web.json_response({
        "message": "Yo mamma so fat even penguins are jealous of the way she waddles."
    })


def setup_routes(app):
    app.router.add_get("/api/test", test_view)

    app.router.add_get("/api/artists", get_artists_view)
    app.router.add_post("/api/artists", post_artists_view)
    app.router.add_put("/api/artists", put_artists_view)
    app.router.add_delete("/api/artists/{id}", delete_artists_view)

    app.router.add_get("/api/tracks/{id}", get_track_view)
    app.router.add_post("/api/tracks", post_tracks_view)
    app.router.add_put("/api/tracks", put_tracks_view)
    app.router.add_delete("/api/tracks/{id}", delete_tracks_view)

    app.router.add_get("/api/albums/artists/{artist_id}", get_albums_view)
    app.router.add_get("/api/albums/{id}", get_album_view)
    app.router.add_post("/api/albums", post_albums_view)
    app.router.add_put("/api/albums", put_albums_view)
    app.router.add_delete("/api/albums/{id}", delete_albums_view)
