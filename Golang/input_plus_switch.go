package main

import "fmt"

func main() {

 var input int
 fmt.Scanln(&input)
  
 switch {
    case input>0 && input<10:
      fmt.Println("From 0 to 10")
    case input > 10:
      fmt.Println("Greater than 10")
  }
}
