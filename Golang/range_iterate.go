package main

import "fmt"

func main() {
  arr := make([]int, 4)
  arr[1] = 10
  arr[2] = 20

  for i, v := range arr {
    fmt.Println(i, v)
  }
}
