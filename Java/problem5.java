import java.util.*;

/*
NaiveGCD(a, b):
	best <- 0
	for d from 1 to a+b:
		if d/a and d/b:
			best <- d
	return best
------------------------------------------
EuclidGCD(a, b):
	if b = 0:
		return a
	a1 <- the remainder when a is divided by b
	return EuclidGCD(b, a1)
*/

public class problem5 {

	private static long NaiveGCD(int a, int b) {
		long best = 0;
		for (long i = 0; i <= a+b; ++i) {
			if (a%i == 0 && b%i == 0) {
				best = i;
			}
		}
		return best;
	}

	private static long EuclidGCD(int a, int b) {
		if (b==0)
			return a;
		int a1 = a%b;
		return EuclidGCD(b, a1);
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		int b = s.nextInt();
		System.out.println(EuclidGCD(a, b));
	}
}