package main

import (
"fmt"
"sort"
)

var pln = fmt.Println 
func main() {
    Numbers :=[]int {3,6,5,8,9,3,7,1,1,2,7,10,4}
    sort.Ints(Numbers )
    pln(Numbers )
    
    
    
}
