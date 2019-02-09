# -*- coding: utf-8 -*-
"""
Created on Fri jan 4 12:19:31 2018

@author: Narmada Krishnasamy
"""
# movie 
import media 
import fresh_tomatoes

# Object arguments 
birds = media.Movie("For the Birds - 2000", 
                        "A group of snooty birds roosting on a telephone wire get their just deserts when a goofy bird drops in.",
                        "https://m.media-amazon.com/images/M/MV5BMTQzMDEyODYwNF5BMl5BanBnXkFtZTgwOTcxMDgwMjE@._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=WjoDEQqyTig")

presto = media.Movie("Presto - 2008", 
                        "Presto, a magician , who uses a rabbit to entertain, doesn't feed the rabbit suitably. Angry, the rabbit take revenge on Presto.",
                        "https://m.media-amazon.com/images/M/MV5BMTEwNjMwMjc3MDdeQTJeQWpwZ15BbWU4MDg0OTA4MDIx._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=D4Dnm6dkOVI")

piper = media.Movie("Piper - 2016", 
                        "A mother bird tries to teach her little one how to find food by herself. ",
                        "https://m.media-amazon.com/images/M/MV5BNzhhMDkwNWItMmRlMS00ODg1LTkzMzAtZGM3NTAwNzViZGU5XkEyXkFqcGdeQXVyOTI3MDg0NzA@._V1_QL50_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=e7v2zDZBf6g&index=3&list=PLOEvE3uqph5ZKXsq8Q7JzlWbadeWtahQf")

lifted = media.Movie("Lifted - 2006", 
                        "A teenage alien tries to abduct a sleeping human, but with so many switches to do so, it's nearly impossible.",
                        "https://m.media-amazon.com/images/M/MV5BMjE0MTcyNDQ3M15BMl5BanBnXkFtZTcwMzI0MjA1MQ@@._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=i62znvPLlrw")

luna = media.Movie("La Luna - 2011", 
                        "A young boy helps his father and grandfather harvest stars from the moon.",
                        "https://m.media-amazon.com/images/M/MV5BZThmZjNjOTctNjhjNy00OGE5LTlhODEtNTRkMWE3NzJjMjdmXkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=vbuq7w3ZDUQ")

game = media.Movie("Geri's Game - 1997", 
                        "Geri sets up a chess game to play his greatest opponent - himself.",
                        "https://m.media-amazon.com/images/M/MV5BMTg3OTkxODU3OV5BMl5BanBnXkFtZTgwNDgxMDgwMjE@._V1_QL50_.jpg",
                        "https://www.youtube.com/watch?v=GgKHwCcMcGY")

# Create movie trailer page with array of Movie class objects
movies = [piper,presto,birds,lifted,luna,game]

# Create page with movies as listed
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__module__)