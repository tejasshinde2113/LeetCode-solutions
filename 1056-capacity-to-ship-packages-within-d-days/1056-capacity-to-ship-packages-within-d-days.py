class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        arr = [max(weights), sum(weights)]

        def check(mid):
            cnt = 1
            temp = 0
            for i, a in enumerate(weights):

                if temp + a <= mid:
                    temp += a
                else:
                    temp = a
                    cnt += 1

            if cnt <= days:

                return True
            return False

        mid = None

        res = sum(weights)
        while arr[0] <= arr[1]:
            mid = arr[0] + (arr[1] - arr[0]) // 2

            if check(mid):

                arr[1] = mid - 1

                res = min(res, mid)
            else:
                arr[0] = mid + 1

        return res
