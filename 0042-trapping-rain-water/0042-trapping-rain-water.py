class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = 0
        lmaxheight = height[lmax]
        rmax = len(height) -1
        rmaxheight = height[rmax]
        

        total = 0

        while lmax < rmax:
            if lmaxheight < rmaxheight:
                lmax += 1
                lmaxheight = max(lmaxheight, height[lmax])
                total += max(0, lmaxheight - height[lmax])
            else:
                rmax -= 1
                rmaxheight = max(rmaxheight, height[rmax])
                total += max(0, rmaxheight - height[rmax])

        return total



            
        