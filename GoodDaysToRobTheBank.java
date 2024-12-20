/*
Problem - 2100 Find Good Days To Rob the Bank
Link - https://leetcode.com/problems/find-good-days-to-rob-the-bank/
*/

class Solution {
    public List<Integer> goodDaysToRobBank(int[] security, int time) {
        // store length of non-increase seq leading to i-th element
        int[] nonIncrease = new int[security.length];
        for (int i = 1; i < security.length - time; i++) {
            if (security[i-1] < security[i])
                nonIncrease[i] = 0;
            else
                nonIncrease[i] = nonIncrease[i-1] + 1;
        }

        // same for nonDecrease
        int[] nonDecrease = new int[security.length];
        for (int i = security.length - 2; i >= time; i--) {
            if (security[i+1] < security[i])
                nonDecrease[i] = 0;
            else
                nonDecrease[i] = nonDecrease[i+1] + 1;
        }

        ArrayList<Integer> result = new ArrayList<>();
        for (int i = time; i < security.length - time; i++) {
            if (nonIncrease[i] >= time && nonDecrease[i] >= time)
                result.add(i);
        }
        return result;
    }
}
