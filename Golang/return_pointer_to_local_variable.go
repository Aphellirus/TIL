package main

import "fmt"

func ret_point() *int {
    myint := 42
    return &myint
}

func main() {
    mypoint := ret_point()
    fmt.Println(*mypoint)
}
