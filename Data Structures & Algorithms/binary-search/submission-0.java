class Solution {
    public int search(int[] nums, int target) {
        int high = nums.length - 1;
        int low = 0;
        int mid = 0;

        while (low <= high) {

            mid = (low+high) / 2;

            if (nums[mid] == target) return mid;

            if (nums[mid] < target) {
                low = mid + 1;
            }

            else if (nums[mid] > target) {
                high = mid - 1;
            }
        }

    return -1;

    }
}
