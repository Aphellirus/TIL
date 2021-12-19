var x interface{} = []int{1, 2, 3}
str1 := fmt.Sprintf("%v", x)
str2 := x.(string)

fmt.Println(str1)
fmt.Println(str2)
