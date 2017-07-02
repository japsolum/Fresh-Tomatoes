import media
import fresh_Tomatoes

#creates multiple objects of the Movie class
toyStory = media.Movie("Toy Story", "G", "1hr 21mins", "1995",
"A story about a boy and his toys that come to life",
"http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "PG-13", "2hr 42mins", "2009",
"A marine visits an alien planet and befriends the inhabitants",
"http://www.impawards.com/2009/posters/avatar.jpg",
"https://youtu.be/5PSNL1qE6VY")
darkKnight = media.Movie("The Dark Knight","PG-13", "2hr 32min", "2008",
"Batman faces off against his nemesis Joker",
"http://www.impawards.com/2008/posters/dark_knight_ver12.jpg",
"https://youtu.be/EXeTwQWrcwY")
darkKnightRises = media.Movie("The Dark Knight Rises", "PG-13", "2hr 44 mins", "2012",
"Batman must stop baine from taking controll of gotham",
"http://cdn.collider.com/wp-content/uploads/the-dark-knight-rises-poster-405x600.jpg",
"https://youtu.be/ay-Xg1oTeAs")
inception = media.Movie("Inception", "PG-13", "2hr 28mins", "2010",
"Characters must use the ability to enter peoples dreams without being lost forever.",
"http://img.moviepostershop.com/inception-movie-poster-2010-1010547301.jpg",
"https://youtu.be/YoHD9XEInc0")
hangover = media.Movie("The Hangover", "R", "1hr 40mins", "2009",
"After a night of heavy partying, a group friends must find where they lost their 4th party member",
"http://www.impawards.com/2009/posters/hangover.jpg",
"https://youtu.be/tcdUhdOlz9M")

movies = [toyStory, avatar, darkKnight, darkKnightRises, inception, hangover]
fresh_Tomatoes.open_movies_page(movies)
