class Saver:
    def __init__(self) -> None:
        pass
    
    def save_song(self, song):
        file = open('D:/stp2021/labs/lab01/song.txt', 'w', encoding='utf-8')
        file.write(song)
        file.close