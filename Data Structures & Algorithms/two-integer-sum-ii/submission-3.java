class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // int[] indexes = new int[2];

        // int int1 = 0;
        // int int2 = 0;
        // for (int i = 0; i < numbers.length; i++) {
        //     int1 = numbers[i];
        //     int diff = target - int1;

        //     if (int1 > diff) {
        //         break;
        //     }

        //     for (int j = i + 1; j < numbers.length; j++) {
        //         int2 = numbers[j];

        //         if (int2 == diff) {
        //             indexes[0] = i + 1;
        //             indexes[1] = j + 1;
        //             return indexes;
        //         }

        //         if (int2 > diff) {
        //             break;
        //         }
        //     }
        // }


        // return indexes;

        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            int sum = numbers[left] + numbers[right];

            if (sum == target) {
                return new int[] {left+1, right+1};
            }

            else if (sum > target) {
                right--;
            }

            else left++;
        }

        return new int[0];
    }
}
