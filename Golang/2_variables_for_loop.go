package main
import "fmt"

func main() {
    for i, j := 1, 11; 
        i <= 10 && j <= 20;
        i, j = i+1, j+1 {
        
        fmt.Println(i, j)
    }
}
