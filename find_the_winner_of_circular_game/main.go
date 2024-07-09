func findTheWinner(n int, k int) int {
    winner := 0 
    for i:=2;i<n+1;i++{
        winner = (winner+k)%i
    }
    return winner +1
}