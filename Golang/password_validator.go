package main

import (
    "fmt"
)

func get_password() string {
    fmt.Println("Enter Password: ")
    var password string
    fmt.Scanln(&password)
    return password
}

func check_length(password string) bool {
    if len(password) >= 7 {
        return true
    } else {
        return false
    }
}

func check_characters(password string) bool {
    var counter int = 0
    var schars = [...]string{"!", "@", "#", "$", "%", "&", "*"}
    for _, c := range schars {
        for _, i := range password {
            if string(c) == string(i) {
                counter += 1
            }
        }
    }
    if counter >= 2 {
        return true
    } else {
        return false
    }
}

func verify_numbers(password string) bool {
    var counter int = 0
    var numbers = [...]string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    for _, n := range numbers {
        for _, i := range password {
            if string(n) == string(i) {
                counter += 1
            }
        }
    }
    if counter >= 2 {
        return true
    } else {
        return false
    }
}

func check_password(array [3]bool) bool {
    for _, b := range array {
        if b == true {
            continue
        } else {
            return false
        }
    }
    return true
}

func main() {
    var password = get_password()
    var flags = [...]bool{check_length(password), check_characters(password), verify_numbers(password)}
    var valid = check_password(flags)
    if valid == true {
        fmt.Println("Strong")
    } else {
        fmt.Println("Weak")
    }
}
