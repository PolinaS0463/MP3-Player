from bs4 import BeautifulSoup
import requests, sys, os
import sqlite3 as sq
import database
import re

class YourMusic:
    def __init__(self, songs: list = None, download_path: str = "http://rus.hitmotop.com/search?q=", songs_path = "XXMusic1") -> None:
        if songs is None: self.my_songs: list[Song] = []
        else: self.my_songs = songs
        self.download_path = download_path

    def play_song(self, song_id: int) -> None: # Метод включает песню ✓
        os.system("afplay " + self.my_songs[song_id].path)
        self.my_songs[song_id].rating += 1
        with sq.connect(database.DATABASE_PATH) as con:
            cur = con.cursor()
            rating_request = f"UPDATE songs SET rating=rating+1 WHERE id = {song_id + 1}"
            cur.execute(rating_request) 

    def download_song(self, song_info: list[str], a_link: str) -> None: # Метод скачивает песню ✓
        download_link = a_link.get("href")
        song = requests.get(download_link, stream=True)
        file_path = song_info[3]
        if song.status_code == requests.codes.ok:
            with open(file_path, 'wb') as file:
                file.write(song.content)
        self.my_songs.append(Song(song_info[1], file_path, song_info[2], 0))        
        with sq.connect(database.DATABASE_PATH) as con:
            cur = con.cursor()
            insert_request = f"INSERT INTO songs (name, path, singer, rating) VALUES(?, ?, ?, ?)"
            data = [song_info[1], file_path, song_info[2], 0]
            cur.execute(insert_request, data)

    def delete_song(self, song_id: int) -> None: # Метод удаляет песню ✓
        os.remove(self.my_songs[song_id].path)
        self.my_songs.pop(song_id)
        with sq.connect(database.DATABASE_PATH) as con:
            cur = con.cursor()
            delete_request = f"DELETE FROM songs WHERE id = {song_id + 1}"
            cur.execute(delete_request)
            shift_request = f"UPDATE songs SET id=id-1 WHERE id > {song_id}"
            cur.execute(shift_request)

    def search_song(self, sample: str) -> list: # Метод ищет песни ✓
        findings = []
        for song in self.my_songs:
            if sample.lower() == song.name.lower() or sample.lower() == song.singer.lower():
                findings.append(song)
        return findings

    def find_link(self, song_info: list[str]) -> None | str: # Метод ищет -a- необходимой нам песни на WEB-странице ✓
        web_page_path = self.download_path + song_info[0]
        web_code = requests.get(web_page_path).text
        soup = BeautifulSoup(web_code, features="html.parser")
        a_link = soup.find("a", class_="track__download-btn")
        return a_link

    def restore_songs(self) -> None: # Метод проходится по строкам базы данных и заполняет self.my_songs ✓
        with sq.connect(database.DATABASE_PATH) as con: 
            cur = con.cursor()
            cur.execute("SELECT * FROM songs")
            songs_restored = cur.fetchall()
            for song_restored in songs_restored:
                song = Song(song_restored[1], song_restored[2], song_restored[3], song_restored[4])
                self.my_songs.append(song)            
        return songs_restored
                    
    def get_song_index(self, song) -> int: # Метод получает индекс песни в списке self.my_songs ✓
        return self.my_songs.index(song)
    
    def exit(self) -> None: # Метод завершает программу ✓
        sys.exit()
        
class Song: 
    def __init__(self, name: str, path: str, singer: str, rating: str) -> None:
        self.name = name
        self.singer = singer 
        self.rating = rating
        self.path = path

    def full(self, music: YourMusic) -> str:
        return(f'{music.get_song_index(self) + 1}. "{self.name}" - {self.singer} /{self.path}/ ({self.rating})')
     