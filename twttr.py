def main():
    word = input("Input: ")
    print ("Output:",shorten(word))

def shorten(word):
    for patskanis in 'auioeAUIOE':
        word = word.replace(patskanis, '')
    return word

if __name__ == "__main__":
    main()