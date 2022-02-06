class Solution {
    private int MOD = 1000000007;

    public int numTilings(int n) {
        if(n <= 2) return n;

        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;

        for(int i=4; i<=n; i++) dp[i] = (((dp[i-1]*2) % MOD) + dp[i-3]) % MOD;

        return dp[n];
    }
}