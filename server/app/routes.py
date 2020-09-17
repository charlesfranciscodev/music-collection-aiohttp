from views import test_view, get_artists_view


def setup_routes(app):
    app.router.add_get("/api/test", test_view)
    app.router.add_get("/api/artists", get_artists_view)
