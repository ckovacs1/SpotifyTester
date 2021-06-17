import requests

#url to create playlist insert user id and playlist id for this to actually work 
createPlaylistURL = 'https://api.spotify.com/v1/users/{user_id}/playlists'

#spotify url for adding a song to playlist insert the playlist in the url
addSongURL        = 'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

#insert auth token 
accessToken = ''

def createPlaylist(name, public):
    
    #calls the url with the access token and create a playlist with a name and public setting
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

    #returns the json response
    json_resp = response.json()
    return json_resp

#TODO add function for adding songs to playlist 


def main():
    
    #creates a playlist with the name: playlist and a private setting
    playlist = createPlaylist("playlist", False)

    #prints confimation
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()
