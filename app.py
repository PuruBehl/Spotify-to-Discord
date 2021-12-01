# Importing the libraries
from pprint import pprint
from current_song import get_current_playing_song
import time
import requests	

def main():
	count=0
	songs=["none"]
	while(count!=10000):
		count+=1
		time.sleep(1)
		current_song = get_current_playing_song()

		name = current_song["item"]["album"]["name"]
		artist = current_song["item"]["album"]["artists"][0]["name"]

		if name == songs[-1]:
			pass
		else:
			songs.append(name)
			# The current playing song
			print("The current playing song is : ",name,"  by : ",artist)

			# Now we are gonna write the code to make these songs play on our channel
			# command
			command = "!play "+name+" by "+artist

			url = "# Enter your discord url #"
			header = {
			'authorization': '# Enter your authorization key #'}

			payload1 = {
			'content' : command}
			payload2 = {
			'content': "!skip"
			}
			payload3 = {
			'content':'!clear-queue'
			}
			if songs[-2]=="none":
				r=requests.post(url,data=payload3,headers=header)
				r=requests.post(url,data=payload2,headers=header)
			else:
				r=requests.post(url,data=payload2,headers=header)

			r=requests.post(url,data=payload1,headers=header)


if __name__ == "__main__":
	main()