package main

import (
	"fmt"
	"time"
	"math"
	"math/rand"
)

func addone(x int) int {
    return x + 1
    }

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex


func main() {
    fmt.Println("Go in 5 minutes! By Juan F. Verhook")
    fmt.Println("Go is built using packages, any program will run from the main package")
    fmt.Println("You can use built-in functions from the packages by calling their import path and then the function name")
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("1. Below are some practical examples of built in functions")
    fmt.Println("   To print something you must import fmt from main and then call for Println")
    fmt.Println("   fmt.Println('Hello GCI')")
    fmt.Println("   Hello GCI")
    fmt.Println("")
    fmt.Println("   The same goes for any other package")
    fmt.Println("   time.Now()")
    fmt.Println("  ",time.Now())
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("2. The Go environment is deterministic, once you built something it will stay as it is unless you specify it")
    fmt.Println("   rand.Intn returns a random number from a range that will not change ->", rand.Intn(10))
    rand.Seed( time.Now().UTC().UnixNano())
    fmt.Println("   rand.Seed changes the Seed generator, it will make rand.Intn change ->", rand.Intn(10))
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("3. Exported names are used only with Capital letters math.pi is not the same as math.Pi")
    fmt.Println("   Pi value is", math.Pi)
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("4. Functions in Go can take zero or more arguments, you must specify the type always")
    fmt.Println("   func name(var type) functype { #Dosomething }")
    fmt.Println("   Example function: func addone(x int) int { return x+1}")
    fmt.Println("   addone(5)")  
    fmt.Println(    addone(5))
    fmt.Println("   Note: Functions must be declare outside main() function, nested functions are not allowed")
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("5. Variables are defined using var and can be declared inside and outside functions")
    fmt.Println("   var i, j = 1, 2")
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("6. For loops are interesting, there's no while loop but different ways of using a for!")
    fmt.Println("   for i := 0; i < 3; i++ {  fmt.Println(i)  }")
    for i := 0; i < 3; i++ {  fmt.Println("   ", i)  }
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("7. 'While' loop in Go -> for i  < 5 {fmt.Println(i) i += 1}")
    var i = 0
    for i < 5 {
	fmt.Println("   ", i) 
        i += 1}
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("8. If statements are easy, just input condition and cause inside {} if needed add else at the end")
    fmt.Println("   For example: var x = 2")
    fmt.Println("   if x > 3 { fmt.Println('X is greater than 3') } else {fmt.Println('X is smaller than 2')}")
    var x = 2
    if x > 3 { fmt.Println("X is greater than 3") } else { fmt.Println("X is smaller than 2")}
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("9. Arrays are it's own type in Go! Their length can't be modified! Their INMUTABLE")
    fmt.Println("    To declare an array with three integers: ")
    fmt.Println("    var array [3]int")
    var array [3]int
    fmt.Println("   ", array)
    fmt.Println("   You can use slices instead for better manipulation  sl := []int {2, 5}")
    sl := []int {2, 5}
    fmt.Println("   ", sl)
    fmt.Println("   Too add an item to the slice just append it -> sl = append(sl, 11)")
    sl = append(sl, 11) 
    fmt.Println("   ", sl)
    fmt.Println("--------------------------------------------------------------------------------------------------------")
    fmt.Println("10. Learning maps and saying Go-odbye!")
    fmt.Println("    You can map keys to values, just like Python dictionaries!")
    fmt.Println("    First you will need to create with make before using, see for example ac =  make(map[type]Name")
    m = make(map[string]Vertex)
    fmt.Println("    m = make(map[string]Vertex)")
    fmt.Println("    m['Google Headquarters'] = Vertex{37.423021, -122.083739,}")
    m["Google Headquarters"] = Vertex{37.423021, -122.083739,}
    fmt.Println("    fmt.Println('m[Google Headquarters]')")
    fmt.Println("   ", m["Google Headquarters"])
   
}
