# Music Collection REST API

## Docker Commands

Build the image(s):

`docker-compose build`

Run the container(s):

`docker-compose up`

Seed the database:

```shell
cd server
python3 init_db.py
```

Access the database via psql:

`docker-compose exec database psql -U admin`

## Web Server Commands

Create a Python virtual environment:

`python3 -m venv server`

Activate the virtual environment:

```shell
cd server
source bin/activate
```

Install dependencies:

```shell
cd server
pip3 install requirements.txt
```

Start the web server

```shell
cd server
python3 app/main.py
```

## API Route(s)

**GET** `/api/test`

Just a test route to check if the web server is working.

Response
```json
{
  "message": "Yo mamma so fat even penguins are jealous of the way she waddles."
}
```

### Artists

#### GET `/api/artists`

Return an array of all music artists.

Response
```json
[
  {
    "id": 1,
    "name": "Chad Crouch",
    "websiteUrl": "https://www.soundofpicture.com/",
    "location": "Portland, Oregon"
  },
  {
    "id": 2,
    "name": "Brevyn",
    "websiteUrl": "http://vulpianorecords.com/",
    "location": null
  },
  {
    "id": 3,
    "name": "Ketsa",
    "websiteUrl": "https://ketsa.uk//",
    "location": "London"
  }
]
```

---

#### POST `/api/artists`

Create a new music artist.

Request
```json
{
  "name": "New Artist",
  "websiteUrl": "https://website.com/",
  "location": "Planet Earth"
}
```

Response
```json
{
  "id": 9,
  "message": "Artist created successfully"
}
```
200 | Artist created successfully

---

#### PUT `/api/artists`

Update a music artist.

Request
```json
{
  "id": 6,
  "name": "Hype Artist",
  "websiteUrl": "https://example.com/",
  "location": "Somewhere on Earth"
}
```

Response
```json
{
  "message": "Artist updated successfully"
}
```
200 | Artist updated successfully

404 | Artist does not exist

---

#### DELETE `/api/artists/{:id}`

Delete a music artist with the given id.

Response

204 | No Content (deleted)

404 | Artist does not exist

### Tracks

#### GET `/api/tracks/{:id}`

Return a track with the given id.

Response
```json
{
  "id": 1,
  "name": "Algorithms",
  "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_01_-_Algorithms.mp3",
  "artistId": 1
}
```
200 | Success

404 | Track does not exist

---

#### POST `/api/tracks`

Create a new track.

Request
```json
{
  "name": "New Track",
  "musicFileUrl": "https://example.com/track.mp3",
  "artistId": 1
}
```

Response
```json
{
  "id": 62,
  "message": "Track created successfully"
}
```
200 | Track created successfully

400 | Invalid foreign key

---

#### PUT `/api/tracks`

Update a track.

Request
```json
{
  "id": 62,
  "name": "New Track 2",
  "musicFileUrl": "https://example.com/track2.mp3",
  "artistId": 2
}
```

Response
```json
{
  "message": "Track updated successfully"
}
```
200 | Track updated successfully

400 | Invalid foreign key

404 | Track does not exist

---

#### DELETE `/api/tracks/{:id}`

Delete a track with the given id.

Response

204 | No Content (deleted)

404 | Track does not exist

### Albums

#### GET `/api/albums/artists/{:artist_id}`

Return an array of all music albums for the corresponding artist.

