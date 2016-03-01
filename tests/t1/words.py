# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
wordlist=[]
print("Keep on entering words. Enter quit to finish. Empty inputs are ignored ")
while True:
    text = input("")
    if text != "quit":
        if text.strip(" "):
            #If text is empty, its excluded
            wordlist.append(text)
    else:
        print(" ".join(sorted(wordlist)))
        break
