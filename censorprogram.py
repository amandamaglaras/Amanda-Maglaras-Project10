#Amanda Maglaras
#amanda.maglaras1@marist.edu
#censor program

def censors(word):
    for i in range(len(word)):
        if word[i].isalpha():
            word=word[:i] + '*' + word [i+1:]
    return word

def main():
    filesen= input ("File to censor: ")
    origsen= open(filesen, 'r')
    cenwordsf= input ("File containing the censord words: ")
    censored= open(cenwordsf, 'r')
    censoredwords= censored.read().split()

    censortext= ""
    for line in origsen:
        words=line.split()
        for i in range(len(words)):
            word= ""
            for letter in words [i]:
                if letter.isalpha():
                    word+= letter
            if word in censoredwords:
                words[i]= censors(words[i])
        censortext += " ".join(words) + '\n'

    origsen.close()
    censored.close()

    newfile=open("censored.txt", 'w')
    newfile.write(censortext)
    newfile.close()
        
main()
