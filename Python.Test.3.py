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
