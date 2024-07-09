func averageWaitingTime(customers [][]int) float64 {
    var totalWaitTime int
    var currentTime int

    for _, customer := range customers {
        arrivalTime, orderTime := customer[0], customer[1]

        if currentTime < arrivalTime {
            currentTime = arrivalTime
        }
        waitTime := (currentTime + orderTime) - arrivalTime
        totalWaitTime += waitTime
        currentTime += orderTime
    }

    return float64(totalWaitTime) / float64(len(customers))
}
