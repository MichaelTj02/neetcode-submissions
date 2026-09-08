class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            hMap.put(c, hMap.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < t.length(); i++) {
            
            if (!hMap.containsKey(t.charAt(i))) {
                return false;
            }

            else {
                hMap.put(t.charAt(i), hMap.get(t.charAt(i)) - 1);

                if (hMap.get(t.charAt(i)) == 0) {
                    hMap.remove(t.charAt(i));
                }
            }
        }

        return hMap.isEmpty();
    }
}
