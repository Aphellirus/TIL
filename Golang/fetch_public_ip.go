package main

import (
    "fmt"
    "net/http"
    "log"
    "io/ioutil"
)

func errorHandler(e error){
    if e != nil {
        log.Fatal(e)
    }
}
func whatIsMyIP(){
    resp, err := http.Get("http://ifconfig.me")
    errorHandler(err)
    defer resp.Body.Close()
    ip, err := ioutil.ReadAll(resp.Body)
    errorHandler(err)
    fmt.Printf("SoloLearn Public IP:- %v", string(ip))
    
}
func main() {
    whatIsMyIP()
}
