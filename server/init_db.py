from sqlalchemy import create_engine, MetaData

from app.settings import config
from app.db import artists, tracks, albums, albums_tracks


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"


def create_tables(engine):
    meta = MetaData()
    if engine.dialect.has_table(engine, "albums_tracks"):
        albums_tracks.drop(bind=engine)
    if engine.dialect.has_table(engine, "albums"):
        albums.drop(bind=engine)
    if engine.dialect.has_table(engine, "tracks"):
        tracks.drop(bind=engine)
    if engine.dialect.has_table(engine, "artists"):
        artists.drop(bind=engine)
    meta.create_all(bind=engine, tables=[artists, tracks, albums, albums_tracks])


def seed_artists(engine):
    conn = engine.connect()
    conn.execute(
        artists.insert(),
        [
            {
                "name": "Chad Crouch",
                "websiteUrl": "https://www.soundofpicture.com/",
                "location": "Portland, Oregon"
            },
            {
                "name": "Brevyn",
                "websiteUrl": "http://vulpianorecords.com/",
                "location": None
            },
            {
                "name": "Ketsa",
                "websiteUrl": "https://ketsa.uk//",
                "location": "London"
            },
            {
                "name": "KieLoKaz",
                "websiteUrl": "https://www.musikbrause.de/",
                "location": "Göppingen - Germany"
            },
            {
                "name": "Scott Holmes",
                "websiteUrl": "https://scottholmesmusic.com/",
                "location": "Arbroath, Scotland"
            }
        ]
    )
    conn.close()


def seed_tracks(engine):
    conn = engine.connect()
    conn.execute(
        tracks.insert(),
        [
            {
                "name": "Algorithms",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_01_-_Algorithms.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Elipsis",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_02_-_Elipsis.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Illustrated Novel",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_03_-_Illustrated_Novel.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Moonrise",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_04_-_Moonrise.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Negentropy",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_05_-_Negentropy.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Organisms",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_06_-_Organisms.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Shipping Lanes",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_07_-_Shipping_Lanes.mp3",
                "genreId": 5,
                "artistId": 1
            },

            {
                "name": "Bon Journée",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_01_-_Bon_Journe.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "The Ramble",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_02_-_The_Ramble.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Drifting",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_03_-_Drifting.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Barefoot",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_04_-_Barefoot.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Fuzzy Caterpillar",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_05_-_Fuzzy_Caterpillar.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Pacing",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_06_-_Pacing.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Starlight",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_07_-_Starlight.mp3",
                "genreId": 5,
                "artistId": 1
            },

            {
                "name": "Dusk",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_01_-_Dusk.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Dim",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_02_-_Dim.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "City Lights",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_03_-_City_Lights.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Small Hours",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_04_-_Small_Hours.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "The Gloaming",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_05_-_The_Gloaming.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Nocturnal",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_06_-_Nocturnal.mp3",
                "genreId": 5,
                "artistId": 1
            },
            {
                "name": "Daybreak",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_07_-_Daybreak.mp3",
                "genreId": 5,
                "artistId": 1
            },

            {
                "name": "Orange Eventide",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_01_-_Orange_Eventide.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Meditation Room II",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_02_-_Meditation_Room_II.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Siren's Call",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_03_-_Sirens_Call.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Moonbow",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_04_-_Moonbow.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Tranquil Bay",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_05_-_Tranquil_Bay.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Drinking the Dream",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_06_-_Drinking_the_Dream.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Dark Depths",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_07_-_Dark_Depths.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Sounding Echo",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_08_-_Sounding_Echo.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Melting Pearls",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_09_-_Melting_Pearls.mp3",
                "genreId": 5,
                "artistId": 2
            },
            {
                "name": "Waterwalk",
                "musicFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_10_-_Waterwalk.mp3",
                "genreId": 5,
                "artistId": 2
            },

            {
                "name": "Reunion of the Spaceducks (Kielokaz ID 365)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_01_-_Reunion_of_the_Spaceducks_Kielokaz_ID_365.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Trip to Ganymed (Kielokaz ID 363)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_02_-_Trip_to_Ganymed_Kielokaz_ID_363.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Wow (Kielokaz ID 359)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_03_-_Wow_Kielokaz_ID_359.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Just Arround the World (Kielokaz ID 362)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_04_-_Just_Arround_the_World_Kielokaz_ID_362.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Opening Horizons (Kielokaz ID 361)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_05_-_Opening_Horizons_Kielokaz_ID_361.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Krotenwurz (Kielokaz ID 360)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_06_-_Krotenwurz_Kielokaz_ID_360.mp3",
                "genreId": 10,
                "artistId": 4
            },
            {
                "name": "Alte Herren (Kielokaz ID 364)",
                "musicFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_07_-_Alte_Herren_Kielokaz_ID_364.mp3",
                "genreId": 10,
                "artistId": 4
            },

            {
                "name": "Storybook",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_01_-_Storybook.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Hotshot",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_02_-_Hotshot.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Stomps and Claps",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_03_-_Stomps_and_Claps.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Upbeat Party",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_04_-_Upbeat_Party.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Little Idea",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_05_-_Little_Idea.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Clear Progress",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_06_-_Clear_Progress.mp3",
                "genreId": 11,
                "artistId": 5
            },
            {
                "name": "Inspirational Outlook",
                "musicFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_07_-_Inspirational_Outlook.mp3",
                "genreId": 11,
                "artistId": 5
            }
        ]
    )
    conn.close()


