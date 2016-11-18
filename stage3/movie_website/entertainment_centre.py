import media
import fresh_tomatoes

earthlings = media.Movie("Earthlings", "Make the connection.", "https://static1.squarespace.com/static/55eb2900e4b079d8e4aebba2/t/55ec9b99e4b07f8c7796276d/1441569759158/", "https://www.youtube.com/watch?v=Hm7Babs_FJU", "1h 48m")

bold_native = media.Movie("Bold Native", "A film about animal liberation.", "http://rackcdn.elephantjournal.com/wp-content/uploads/2010/06/BoldNativePoster_6X91.jpg", "https://www.youtube.com/watch?v=KCL4jQWPQ-Q", "1h 45m")

cowspiracy = media.Movie("Cowspiracy", "The sustainability secret", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU5NzAyMzk1MF5BMl5BanBnXkFtZTgwODE3NjQyNTE@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=nV04zyfLyN4", "1h 31m")

best_speech = media.Movie("Best Speech Ever", "Best speech you will ever hear.", "best_speech_image.png", "https://www.youtube.com/watch?v=_K36Zu0pA4U", "0h 49m")

forks_over_knives = media.Movie("Forks Over Knives", "WARNING: This movie could save your life.", "https://upload.wikimedia.org/wikipedia/en/b/b6/Forks_Over_Knives_movie_poster.png", "https://www.youtube.com/watch?v=O7ijukNzlUg", "1h 36m")

speciesism = media.Movie("Speciesism: The Movie", "You'll never look at animals the same way again. Especially humans.", "http://t0.gstatic.com/images?q=tbn:ANd9GcRl2Xc0SEv5Bd_tSPkr-DzhvVSNWRgh0ubR9gtUWlT44nrsJknu", "https://www.youtube.com/watch?v=tJYzia6KUbs", "1h 34m")

lucent = media.Movie("Lucent", "Shining a light of Australian pig farming.", "https://www.google.com.au/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=0ahUKEwiTyK_wqrPQAhWIW5QKHUDqBd8QjBwIBA&url=http%3A%2F%2Fwww.aussiepigs.com%2Fimages%2Flucent%2FPoster4.jpg&bvm=bv.139250283,d.dGo&psig=AFQjCNFYxuqn6kyJL1Jj8XTQolLsB1T-GA&ust=1479593874579290", "https://vimeo.com/104075198", "1h 47m")

movies = [earthlings, bold_native, cowspiracy, best_speech, forks_over_knives, speciesism]

fresh_tomatoes.open_movies_page(movies)
