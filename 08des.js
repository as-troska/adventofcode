const fs = require('fs');

const data = fs.readFileSync('08des.txt', 'utf8').split(/\r?\n/);

class Tree {
    constructor(tree, x, y) {
        this.height = Number(tree);
        this.posX = x;
        this.posY = y;
    }

    isVisible() {
        let visibleNorth = false;
        let visibleWest = false;
        let visibleSouth = false;
        let visibleEast = false;

        // Check for borders
        if (this.posX === 0 || this.posX === 98 || this.posY === 0 || this.posY === 98) {
            return true
        }

        // Check south
        for (let i = this.posX + 1; i < forest.length; i++) {
            if (forest[i][this.posY].height < this.height) {
                visibleSouth = true;
            } else if (forest[i][this.posY].height >= this.height) {
                visibleSouth = false;
                break
            }
        }

        // Check north
        for (let i = this.posX - 1; i > -1; i--) {
            if (forest[i][this.posY].height < this.height) {
                visibleNorth = true;
            } else if (forest[i][this.posY].height >= this.height) {
                visibleNorth = false;
                break
            }
        }

        // Check east
        for (let i = this.posY + 1; i < forest[this.posY].length; i++) {
            if (forest[this.posX][i].height < this.height) {
                visibleEast = true;
            } else if (forest[this.posX][i].height >= this.height) {
                visibleEast = false;
                break
            }
        }

        // Check west
        for (let i = this.posY - 1; i > -1; i--) {
            if (forest[this.posX][i].height < this.height) {
                visibleWest = true;
            } else if (forest[this.posX][i].height >= this.height) {
                visibleWest = false;
                break
            }
        }

        if (visibleEast || visibleNorth || visibleSouth || visibleWest ) {
            return true
        } else {
            return false
        }        
    }

    getScenicScore() {
        let S = 0
        let N = 0
        let E = 0
        let W = 0

        // Check south
        for (let i = this.posX + 1; i < forest.length; i++) {
            if (forest[i][this.posY].height < this.height) {
                S++
            } else if (forest[i][this.posY].height >= this.height) {
                S++
                break
            }
        }

        // Check north
        for (let i = this.posX - 1; i > -1; i--) {
            if (forest[i][this.posY].height < this.height) {
                N++
            } else if (forest[i][this.posY].height >= this.height) {
                N++
                break
            }
        }

        // Check east
        for (let i = this.posY + 1; i < forest[this.posY].length; i++) {
            if (forest[this.posX][i].height < this.height) {
                E++
            } else if (forest[this.posX][i].height >= this.height) {
                E++
                break
            }
        }

        // Check west
        for (let i = this.posY - 1; i > -1; i--) {
            if (forest[this.posX][i].height < this.height) {
                W++
            } else if (forest[this.posX][i].height >= this.height) {
                W++
                break
            }
        }

        let scenicScore = W * E * N * S;        
        
        return scenicScore
    }
}

let forest = [];

let x = 0;
let y = 0;

for (let line of data) {
    let row = [];
    for (let number in line) {
        row.push(new Tree(line[number], x, y))
        y++
    }
    forest.push(row)
    x++
    y = 0
}

counter = 0
scenicScores = []

for(let row of forest) {
    for (let tree of row) {
        if(tree.isVisible()) {
            counter++
        }
        scenicScores.push(tree.getScenicScore())
    }
}

scenicScores.sort(function(a, b) {
    return a - b;
  })
scenicScores.reverse()



console.log("Number of trees visible: " + counter)
console.log("Largest scenic score: " + scenicScores[0])


