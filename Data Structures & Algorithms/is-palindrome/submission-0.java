class Solution {
    public boolean isPalindrome(String s) {
        String withoutSpace = s;
        
        withoutSpace = withoutSpace.replaceAll("[\\s\\p{Punct}]", "");

        withoutSpace = withoutSpace.toLowerCase();

        String flipped = new StringBuilder(withoutSpace).reverse().toString();

        System.out.println(withoutSpace);
        System.out.println(flipped);

        if (flipped.equals(withoutSpace)) {
            return true;
        }
        return false;
    }
}
