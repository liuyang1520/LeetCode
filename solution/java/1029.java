/*
@difficulty: easy
@tags: greedy
@notes: Sort the differences of costs individually, and always pick up the one with larger diff first.
There is another better greedy way here: https://leetcode.com/problems/two-city-scheduling/discuss/278771/Java-sort-solution
*/
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        List<int[]> diffs = new ArrayList<>();
        for (int i = 0; i < costs.length; i++) {
            diffs.add(new int[]{Math.abs(costs[i][0] - costs[i][1]), i});
        }
        Collections.sort(diffs, (a, b) -> - a[0] + b[0]);
        int total = 0, A = costs.length / 2, B = costs.length / 2;
        for (int i = 0; i < diffs.size(); i++) {
            int index = diffs.get(i)[1];
            if (costs[index][0] > costs[index][1]) {
                if (B > 0) {
                    B--;
                    total += costs[index][1];
                } else {
                    total += costs[index][0];
                }
            } else if (costs[index][0] < costs[index][1]) {
                if (A > 0) {
                    A--;
                    total += costs[index][0];
                } else {
                    total += costs[index][1];
                }
            } else {
                total += costs[index][0];
            }
        }
        return total;
    }
}
