func main() {
    Publish("A goroutine starts a new thread.", 5*time.Second)
    fmt.Println("Let’s hope the news will be published before I leave.")

    // Wait for the news to be published.
    time.Sleep(10 * time.Second)

    fmt.Println("Ten seconds later: I’m leaving now.")
}
