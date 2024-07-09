func maxArea(height []int) int {
    l,r :=0, len(height)-1
    marea := 0
    h:=0
    for l<r{
        width := r-l
        if height[l] < height[r]{
            h = height[l]
            l++
        } else{
            h = height[r]
            r--
        }
        area := width * h
        if marea < area{
            marea = area
        }
    }
    return marea
}