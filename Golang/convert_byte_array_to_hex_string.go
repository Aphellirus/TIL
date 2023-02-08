import (
	"fmt"
	"crypto/sha1"
  "encoding/hex"
)

func MakeHash(val string) {
	// val = foo
	hash := sha1.New()
	hash.Write([]byte(val))
    hashstr := hex.EncodeToString(hash.Sum(nil))
    
    fmt.Println(hashstr) // prints 0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33
}
