import requests 

API = "https://apis.xditya.me"

def search(text):
        r = requests.get(API + f"/lyrics?song={text}")
        find = r.json()
        return find
       
def lyrics(text):
        xD = search(text)
        lyric = f'**🎶 Successfully Extracted Lyrics Of {text} 🎶**\n\n\n\n'
        lyric += f'`{xD["lyrics"]}`'
        return text
