function solution(nums) {
    const N = nums.length
    const mySet = new Set(nums)
    return Math.min(N/2, mySet.size)
}