def seed_albums(engine):
    conn = engine.connect()
    conn.execute(
        albums.insert(),
        [
            {
                "name": "Arps",
                "websiteUrl": "https://www.soundofpicture.com/",
                "genreId": 5,
                "artistId": 1,
                "coverArtFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_Arps_-_20190913144052757.jpg",
                "description": "With 'Arps' Portland, Or. composer/producer Chad Crouch has created a collection of warm analog synth tracks with arpeggiated melodies that recall the late 70’s early 80’s golden era of electronic music.  Meditative, undulating, sweeping synth parts weave together in a reflective, melodic reverie.  Touchstones include Air, OMD, The theme song to Stranger Things, and Kraftwerk."
            },
            {
                "name": "Drifter",
                "websiteUrl": "https://www.soundofpicture.com/",
                "genreId": 5,
                "artistId": 1,
                "coverArtFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_Drifter_-_20190805125622490.jpg",
                "description": "Portland, Or. composer/producer Chad Crouch has been on a bohemian power-ballad streak and 'Drifter' collects the cream of the crop.  The instrumental compositions are mellow, melodic, meandering and multifaceted.  Arrangements feature electric piano, electric bass, drums, synth, vibes, strings and detailed percussion, while melodies veer toward the sunny side of the street. It's a uniquely organic chill-out suite with heart."
            },
            {
                "name": "Night Tracks",
                "websiteUrl": "https://www.soundofpicture.com/",
                "genreId": 5,
                "artistId": 1,
                "coverArtFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_Night_Tracks_-_20190622142220691.jpg",
                "description": None
            },
            {
                "name": "Liquid Sunlight",
                "websiteUrl": "http://vulpianorecords.com/",
                "genreId": 5,
                "artistId": 2,
                "coverArtFileUrl": "https://music-collector.github.io/music/electronic/liquid-sunlight/Brevyn_-_Liquid_Sunlight_-_2018082593931258.png",
                "description": "Following Brevyn's single release on Vulpiano Records for Netlabel Day 2018, 'Sea Cave / Indigo' (vulpianorecords.bandcamp.com/album/sea-cave-indigo) comes a re-release of their delightfully summery 'Liquid Sunlight' album, complete with bonus tracks ('Drinking the Dream', 'Dark Depths') and an updated track order. More about 'Liquid Sunlight' From Brevyn: Liquid Sunlight was inspired by synth/sequencer-based new age of the 80s and early 90s like Vangelis, Spencer Nilsen [mostly his work on the Sega CD Ecco The Dolphin music] & Suzanne Ciani. Since this sort of music is often dismissed as pure cheese I wanted to contrast that presumption by emphasizing it’s more mysterious edges. This is not to say I think it can’t be good or effective without that sort of twist. But I also just wanted to explore that particular nostalgic yet haunting feeling certain pieces by say, Emerald Web or Vangelis captured really beautifully. You know, the twinkle of synth bells / flute in an old fantasy animation’s credits roll, which became strangely eerie as time went by and/or as the VHS got wonky. Even the way some 90s weather channel music sounds could apply. I felt sunsets were another thing I came to associate with this feeling, hence the one in the cover. I wanted to evoke a lost paradise, one surrounded by colorful nature with something sinister at work. The genuine beauty I heard in these songs and the motivation to create something similar myself - and without irony - are big parts of what led me to make this album."
            },
            {
                "name": "Free Ganymed",
                "websiteUrl": "https://www.musikbrause.de/",
                "genreId": 10,
                "artistId": 4,
                "coverArtFileUrl": "https://music-collector.github.io/music/jazz/free-ganymed/KieLoKaz_-_Free_Ganymed_-_20190912113845208.jpg",
                "description": "New Album out from the Staubkeller. We are a Jazz Livenjam Band, playling sometimes after work together."
            },
            {
                "name": "Inspiring & Upbeat Music",
                "websiteUrl": "https://scottholmesmusic.com/",
                "genreId": 11,
                "artistId": 5,
                "coverArtFileUrl": "https://music-collector.github.io/music/pop/inspiring-upbeat-music/Scott_Holmes_-_Inspiring__Upbeat_Music_-_2019090383732068.jpg",
                "description": "New Album out from the Staubkeller. We are a Jazz Livenjam Band, playling sometimes after work together."
            }
        ]
    )
    conn.close()


