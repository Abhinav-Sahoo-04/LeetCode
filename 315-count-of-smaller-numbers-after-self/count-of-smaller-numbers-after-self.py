class Solution:
    def countSmaller(self, nums):
        n = len(nums)
        ans = [0] * n
        arr = [(nums[i], i) for i in range(n)]

        def mergeSort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)

            temp = []
            i = left
            j = mid + 1
            smaller = 0

            while i <= mid and j <= right:

                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    smaller += 1
                    j += 1

                else:
                    ans[arr[i][1]] += smaller
                    temp.append(arr[i])
                    i += 1

            while i <= mid:
                ans[arr[i][1]] += smaller
                temp.append(arr[i])
                i += 1

            while j <= right:
                temp.append(arr[j])
                j += 1

            arr[left:right + 1] = temp

        mergeSort(0, n - 1)

        return ans