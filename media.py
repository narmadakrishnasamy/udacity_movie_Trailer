# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:18:41 2018


@author: HP
""" 
import webbrowser

class Movie():
    """ This file stores movie related information """
    VALID_RATINGS =["G","PG","PG-13","R"]
    
    def __init__(self, movie_title,movie_storyline,movie_image_url,movie_trailer_url):
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image_url
        self.trailer_youtube_url = movie_trailer_url
        
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
        