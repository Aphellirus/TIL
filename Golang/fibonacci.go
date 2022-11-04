package main

import "fmt"

func main() {
     var a []int
     f := 1
     ib := 0
     fibonacci := 0
     fmt.Printf("My fibonacci in Golang\n\n")
     var n int
     fmt.Scanf("%d", &n)
for i := 0; i < n; i++ { 
        fmt.Printf("%d\n",fibonacci)
        a = append(a,fibonacci)
        fibonacci = f + ib
        f = ib
        ib = fibonacci
        }
        fmt.Println("\n\nfibonacci sequence in array\t\t\t\t\t\tseq=",a)
}
