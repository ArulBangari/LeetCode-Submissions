class Solution:
    def punishmentNumber(self, n: int) -> int:
        def checkPunishment(num_str, goal, index, temp_sum):
            # Loop through and create all partitions
            for i in range(1, len(num_str) - index + 1):
                # Haven't added all partitions together yet. Have to call again until reaching end
                if checkPunishment(num_str, goal, index + i, temp_sum + int(num_str[index: index + i])):
                    return True
            # If reached end of number and the sum of partitions is the goal, return True
            if temp_sum == goal and index >= len(num_str):
                return True
            return False

        punishment_sum = 0
        for num in range(1, n + 1):
            num_str_sq = str(num * num)
            # If fulfilling 2nd condition, add to punishment sum
            if checkPunishment(num_str_sq, num, 0, 0):
                punishment_sum += num * num
        return punishment_sum

