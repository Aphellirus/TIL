package main
import "fmt"

func subtract(x, y int) int {
  return x-y
}

func main() {
  result := subtract(21, 11)
  fmt.Println(result)
}
