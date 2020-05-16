fun main(args: Array<String>) {
    val daysOfWeek = arrayOf("Sun", "Mon", "Tues", "Wed", "Thur", "Fri", "Sat")
 
    println("Last index: ${daysOfWeek.lastIndex}\n")
    
    for (index in daysOfWeek.indices){
        println("$index: ${daysOfWeek[index]}")
    }
    
    println()
    
    for (index in 1..5) {
        println("$index: ${daysOfWeek[index]}")
    }
    
    println()
    
    for (index in 1 until daysOfWeek.lastIndex) {
        println("$index: ${daysOfWeek[index]}")
    }
    
    println()
    
    for (index in daysOfWeek.lastIndex downTo 0 step 2) {
        println("$index: ${daysOfWeek[index]}")
    }
    
}
