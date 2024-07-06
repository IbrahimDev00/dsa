func passThePillow(n int, time int) int {
    cycleLength := 2 * (n - 1)
    time = time % cycleLength

    if time < n {
        return time + 1
    } else {
        return 2*n - time - 1
    }
}
