const fs = require('fs');

class CPUtoVideo {
    constructor() {
        this.cycle = 1;
        this.Xregister = 1;
        this.input = [];
        this.XregisterSum = 0;
        this.currentPixel = 0;
        this.CRT = [
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]
        ]
        this.output = [];

    }
    addX(value) {
        if(this.testCycle(this.cycle)) {        
                      
        }
        this.draw(this.Xregister, this.cycle)
        this.cycle ++
        if(this.testCycle(this.cycle)) {        
                     
        }
        this.draw(this.Xregister, this.cycle)
        this.cycle++
        this.Xregister += value
    }
    noop() {
        if(this.testCycle(this.cycle)) {            
                       
        }
        this.draw(this.Xregister, this.cycle)
        this.cycle++
    }
    draw(xregister, cycle) {
        let cursorStart = xregister - 1;
        let cursorStop = xregister + 1;
         if (cycle <= 40) {
            console.log("Start: " + cursorStart + " Stop: " + cursorStop + " Current pixel: " + this.currentPixel)

            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[0][this.currentPixel] = "#";
            }
            this.currentPixel++
         } else if(cycle <= 80) {
            if (this.currentPixel > 39) {
                this.currentPixel = 0
            }
            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[1][this.currentPixel] = "#";
            }
            this.currentPixel++            
         } else if(cycle <= 120) {
            if (this.currentPixel > 39) {
                this.currentPixel = 0
            }
            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[2][this.currentPixel] = "#";
            }
            this.currentPixel++            
         } else if(cycle <= 160) {
            if (this.currentPixel > 39) {
                this.currentPixel = 0
            }
            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[3][this.currentPixel] = "#";
            }
            this.currentPixel++            
         } else if(cycle <= 200) {
            if (this.currentPixel > 39) {
                this.currentPixel = 0
            }
            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[4][this.currentPixel] = "#";
            }
            this.currentPixel++            
         } else if(cycle <= 240) {
            if (this.currentPixel > 39) {
                this.currentPixel = 0
            }
            if (this.currentPixel >= cursorStart && this.currentPixel <= cursorStop) {
                this.CRT[5][this.currentPixel] = "#";
            }
            this.currentPixel++            
         }
    }
    readInput() {
        let input = fs.readFileSync('10des.txt', 'utf8').split(/\r?\n/);
        for (let line of input) {
            line = line.split(" ")
            this.input.push(line)
        }
    }
    testCycle(cycle) {
        if(cycle == 20 || cycle == 60 || cycle == 100 || cycle == 140 || cycle == 180 || cycle == 220) {
            let signalStrength = cycle * this.Xregister
            console.log("Cycle " + this.cycle + ". X-register at: "  + this.Xregister)
            console.log("Signal strength: " + signalStrength)
            this.XregisterSum += signalStrength
            console.log("X-register sum at " + this.cycle + " cycles: " + this.XregisterSum)
            return true
        } else {
            return false
        }
    }
    print() {
        for (let line of this.CRT) {
            line = line.join("");
            this.output.push(line)
            console.log(line)
        }
    }
    run() {
        for (let line of this.input) {
            if (line[0] === "noop") {
                this.noop()
            } else {
                this.addX(Number(line[1]))
            }
        }
    }
}

let elfMachine = new CPUtoVideo();
elfMachine.readInput()
elfMachine.run()
elfMachine.print()





