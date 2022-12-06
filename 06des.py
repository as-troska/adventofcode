with open("06des.txt") as file:
    for line in file:
        scrambleddata = line.replace("\n", "")


counter = 4


while (counter < len(scrambleddata)):
    lastfour = scrambleddata[counter-4:counter]    

    successcounter = 0
    for letter in lastfour:
        if (lastfour.count(letter) == 1):
            successcounter += 1
        else:
            break
    
    if (successcounter == 4):
        print("Four different letters found at pos: ", counter)
        break

    counter += 1

messagecounter = 14

while (messagecounter < len(scrambleddata)):
    lastfourteen = scrambleddata[messagecounter-14:messagecounter]   

    messagesuccesscounter = 0
    for letter in lastfourteen:
        if (lastfourteen.count(letter) == 1):
            messagesuccesscounter += 1
        else:
            break
    
    if (messagesuccesscounter == 14):
        print("Fourteen different letters found at pos: ", messagecounter)
        break

    messagecounter += 1