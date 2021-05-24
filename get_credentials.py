from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth, SpotifyPKCE
from spotipy.exceptions import SpotifyException
import spotipy
import os
import sys
import yaml

client_id = ""
client_secret = ""
redirect_uri = ""

scope = "playlist-modify-public"

manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, scope=scope, redirect_uri=redirect_uri)
print(manager.get_access_token())