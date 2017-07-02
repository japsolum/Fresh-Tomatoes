import webbrowser

class Movie():
    def __init__(self, title, rating, time, year, storyline, poster, trailer):
        self.title = title
        self.rating = rating
        self.time = time
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def showTrailer(self):
        webbrowser.open(self.trailerYoutubeUrl)
