/*program to calculate the volume of a cylinder*/
package main

import "fmt"

func main() {
    var area,volume,radius,length float64
     const pi=3.14
     fmt.Println("Enter radius:")
     fmt.Scanln(&radius)
     area=pi*radius*radius
     fmt.Println("Enter Length:")
     fmt.Scanln(&length)
     volume=area*length /*formula to calculate the volume of a cylinder*/
   
    fmt.Println(volume)
}
