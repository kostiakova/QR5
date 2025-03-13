package main

import (
    "fmt"
    "strconv"
)

const EX__STR = "Wie heist du? This is problem! ce n'est pas le problem pour moi|"

var dictColors = map[int]string{0: "⚫", 1: "⚪", 2: "🟥", 3: "🟩", 4: "🟦"}
var reversedColors = map[string]int{"⚫": 0, "⚪": 1, "🟥": 2, "🟩": 3, "🟦": 4}

func strToList(src string) []rune {
    return []rune(src)
}

func lstToStr(src []rune) string {
    return string(src)
}

func decToQuin(decimal int) int {
    res := ""
    for decimal >= 1 {
        res = strconv.Itoa(decimal%5) + res
        decimal /= 5
    }
    quinary, _ := strconv.Atoi(res)
    return quinary
}

func quinToDec(num int) int {
    decimalValue := 0
    base := 1
    for num > 0 {
        lastDigit := num % 10
        num /= 10
        decimalValue += lastDigit * base
        base *= 5
    }
    return decimalValue
}

func getUTFCode(s string) []int {
    lst := strToList(s)
    retS := make([]int, len(lst))
    for i, r := range lst {
        retS[i] = int(r)
    }
    return retS
}

func getCharFromCode(codees []int) string {
    runes := make([]rune, len(codees))
    for i, code := range codees {
        runes[i] = rune(code)
    }
    return lstToStr(runes)
}

func listQuinary(list []int) []int {
    quinary := make([]int, len(list))
    for i, v := range list {
        quinary[i] = decToQuin(v)
    }
    return quinary
}

func listDecimal(listQ []int) []int {
    decimal := make([]int, len(listQ))
    for i, v := range listQ {
        decimal[i] = quinToDec(v)
    }
    return decimal
}

func quinToColor(src []int) []string {
    r := make([]string, len(src))
    for i, el := range src {
        s := strconv.Itoa(el)
        t := ""
        for _, char := range s {
            t += dictColors[int(char-'0')]
        }
        r[i] = t
    }
    return r
}

func colorToQuin(src []string) []int {
    r := make([]int, len(src))
    for i, el := range src {
        t := ""
        for _, char := range el {
            t += strconv.Itoa(reversedColors[string(char)])
        }
        r[i], _ = strconv.Atoi(t)
    }
    return r
}

func strToQuin(src string) []int {
    return listQuinary(getUTFCode(src))
}

func strToColored(src string) []string {
    return quinToColor(listQuinary(getUTFCode(src)))
}

func coloredToStr(src []string) string {
    return getCharFromCode(listDecimal(colorToQuin(src)))
}

func main() {
    // EXAMPLE:
    // quin := listQuinary(getUTFCode(EX__STR))
    // colors := quinToColor(quin)
    // quin = colorToQuin(colors)
    // dec := listDecimal(quin)
    // strr := getCharFromCode(dec)
    fmt.Println(strToQuin(EX__STR))
    fmt.Println(strToColored(EX__STR))
    fmt.Println(coloredToStr([]string{"🟥🟦🟥", "🟦⚫⚪", "🟦⚪🟩", "🟦⚪🟩", "🟦🟥⚪", "⚪⚪🟥", "⚪🟦🟦", "🟩🟩⚫"}))
}