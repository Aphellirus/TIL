package main

import "fmt"

func main() {
	x := []int{48, 96, 86, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 9, 79, 17}
	var min int
	for i, value := range x {
		if i == 0 || min > value {
			min = value
		}
	}
	fmt.Println(min)
}
