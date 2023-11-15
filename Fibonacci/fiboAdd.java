package Fibonacci;

public class fiboAdd {

    public int fib(int n) {
        if (n <= 1) {
            return n;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }

    public static void main(String[] args) {
        fiboAdd fib = new fiboAdd();

        // Test cases
        int[][] testCases = {
            {0, 0},
            {1, 1},
            {2, 1},
            {3, 2},
            {4, 3},
            {5, 5},
            {6, 8},
            {7, 13},
            {8, 21},
            {9, 34},
            {10, 55},
        };

        // Run test cases
        for (int[] testCase : testCases) {
            int expected = testCase[1];
            int actual = fib.fib(testCase[0]);

            if (expected != actual) {
                System.out.println("Test case failed: fib(" + testCase[0] + ") expected " + expected + ", but got " + actual);
            } else {
                System.out.println("Test case passed: fib(" + testCase[0] + ") = " + actual);
            }
        }
    }
}
