package main

import (
	"fmt"
	"math"
	"slices"
)


func main() {
	l := []int{}
	for s := 0; s <= 100000; s+=2 {
		go func() {
			for i := 1; i <= 100000; i+=2 {
				if i == s {
					continue
				}
				n := math.Pow(2, float64(s)) * math.Pow(3, float64(i))
				if 200_000_000 <= n && n <= 400_000_000 {
					l = append(l, int(n))
				}

			}
		}()
	}
	slices.Sort(l)
	fmt.Println(l)


}
