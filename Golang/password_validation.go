package main

import (
       "fmt"
       "unicode"
       "strings"
       )

func main() {
  var pw string
  fmt.Scanln(&pw)
  str1 := "!@#$%&*"
  a := 0
  b := 0
  c := 0
  for _, l := range pw { 
     a += 1 
          
     if unicode.IsDigit(l) {
         b += 1
     }
     if strings.Contains(str1, string(l))  {
         c += 1
       }
  }            
  if (b > 1 && c > 1 && a > 6)   {    
     fmt.Print("Strong")
     } else {
     fmt.Print("Weak")
    }
}
