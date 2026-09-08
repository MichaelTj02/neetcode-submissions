class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> numbers = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            numbers.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (numbers.containsKey(diff) && numbers.get(diff) != i) {
                return new int[]{i, numbers.get(diff)};
            }
        }

        return new int[0];

    }
}
