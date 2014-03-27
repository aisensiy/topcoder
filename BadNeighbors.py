class BadNeighbors:
    def maxDonations(self, ary):
        a = self.dpalg(ary)
        b = self.dpalg(ary[::-1])
        return max(a, b)

    def dpalg(self, ary):
        n = len(ary)
        if n == 0: return 0
        if n == 1: return ary[0]

        dp = list(ary[:])

        zeroin = [False] * n
        zeroin[0] = True

        dp[1] = max(dp[0], dp[1])
        if ary[1] != ary[0] and dp[1] == ary[0]:
            zeroin[1] = True

        for i in range(2, n):
            if (i != n - 1 or (i == n - 1 and not zeroin[i - 2]))\
            and ary[i] + dp[i - 2] > dp[i - 1]:
                dp[i] = ary[i] + dp[i - 2]
                zeroin[i] = zeroin[i - 2]
            else:
                dp[i] = dp[i - 1]
                zeroin[i] = zeroin[i - 1]

        return dp[-1]


if __name__ == '__main__':
    bd = BadNeighbors()
    print bd.maxDonations((10, 3, 2, 5, 7, 8))
    print bd.maxDonations([11, 15])
    print bd.maxDonations([7, 7, 7, 7, 7, 7, 7])
    print bd.maxDonations([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
    print bd.maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6,
        237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81,
        45, 435, 7, 36, 57, 86, 81, 72])
