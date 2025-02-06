class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        wild_west = list(s)
        moves = 0
        while wild_west:
            # index of first char that matches the last char
            matching_end = wild_west.index(wild_west[-1])
            # if end is the only one of its kind move it to centre
            if matching_end == len(wild_west) - 1:
                moves_to_middle = matching_end // 2
                moves += matching_end // 2
            else:
                # move first match of end to the start
                moves += matching_end
                # remove the first match
                wild_west.pop(matching_end)
                
            # remove the end of the list 
            wild_west.pop()

        return moves
