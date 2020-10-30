fun main(args: Array<String>) {
    println(grp()) 
}
     fun grp(): String {
     val chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVVWXYZ"
     var password = ""
     for (x in 0..10) {
        password += chars[Math.floor(Math.random() * chars.length).toInt()]
    }
     return password
}
