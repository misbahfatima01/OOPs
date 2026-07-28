from word_counter import WordProcessor

def main():
    text = input("Enter words separated bt spaces: ")
    wp = WordProcessor(text)
    wp.display()

if __name__ == "__main__":
    main()
