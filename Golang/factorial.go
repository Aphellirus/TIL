package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.Replace(input, "\r\n", "", -1)
	userInput, _ := strconv.ParseUint(input, 10, 64)
	factorials := factorial(userInput)
	result := fmt.Sprintf("You entered %v and the factorial is %v.", input, factorials)
	fmt.Println(result)
}

func factorial(x uint64) uint64 {
	if x == 0 {
		return 1
	}
	return x * factorial(x-1)
