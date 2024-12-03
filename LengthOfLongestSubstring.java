/*
Problem - 3 Longest Substring Without Repeating Characters
Link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0)
            return 0;
        if (s.length() == 1)
            return 1;

        int maxLength = 0;
        int left = 0, right = 1;
        HashSet<Character> hist = new HashSet<>();
        hist.add(s.charAt(0));

        while (left < s.length() && right < s.length()) {

            // push left to reach to a legal substring
            while (hist.contains(s.charAt(right))) {
                hist.remove(s.charAt(left));
                left++;
            }

            // add the right char to the substring since its legal now
            hist.add(s.charAt(right));
            right++;

            if (hist.size() > maxLength)
                maxLength = hist.size();
        }
        return maxLength;
    }
}
