const Phi = 1.618

// single constant
const (
  A = "A"
  B = "B"
)

// multiple constant
const (
  A, B = "A", "B"
  Monday, Sunday = "Monday", "Sunday"
)

const lightSpeed = 299792458 // initial value

// Error! Constants cannot be changed
lightSpeed = 299792460
