import random

class Generator_song:
    def __init__(self, verse1, verse2, verse3, refrain):
        self.verse1 = verse1
        self.verse2 = verse2
        self.verse3 = verse3
        self.refrain = refrain
        self.refrain_str = 'Припев:\n'
        self.song = 'Сгенерированная песня: \n\n'
    
    def generate_song(self, lines):
        for i in range(self.refrain):
            self.refrain_str += lines[random.randint(0, len(lines) - 1)]
        self.song += self.add_verse(self.verse1, lines)
        self.song += self.add_verse(self.verse2, lines)
        self.song += self.add_verse(self.verse3, lines)
        return self.song

    def add_verse(self, verse, lines):
        verse_str = ''
        for i in range(verse):
            verse_str += lines[random.randint(0, len(lines) - 1)]
        verse_str += '\n' + self.refrain_str + '\n'
        return verse_str
