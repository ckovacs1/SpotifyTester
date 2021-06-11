import requests

#insert user id and playlist id for this to actually work 
createPlaylistURL = 'https://api.spotify.com/v1/users/{user_id}/playlists'
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

#TODO add function for adding songs to playlist 


def main():
    playlist = createPlaylist("playlist", False)

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()
