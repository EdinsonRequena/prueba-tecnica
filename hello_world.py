first_word, second_word = 'Hola, ', 'Mundo!'

def hello(first_word, second_word):
    '''
    :type first_word: str
    :type second_word: str
    :rtype both: str
    '''
    both = first_word + second_word
    print(both)

def main():
    hello(first_word, second_word)

if __name__ == "__main__":
    main()

