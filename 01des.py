with open ("01des.txt") as file:
    grouplist = []
    elf = []
    for line in file:
        if(line != '\n'):
            line = line.replace("\n", "")
            elf.append(int(line))
        else:
            grouplist.append(elf)
            elf = []

elflist = []

for elf in grouplist:
    sum = 0
    for calories in elf:
        sum = sum + calories
    elflist.append(sum)

elflist.sort()

print("Top elf is carrying", elflist[-1], "calories")

topelves = elflist[-1] + elflist [-2] + elflist[-3]

print("Top three elves are carrying", topelves, "calories combined") 