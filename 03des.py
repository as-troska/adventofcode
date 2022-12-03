prioritysum = 0

with open ("03des.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        splitat = int(len(line) / 2)
        firstcompartment, secondcompartment = line[:splitat], line[splitat:]

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for letter in alphabet:
            if (letter in firstcompartment and letter in secondcompartment): 
                priority = alphabet.find(letter) + 1                
            elif (letter.upper() in firstcompartment and letter.upper() in secondcompartment):
                priority = alphabet.find(letter) + 27                
        
        prioritysum = prioritysum + priority

print("Sum of priorites of all backpacks:", prioritysum)

with open ("03des.txt") as file:
    prioritysumv2 = 0

    backpacks = []
    for line in file:
        backpacks.append(line)
    
    counter = 0
    while (counter < len(backpacks)):
        firstbackpack = backpacks[counter]
        secondbackpack = backpacks[counter + 1]
        thirdbackpack = backpacks[counter + 2]

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        for letter in alphabet:
            if (letter in firstbackpack and letter in secondbackpack and letter in thirdbackpack):
                priority = alphabet.find(letter) + 1
            elif (letter.upper() in firstbackpack and letter.upper() in secondbackpack and letter.upper() in thirdbackpack):
                priority = alphabet.find(letter) + 27

        prioritysumv2 = prioritysumv2 + priority              

        counter = counter + 3


print("Sum of priorities for all backpack-groups:", prioritysumv2)