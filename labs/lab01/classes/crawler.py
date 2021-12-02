import os

class Crawler:

    def __init__(self,dir):
        self.dir = 'D:/stp2021/labs/lab01/' + dir
        self.files = os.listdir(dir)
        self.lines = []

    def crawl_song(self):
        for file in self.files:
            temp = open(self.dir + '/' + file,'r', encoding='utf-8')
            for line in temp:
                self.lines.append(line)
            temp.close
        return self.lines