package main

import "fmt"

func main() { 
    arr1 := []int { 2, 4, 5, 8 }
    arr2 := []int { 3, 8, 9 }
    arr2 = append(arr2, arr1...)
    fmt.Println(arr2)
}
