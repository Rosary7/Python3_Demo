"""
 Python - Inner classs
"""
class Language:
    def __init__(self):
        self.language_name = 'English'
        self.grammar = self.EnglishGrammar()

    class EnglishGrammar:
        def verb(self):
            return 'A word is used to describe an action or state,'


if __name__ == '__main__':
    language = Language()
    print(language.language_name)
    print(language.grammar.verb())