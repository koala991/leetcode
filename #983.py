class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days) == 0:
            return 0
        min_cost = {len(days) - 1: min(costs), -1: 0}
        for i in range(len(days) - 2, -1, -1):
            t_cost_1 = costs[0] + min_cost[self.getNextDay(days, i, 1)]
            t_cost_7 = costs[1] + min_cost[self.getNextDay(days, i, 7)]
            t_cost_30 = costs[2] + min_cost[self.getNextDay(days, i, 30)]
            min_cost[i] = min(t_cost_1, t_cost_7, t_cost_30)
        # print(min_cost)
        return min_cost[0]

    def getNextDay(self, days, i, n):
        output = -1
        for j in range(i, len(days)):
            if days[j] - days[i] >= n:
                output = j
                break
        return output