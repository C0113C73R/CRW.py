Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import webbrowser
>>> import time
>>> import random
>>> 
>>> while True:
	sites = random.choice(["google.com", "mastercode.online", "youtube.com", "weather.gov"])
	visit = "http://{}".format(sites)
	webbrowser.open(visit)
	seconds = random.ranrange(5, 20)
	time.sleep(seconds)
	
