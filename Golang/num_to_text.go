package main

import "fmt"

func numText(num int) string {
    var text string
    
    switch num {
        case 0:
        text = "Zero"
        
        case 1:
        text = "One"
        
        case 2:
        text = "Two"
        
        case 3:
        text = "Three"
        
        case 4:
        text = "Four"
        
        case 5:
        text = "Five"
        
        case 6:
        text = "Six"
        
        case 7:
        text = "Seven"
        
        case 8:
        text = "Eight"
        
        case 9:
        text = "Nine"
    }
    
    return text
}

func main() {
    var firstNum int
    fmt.Scanln(&firstNum)
    fmt.Println(numText(firstNum))
    
    var secondNum int
    fmt.Scanln(&secondNum)
    fmt.Println(numText(secondNum))
    
    var thirdNum int
    fmt.Scanln(&thirdNum)
    fmt.Print(numText(thirdNum))
}
