package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := "Tit4Tat"
	str = regexp.MustCompile(`[^a-zA-Z ]+`).ReplaceAllString(str, "")
	fmt.Println(str)
}