def seed_albums_tracks(engine):
    conn = engine.connect()
    conn.execute(
        albums_tracks.insert(),
        [
            {
                "albumId": 1,
                "trackId": 1,
                "order": 1
            },
            {
                "albumId": 1,
                "trackId": 2,
                "order": 2
            },
            {
                "albumId": 1,
                "trackId": 3,
                "order": 3
            },
            {
                "albumId": 1,
                "trackId": 4,
                "order": 4
            },
            {
                "albumId": 1,
                "trackId": 5,
                "order": 5
            },
            {
                "albumId": 1,
                "trackId": 6,
                "order": 6
            },
            {
                "albumId": 1,
                "trackId": 7,
                "order": 7
            },

            {
                "albumId": 2,
                "trackId": 8,
                "order": 1
            },
            {
                "albumId": 2,
                "trackId": 9,
                "order": 2
            },
            {
                "albumId": 2,
                "trackId": 10,
                "order": 3
            },
            {
                "albumId": 2,
                "trackId": 11,
                "order": 4
            },
            {
                "albumId": 2,
                "trackId": 12,
                "order": 5
            },
            {
                "albumId": 2,
                "trackId": 13,
                "order": 6
            },
            {
                "albumId": 2,
                "trackId": 14,
                "order": 7
            },

            {
                "albumId": 3,
                "trackId": 15,
                "order": 1
            },
            {
                "albumId": 3,
                "trackId": 16,
                "order": 2
            },
            {
                "albumId": 3,
                "trackId": 17,
                "order": 3
            },
            {
                "albumId": 3,
                "trackId": 18,
                "order": 4
            },
            {
                "albumId": 3,
                "trackId": 19,
                "order": 5
            },
            {
                "albumId": 3,
                "trackId": 20,
                "order": 6
            },
            {
                "albumId": 3,
                "trackId": 21,
                "order": 7
            },

            {
                "albumId": 4,
                "trackId": 22,
                "order": 1
            },
            {
                "albumId": 4,
                "trackId": 23,
                "order": 2
            },
            {
                "albumId": 4,
                "trackId": 24,
                "order": 3
            },
            {
                "albumId": 4,
                "trackId": 25,
                "order": 4
            },
            {
                "albumId": 4,
                "trackId": 26,
                "order": 5
            },
            {
                "albumId": 4,
                "trackId": 27,
                "order": 6
            },
            {
                "albumId": 4,
                "trackId": 28,
                "order": 7
            },
            {
                "albumId": 4,
                "trackId": 29,
                "order": 8
            },
            {
                "albumId": 4,
                "trackId": 30,
                "order": 9
            },
            {
                "albumId": 4,
                "trackId": 31,
                "order": 10
            },

            {
                "albumId": 5,
                "trackId": 32,
                "order": 1
            },
            {
                "albumId": 5,
                "trackId": 33,
                "order": 2
            },
            {
                "albumId": 5,
                "trackId": 34,
                "order": 3
            },
            {
                "albumId": 5,
                "trackId": 35,
                "order": 4
            },
            {
                "albumId": 5,
                "trackId": 36,
                "order": 5
            },
            {
                "albumId": 5,
                "trackId": 37,
                "order": 6
            },
            {
                "albumId": 5,
                "trackId": 38,
                "order": 7
            },

            {
                "albumId": 6,
                "trackId": 39,
                "order": 1
            },
            {
                "albumId": 6,
                "trackId": 40,
                "order": 2
            },
            {
                "albumId": 6,
                "trackId": 41,
                "order": 3
            },
            {
                "albumId": 6,
                "trackId": 42,
                "order": 4
            },
            {
                "albumId": 6,
                "trackId": 43,
                "order": 5
            },
            {
                "albumId": 6,
                "trackId": 44,
                "order": 6
            },
            {
                "albumId": 6,
                "trackId": 45,
                "order": 7
            }
        ]
    )
    conn.close()


if __name__ == "__main__":
    db_url = DSN.format(**config["postgres"])
    engine = create_engine(db_url)
    create_tables(engine)
    seed_artists(engine)
    seed_tracks(engine)
    seed_albums(engine)
    seed_albums_tracks(engine)
