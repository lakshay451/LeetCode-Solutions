# Time:  O(nlogn + n * k)
# Space: O(n * k)

import bisect


class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort(key=lambda x: x[1])
        sorted_ends = [x[1] for x in events]
        prv = [bisect.bisect_left(sorted_ends, event[0])-1 for event in events]
        dp = [[0]*(k+1) for _ in xrange(len(events)+1)]
        for i in xrange(1, len(events)+1):
            for j in xrange(1, k+1):
                dp[i][j] = max(dp[i-1][j], dp[prv[i-1]+1][j-1]+events[i-1][2])
        return dp[-1][-1]


# Time:  O(nlogn + n * k)
# Space: O(n * k)
import bisect


class Solution2(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort()
        sorted_starts = [x[0] for x in events]
        nxt = [bisect.bisect_right(sorted_starts, event[1])-1 for event in events]
        dp = [[0]*(k+1) for _ in xrange(len(events)+1)]
        for i in reversed(xrange(len(events))):
            for j in xrange(1, k+1):
                dp[i][j] = max(dp[i+1][j], dp[nxt[i]+1][j-1]+events[i][2])
        return dp[0][-1]
