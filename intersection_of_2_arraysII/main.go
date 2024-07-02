func intersect(nums1 []int, nums2 []int) []int {
    countMap := make(map[int]int)
    for _, num := range nums1 {
        countMap[num]++
    }
    
    result := []int{}
    
    for _, num := range nums2 {
        if count, found := countMap[num]; found && count > 0 {
            result = append(result, num)
            countMap[num]-- 
        }
    }

    return result
}