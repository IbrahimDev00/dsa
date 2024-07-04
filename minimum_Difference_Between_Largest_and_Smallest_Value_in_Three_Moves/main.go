import(
    "math"
    "sort"
)
func minDifference(nums []int) int {
	if len(nums) <= 4 {
		return 0
	}

	sort.Ints(nums)

	ans := nums[len(nums)-1] - nums[0] 
	for i := 0; i < 4; i++ {
		ans = int(math.Min(float64(ans), float64(nums[len(nums)-(4-i)]-nums[i])))
	}
	return ans
}