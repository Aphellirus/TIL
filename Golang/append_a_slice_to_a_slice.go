// appendSliceToSlice method  appends slice y to x 
func appendSliceToSlice() {
	x := []int{1,2,3}
	y := []int{4,5,6}
	x = append(x, y...)
    fmt.Println(x)	// output: [1 2 3 4 5 6]
}
