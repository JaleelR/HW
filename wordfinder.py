"""Word Finder: finds random words from a dictionary."""
import random
class WordFinder:
   
    def __init__(self, path):
        self.path = path
        self.list_of_words = self.list_of_wordz()
        self.word_lists = self.word_list()


    '''Reads word list, gets the words from file and returns list of words '''
    def word_list(self):
       wordlist = []
       file = open(self.path, "r")
       for line in file:
          wordlist.append(line.rstrip())
          file.close
       return wordlist
      
    '''
    gets the number of lines in file to get the total number count,
    since each line has one word on it 
    '''
    def list_of_wordz(self):
       line_of_words = 0
       file = open(self.path, "r")
       for line in file:
          line_of_words += 1
          file.close
       print(f'{line_of_words} words read')
    
    '''Uses random.choice which will choose a random word from list'''
    def random(self):
     random_word = random.choice(self.word_lists)
     return random_word


 
class RandomWordFinder(WordFinder):
    def __init__(self, path):
       super().__init__(path)
      
   
    '''
    Gets words from file, removes the comments and blank lines
    keeps the other lines 
    '''  
    def comment_lines(self):
       with open(self.path, 'r') as file:
        trash_elements = []
        keep = []
        for line in file:
            if line.startswith("#") or not line:
             trash_elements.append(line)
             
        else:
            keep.append(line.rstrip())
        return keep


        



