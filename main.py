def kbig(nums, k):
    if k==1:
        return max(nums)
    m = nums[0]
    n1=max(nums)
    nums.remove(n1)

    for j in range(0, len(nums)):

        for i in range(0, len(nums)):

            if abs(n1 - nums[i]) < m:
                m = abs(n1 - nums[i])
                el = nums[i]

        m=nums[0]

        n1 = el
        nums.remove(n1)

        if j+2 == k:
            return n1
