# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 19:10:20 2020

@author: Brooks Hanson
"""
#%%
from IPython import get_ipython
get_ipython().magic('reset -sf')
# reset environment
#%%
import random #used to shuffle playlist
class Song:
    #construct the Song class
    def __init__(self, STitle, Artist):
        self.title = STitle
        self.artist = Artist
        #each song object has attributes of Title and Artist
        
    def __str__(self):
        return("Title: " + str(self.title) +
               "\nArtist: " +str(self.artist))
        #allow for built in print function use

class Playlist:
    #construct the Playlist class
    def __init__(self, PTitle, Desc=''):    #description set to null so user
        self.PlaylistTitle = PTitle         #can just enter a title if desired
        self.description = Desc
        self.AddSong = True     #This is used to set up our duplicate testing
        self.songs = []         #empty list of songs to be filled
        #each playlist object has attributes of a playlist title, description 
        #of playlist, and a list of all songs that have been added to the playlist
        
    def __str__(self):
        display = ("Playlist: " + str(self.PlaylistTitle) +
               "\nDescription: " + str(self.description) +
               "\nSongs: \n")   #prints title and description, and header for 
                                #the list of songs
        for song in self.songs:
            display += "{}\n".format(song)
            #concatenates each song in the playlist followed by a new line creator
            #so that the next song in the list will return on the following line
        return(display)
        #allows for use of built in print function
        
    def addSong(self, newsong):
        #Check for duplicates first
        for song in self.songs:
            try:
                if song.upper() == newsong.title.upper():
                    #if a song in the existing list is the same as the song 
                    #that user desires to add, AddSong is set to false so that 
                    #the song does not get added
                    self.AddSong = False
                    raise Exception     #Exception error is raised
            except (Exception):
                #error message is sent to user
                print("Song already exists in playlist")
        #if the AddSong attribute was net flipped to false, the title of the new
        #song is appended to the song list
        if self.AddSong is True:
            self.songs.append(newsong.title)
        #If user attempted to add duplicate, AddSong would be flipped to false
        #and the next song to be added, even if it is not a duplicate, will
        #not pass the above condition and won't be added. So, we set the 
        #AddSong attribute back to True after every addSong attempt
        else:
            self.AddSong = True
        
    def shuffleList(self):
        #uses shuffle method from random class to shuffle our list of songs.
        random.shuffle(self.songs)
        
    def songFound(self, findSong):
        #Checks to see if song is in playlist already.
        for song in self.songs:
            if song.upper() == findSong.upper():
                #if a song in the list matches the song we are checking, then
                #boolean True is returned. if not, boolean False is returned
                return True
            else:
                return False

