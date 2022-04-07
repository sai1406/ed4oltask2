import secrets
from string import printable
 
def makeHarder(word):
    MIN_LEN = 10
    CHARS = printable[:95]
 
    word = list(word)
 
    for index in range(len(word)):
        choice = secrets.choice((0,1,2))
 
        if choice == 1:
            word[index] = word[index].upper()
        elif choice == 2:
            word[index] = secrets.choice(CHARS)
 
 
    while len(word) <= MIN_LEN:
        char = secrets.choice(CHARS) 
        index = secrets.randbelow(len(word))
 
        word.insert(index, char)
 
    return ''.join(word)
 
def genPasswd(seed):
    word = secrets.choice(seed)
    word = makeHarder(word)
 
    return word
 
def main():
    words = input('Enter words: ').split()
    passwd = genPasswd(words)
    print(passwd)
 
 
if __name__ == '__main__':
    main()
 
