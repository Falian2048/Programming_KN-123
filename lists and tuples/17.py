def anagram(first_word, second_word):
    if sorted(first_word) == sorted(second_word):
        return True
    else:
        return False

def main():
    first_word = input("Enter first word: ")
    second_word = input("Enter second word: ")
    print(anagram(first_word, second_word))

if __name__ == "__main__":
    main()
