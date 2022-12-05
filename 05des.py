stacks = [[],["F", "T", "C", "L", "R", "P", "G", "Q"],["N", "Q", "H", "W", "R", "F", "S", "J"],["F", "B", "H", "W", "P", "M", "Q"],["V", "S", "T", "D", "F"],["Q", "L", "D", "W", "V", "F", "Z"],["Z", "C", "L", "S"],["Z", "B", "M", "V", "D", "F"],["T", "J", "B"],["Q", "N", "B", "G", "L", "S", "P", "H"]]
stacks2 = [[],["F", "T", "C", "L", "R", "P", "G", "Q"],["N", "Q", "H", "W", "R", "F", "S", "J"],["F", "B", "H", "W", "P", "M", "Q"],["V", "S", "T", "D", "F"],["Q", "L", "D", "W", "V", "F", "Z"],["Z", "C", "L", "S"],["Z", "B", "M", "V", "D", "F"],["T", "J", "B"],["Q", "N", "B", "G", "L", "S", "P", "H"]]

debugstacks = [[],["Z", "N"],["M", "C", "D"],["P"]]

debugcount = 1
with open("05des.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.split(" ")

        fromstack = int(line[3])
        tostack = int(line[5])
        howmany = int(line [1])

        print("Line", debugcount, ". Move", howmany, "From", fromstack, "to", tostack)

        for move in range(0, howmany):
            crate = stacks[fromstack].pop(-1)
            move = stacks[tostack].append(crate)
        
              
        crates = stacks2[fromstack][-howmany:]
        for crate in crates:
            stacks2[fromstack].pop()
            stacks2[tostack].append(crate)   
        
        debugcount += 1


print("Top stacks with first configuration:", stacks[1][-1], stacks[2][-1], stacks[3][-1], stacks[4][-1], stacks[5][-1], stacks[6][-1], stacks[7][-1], stacks[8][-1], stacks[9][-1])

print("Top stacks with second configuration:",stacks2[1][-1], stacks2[2][-1], stacks2[3][-1], stacks2[4][-1], stacks2[5][-1], stacks2[6][-1], stacks2[7][-1], stacks2[8][-1], stacks2[9][-1])
            




        


