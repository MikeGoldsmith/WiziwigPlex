import re


class Channel:
    def __init__(self, name, url):
        self.name = name
        self.url = url


def Start():

    menu = ObjectContainer();


channel = Channel("mike", "http://shoof.alkass.net/shoof/live/live_1.php")
channels = [channel]

for c in channels:
    print(c.name)
    print(c.url)