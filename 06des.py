with open("06des.txt") as file:
    for line in file:
        scrambleddata = line.replace("\n", "")
        

counter = 4

while (counter < len(scrambleddata)):
    lastfour = [scrambleddata[counter -3], scrambleddata[counter -2], scrambleddata[counter -1], scrambleddata[counter -0]]   

    successcounter = 0
    for letter in lastfour:
        if (lastfour.count(letter) == 1):
            successcounter += 1
        else:
            break
    
    if (successcounter == 4):
        print("Four different letters found at pos: ", counter + 1)
        break

    counter += 1

messagecounter = 14

while (messagecounter < len(scrambleddata)):
    lastfourteen = [scrambleddata[messagecounter -13], scrambleddata[messagecounter -12], scrambleddata[messagecounter -11], scrambleddata[messagecounter -10], scrambleddata[messagecounter -9], scrambleddata[messagecounter -8], scrambleddata[messagecounter -7], scrambleddata[messagecounter -6], scrambleddata[messagecounter -5], scrambleddata[messagecounter -4], scrambleddata[messagecounter -3], scrambleddata[messagecounter -2], scrambleddata[messagecounter -1], scrambleddata[messagecounter -0]]   

    messagesuccesscounter = 0
    for letter in lastfourteen:
        if (lastfourteen.count(letter) == 1):
            messagesuccesscounter += 1
        else:
            break
    
    if (messagesuccesscounter == 14):
        print("Fourteen different letters found at pos: ", messagecounter + 1)
        break

    messagecounter += 1