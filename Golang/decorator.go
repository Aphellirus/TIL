//code inspired from python(see in the comments)
package main

import (
    "fmt"
    "strings"
)

type Callable func()
strRepeat := strings.Repeat

func Decor(f Callable) Callable { 
    Wrap := func() {
        fmt.Println(strRepeat("=", 12))
        f()
        fmt.Println(strRepeat("=", 12))
    };
    return Wrap
}


func PrintText() {
    fmt.Println("Hello world!")
}


func main() {
    Decorated := Decor(PrintText)
    Decorated()
}
