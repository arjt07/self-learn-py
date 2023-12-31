# map Function
def main():
    yell("This", "is", "CS50")
   
# *words -> takes multiple positional Argument 
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()



'''
def main():
    yell("This", "is", "CS50")
    
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    
    print(*uppercased)

if __name__ == "__main__":
    main()
'''


'''
def main():
    yell("This is CS50")
    
def yell(phrase):
    print(phrase.upper())

if __name__ == "__main__":
    main()
'''
