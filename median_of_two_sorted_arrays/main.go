import "sort"
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    s := append(nums1, nums2...)
    sort.Ints(s)
    l := len(s)
    if l%2 == 0{
        return float64(s[l/2-1]+s[l/2]) / 2.0
    } else{
        return float64(s[l/2])
    }
}
