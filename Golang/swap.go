package main

import "fmt"

func main() {
    a := 5
    b := 8
    // ~~~OR~~~ 
    // a, b := 5, 8
    
    a, b = b, a // swapping
    
    fmt.Printf("a = %d, b = %d", a, b) 
}
