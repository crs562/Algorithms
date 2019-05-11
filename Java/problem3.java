import java.util.Scanner;
import java.math.BigInteger;

/*
FibRecurs(n):
	if n <= 1:
		return n
	else:
		return FibRecurs(n-1) + FibRecurs(n-2)
--------------------------------------------------
FibList(n):
	create an array F[0...n]
	F[0] <- 0
	F[1] <- 1
	for i from 2 to n:
		F[i] <- F[i-1] + F[i-2]
	return F[n]
*/


public class problem3 {

	private static long getFibRecurs(int n) {
		if (n <= 1) {
			return n;
		} else {
			return getFibRecurs(n-1) + getFibRecurs(n-2);
		}
	}

	private static BigInteger getFibList(int n) {
		if(n == 0)
			return BigInteger.ZERO;
		else if(n == 1)
			return BigInteger.ONE;
		else {
			BigInteger[] f = new BigInteger[n+1];
			f[0] = BigInteger.ZERO;
			f[1] = BigInteger.ONE;
			for(int i = 2; i <= n; i++)
				f[i] = f[i-1].add(f[i-2]);
			return f[n];
		}
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		System.out.println(getFibList(n));
	}
}