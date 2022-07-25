fun main() {
    data class Point(val x: Int, 
                     val y: Int);
    
    val p = Point(x=0, y=7).also(::println);
    
    val (x, y) = p; // destructuring
    
    when (p) {
      Point(x, y=0) ->
          "On the x axis at $x ."
      
      Point(x=0, y) ->
          "On the y axis at $y ."
      
      else -> "On neither axis: ($x, $y)."
    }.also(::println); // "when" can also be used as an expression which can return some value(here, it is a string), im using "also()" extension method to print that value.
}
