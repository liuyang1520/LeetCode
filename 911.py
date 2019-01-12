"""
Caculate the leading person for each given timestamp.
Then do a linear search (1) or a binary search (2) on the results with given t.
"""
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        lastPerson, lastVote = -1, -1
        votes, self.stats = {}, []
        for i, time in zip(persons, times):
            votes[i] = votes.get(i, 0) + 1
            if votes[i] >= lastVote:
                lastPerson, lastVote = i, votes[i]
                self.stats.append([time, i])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t >= self.stats[-1][0]: return self.stats[-1][1]
        last = self.stats[0][1]
        for time, i in self.stats:
            if t < time:
                return last
            last = i


class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        lastPerson, lastVote = -1, -1
        votes, self.stats = {}, []
        for i, time in zip(persons, times):
            votes[i] = votes.get(i, 0) + 1
            if votes[i] >= lastVote:
                lastPerson, lastVote = i, votes[i]
                self.stats.append([time, i])

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        if t >= self.stats[-1][0]: return self.stats[-1][1]
        i = bisect.bisect(self.stats, [t, float('inf')], 1)
        return self.stats[i-1][1]
