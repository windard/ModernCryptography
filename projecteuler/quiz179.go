package main

import "fmt"

func TotalFactors(n int) (pfs []int) {
	var i int
	for i = 1; i*i < n; i++ {
		if n%i == 0 {
			pfs = append(pfs, i)
			pfs = append(pfs, n/i)
		}
	}
	if i*i == n {
		pfs = append(pfs, i)
	}
	return
}

func CalculateTotal(n int) (result []int) {
	var i int
	lastLength := len(TotalFactors(2))
	for i = 3; i < n; i++ {
		currentLength := len(TotalFactors(i))
		if currentLength == lastLength {
			result = append(result, i-1)
		}
		lastLength = currentLength
	}
	return
}

func main() {
	fmt.Printf("[%d]->%#v\n", 15, TotalFactors(15))
	fmt.Printf("[%d]->%#v\n", 16, TotalFactors(16))

	//fmt.Printf("result:%+v\n", result)
	fmt.Printf("result length:%+v\n", len(CalculateTotal(100)))
	fmt.Printf("result length:%+v\n", len(CalculateTotal(10000)))
	//fmt.Printf("result length:%+v\n", len(CalculateTotal(10000000)))
}
