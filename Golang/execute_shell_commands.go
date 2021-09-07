package main

import (
    "log"
    "os/exec"
)

func main() {
    cmd := exec.Command("ls", "-ahl")
    stdout, err := cmd.Output()
    
    if err != nil {
        log.Println(err.Error())
        panic(err)
    }
    
    log.Println(string(stdout))
}
