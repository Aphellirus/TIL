package main

import "fmt"

func main() {
  x := 42
  var a int
  var b int

  if x > 18 {
    fmt.Println("Allowed")
    fmt.Scanln(&a)
    if a>0{
        fmt.Scanln(&b)
        if b>0{
            fmt.Println(b*b)
        }
    }
  }
}
