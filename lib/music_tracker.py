class MusicTracker():
    def __init__(self):
        self.list_of_music = []

    def add(self, title):
        if title == "":
            raise Exception("No title was entered.")
        else:
            self.list_of_music.append(title)

    def getTracks(self):
        return self.list_of_music