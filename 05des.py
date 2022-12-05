# stacks = [[],["F", "T", "C", "L", "R", "P", "G", "Q"],["N", "Q", "H", "W", "R", "F", "S", "J"],["F", "B", "H", "W", "P", "M", "Q"],["V", "S", "T", "D", "F"],["Q", "L", "D", "W", "V", "F", "Z"],["Z", "C", "L", "S"],["Z", "B", "M", "V", "D", "F"],["T", "J", "B"],["Q", "N", "B", "G", "L", "S", "P", "H"]]
stacks = [[],["N", "Z"],["D", "C", "M"],["P"]]

debugcount = 1
with open("05des.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split(" ")

        fromstack = line[3]
        tostack = line[5]
        howmany = line [1]

        print("Line", debugcount, ". Move", howmany, "From", fromstack, "to", tostack)

        for move in range(1, int(howmany)):
            crate = stacks[int(fromstack)].pop(-1)
            move = stacks[int(tostack)].append(crate)
            
        debugcount += 1


print(stacks[1][-1], stacks[2][-1], stacks[3][-1])
#  stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1], stacks[9][-1])
            




        