Response
```json
[
  {
    "id": 1,
    "name": "Arps",
    "websiteUrl": "https://www.soundofpicture.com/",
    "artistId": 1,
    "coverArtFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_Arps_-_20190913144052757.jpg",
    "description": "With 'Arps' Portland, Or. composer/producer Chad Crouch has created a collection of warm analog synth tracks with arpeggiated melodies that recall the late 70’s early 80’s golden era of electronic music.  Meditative, undulating, sweeping synth parts weave together in a reflective, melodic reverie.  Touchstones include Air, OMD, The theme song to Stranger Things, and Kraftwerk."
  },
  {
    "id": 2,
    "name": "Drifter",
    "websiteUrl": "https://www.soundofpicture.com/",
    "artistId": 1,
    "coverArtFileUrl": "https://music-collector.github.io/music/electronic/drifter/Chad_Crouch_-_Drifter_-_20190805125622490.jpg",
    "description": "Portland, Or. composer/producer Chad Crouch has been on a bohemian power-ballad streak and 'Drifter' collects the cream of the crop.  The instrumental compositions are mellow, melodic, meandering and multifaceted.  Arrangements feature electric piano, electric bass, drums, synth, vibes, strings and detailed percussion, while melodies veer toward the sunny side of the street. It's a uniquely organic chill-out suite with heart."
  },
  {
    "id": 3,
    "name": "Night Tracks",
    "websiteUrl": "https://www.soundofpicture.com/",
    "artistId": 1,
    "coverArtFileUrl": "https://music-collector.github.io/music/electronic/night-tracks/Chad_Crouch_-_Night_Tracks_-_20190622142220691.jpg",
    "description": null
  }
]
```
200 | Success

400 | Artist does not exist

---

#### GET `/api/albums/{:id}`

Return a music album with the given id and all its tracks.

Response
```json
{
  "id": 1,
  "name": "Arps",
  "websiteUrl": "https://www.soundofpicture.com/",
  "artistId": 1,
  "coverArtFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_Arps_-_20190913144052757.jpg",
  "description": "With 'Arps' Portland, Or. composer/producer Chad Crouch has created a collection of warm analog synth tracks with arpeggiated melodies that recall the late 70’s early 80’s golden era of electronic music.  Meditative, undulating, sweeping synth parts weave together in a reflective, melodic reverie.  Touchstones include Air, OMD, The theme song to Stranger Things, and Kraftwerk.",
  "tracks": [
    {
      "id": 1,
      "name": "Algorithms",
      "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_01_-_Algorithms.mp3",
      "artistId": 1,
      "order": 1
    },
    {
      "id": 2,
      "name": "Elipsis",
      "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_02_-_Elipsis.mp3",
      "artistId": 1,
      "order": 2
    },
    {
      "id": 3,
      "name": "Illustrated Novel",
      "musicFileUrl": "https://music-collector.github.io/music/electronic/arps/Chad_Crouch_-_03_-_Illustrated_Novel.mp3",
      "artistId": 1,
      "order": 3
    }
  ]
}
```
200 | Success

404 | Album does not exist

---

#### POST `/api/albums`

Create a new album.

Request
```json
{
  "name": "New Album",
  "websiteUrl": "https://example.com",
  "artistId": 1,
  "coverArtFileUrl": "https://example.com/cover-art.png",
  "description": "Sugar plum gummi bears jelly-o ice cream croissant. Sugar plum lollipop muffin pudding chocolate dragée macaroon. Marzipan powder sugar plum."
}
```

Response
```json
{
  "id": 10,
  "message": "Album created successfully"
}
```
200 | Album created successfully

400 | Invalid foreign key

---

#### PUT `/api/albums`

Update an album and its tracks.

Request
```json
{
  "id": 7,
  "name": "New Album 2",
  "websiteUrl": "https://example2.com",
  "artistId": 2,
  "coverArtFileUrl": "https://example.com/cover-art2.png",
  "description": "Sugar2 plum gummi bears jelly-o ice cream croissant. Sugar plum lollipop muffin pudding chocolate dragée macaroon. Marzipan powder sugar plum.",
  "tracks": [
    {
      "id": 1,
      "order": 1
    },
    {
      "id": 2,
      "order": 2
    },
    {
      "id": 3,
      "order": 3
    }
  ]
}
```

Response
```json
{
  "message": "Album updated successfully"
}
```
200 | Album updated successfully

400 | Invalid foreign key

404 | Album does not exist

---

#### DELETE `/api/albums/{:id}`

Delete an album with the given id.

Response

204 | No Content (deleted)

404 | Album does not exist

## Credit(s)
* [Original Project](https://github.com/charlesfranciscodev/music-collection)
* [AIOHTTP](https://docs.aiohttp.org/en/stable/)
* [Music](https://github.com/music-collector/music-collector.github.io/tree/master/music)
