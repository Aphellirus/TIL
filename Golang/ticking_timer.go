package main

import "fmt"

type Timer struct {
  id string
  value int
}

func (ptr *Timer) tick() {
  ptr.value += 1
}
var i=0
func main() {
  t := Timer{"timer1", 0}
  var x int
  fmt.Scanln(&x)
  for i=0; i<x; i++ {
  t.tick()
  fmt.Println(t.value)
  }
}
