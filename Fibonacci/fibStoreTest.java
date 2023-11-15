package Fibonacci;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class fibStoreTest {
    @Test
    public void testFib() {

        fibStore fibo = new fibStore();

              // Test cases
        assertEquals(0, fibo.fib(0));
        assertEquals(1, fibo.fib(1));
        assertEquals(1, fibo.fib(2));
        assertEquals(2, fibo.fib(3));
        assertEquals(3, fibo.fib(4));
        assertEquals(5, fibo.fib(5));
        assertEquals(8, fibo.fib(6));
        assertEquals(13, fibo.fib(7));
        assertEquals(21, fibo.fib(8));
        assertEquals(34, fibo.fib(9));
        assertEquals(55, fibo.fib(10));

    }
}
