import java.util.Scanner;
import java.math.BigInteger;

public class problem4 {

	private static int getFibLastDigit(int n) {
		int[] f = new int[n+1];
		f[0] = 0;
		f[1] = 1;
		for(int i = 2; i <= n; i++)
			f[i] = (f[i-1] + f[i-2]) % 10;
		return f[n];
	}

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		System.out.println(getFibLastDigit(n));
	}
}