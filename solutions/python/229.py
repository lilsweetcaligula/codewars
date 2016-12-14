def solution(nums):
    return (nums or []) and sorted(nums)solution = (lambda nums: 
    sorted(nums) if nums else [])