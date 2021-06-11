import requests

createPlaylistURL = 'https://api.spotify.com/v1/users/ckovacs11/playlists'
addSongURL        = 'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

#insert auth token 
accessToken = ''

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
