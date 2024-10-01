class Solution {
    public boolean canArrange(int[] arr, int k) {
        
        int[] remainderFreq = new int[k];
        
        for (int num : arr) {
            int remainder = (num % k + k) % k; 
            remainderFreq[remainder]++;
        }
        
        for (int i = 0; i <= k / 2; i++) {
            if (i == 0) {
                if (remainderFreq[i] % 2 != 0) return false;
            } else {
                if (remainderFreq[i] != remainderFreq[k - i]) return false;
            }
        }
        
        return true;
    }
}