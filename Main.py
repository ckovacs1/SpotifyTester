import requests

createPlaylistURL = 'https://api.spotify.com/v1/users/ckovacs11/playlists'
addSongURL        = 'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

accessToken = 'BQC7mjEOxak1FyDHid9Ql5bKwenAgD5X79CH7NMopeDEEGUCAdH_4aLm6ub6xrN-r7J12nw46zKXfcu8QV1cMSIB-IawoWDYUNMOGfopg-7uaH_Yqrm7aIjkEgrjtz3pUZ1POwQXykDsmRE4rHUpS9HZU8b6FELxBR-__ncXvGDteQ'

def createPlaylist(name, public):
    response = requests.post(
        createPlaylistURL,
        headers={
            "Authorization": f"Bearer {accessToken}"
        },
        json={
            "name": name,
            "public": public
        }
    )

    json_resp = response.json()
    return json_resp


def main():
    playlist = createPlaylist("playlist", False)

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()
