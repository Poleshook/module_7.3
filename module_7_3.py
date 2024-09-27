import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                file = file.read().lower()
                for i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(i, '')
                words = file.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        dictionary_find = {}
        for i, words in self.get_all_words().items():
            for j, word_ in enumerate(words, 1):
                if word_ == word.lower():
                    dictionary_find[i] = j
                    break
        return dictionary_find

    def count(self, word):
        dictionary_count = {}
        for i, words in self.get_all_words().items():
            dictionary_count[i] = words.count(word.lower())
        return dictionary_count


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))