
package Fibonacci;

import java.util.Scanner;

public class fibStore {
    public int fib(int n) {         //Avoids recursion
        if (n==0){
            return 0;
        } 
        else{
    
        int[] fib = new int[n + 1];   //index is storing calculated values
        fib[0] = 0;
        fib[1] = 1;

        for (int i = 2; i <= n; i++) {
            fib[i] = fib[i - 1] + fib[i - 2];
        }

        return fib[n];
    }
    }
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        fibStore fibo = new fibStore();

        System.out.print("Enter the value of n for Fibonacci: ");
        int n = scanner.nextInt();

        if (n < 0) {
            System.out.println("Invalid input. Please enter a non-negative integer.");
        } else {
            int result = fibo.fib(n);
            System.out.println("Fibonacci(" + n + ") = " + result);
        }
    }
}
