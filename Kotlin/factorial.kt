fun main(args: Array<String>) {

	val n = readLine()!!.toInt()

    var result = 1

    for(i in 2..n) {
        result *= i
    }
    
    println("The factorial of $n is: $result")
}
