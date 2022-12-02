def winorloss(you, opponent):
    match opponent:
        case "A":
            match you:
                case "X":
                    return 3 + 1
                case "Y":
                    return 6 + 2
                case "Z":
                    return 0 + 3
        case "B":
            match you:
                case "X":
                    return 0 + 1
                case "Y":
                    return 3 + 2
                case "Z":
                    return 6 + 3
        case "C":
            match you:
                case "X":
                    return 6 + 1
                case "Y":
                    return 0 + 2
                case "Z":
                    return 3 + 3

def winorlossv2(you, opponent):
    match opponent:
        case "A":
            match you:
                case "X":
                    return 0 + 3
                case "Y":
                    return 3 + 1
                case "Z":
                    return 6 + 2
        case "B":
            match you:
                case "X":
                    return 0 + 1
                case "Y":
                    return 3 + 2
                case "Z":
                    return 6 + 3
        case "C":
            match you:
                case "X":
                    return 0 + 2
                case "Y":
                    return 3 + 3
                case "Z":
                    return 6 + 1

score = 0
scorev2 = 0

with open ("02des.txt") as file:
    for line in file:
        line = line.replace(*"\n", "")   
        values = line.split(" ")
        you = values[1]
        opponent = values[0]        
        score = score + winorloss(you, opponent)
        scorev2 = scorev2 + winorlossv2(you, opponent)

print("Your score with faulty guide:", score )
print("Your score with complete guide:", scorev2)




