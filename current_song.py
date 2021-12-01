from getting_keys import get_authtoken
import requests
from requests.structures import CaseInsensitiveDict
import json

def get_current_playing_song():

	# Getting the authtoken from the credential file
	authtoken = get_authtoken()

	# Making a parameter dictionary
	headers_dic = CaseInsensitiveDict()
	headers_dic["Accept"] = "application/json"
	headers_dic["Content-Type"] = "application/json"
	headers_dic["Authorization"] = authtoken

	song_details = requests.get("https://api.spotify.com/v1/me/player/currently-playing",headers=headers_dic)

	return(json.loads(song_details.text))


















