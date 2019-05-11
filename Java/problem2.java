import java.util.*;
import java.io.*;

/*
MaxPairwiseProductNaive(A[1...n]):
	product <- 0
	for i from 1 to n:
		for i from i+1 to n:
			product <- max(product, A[i]*A[j])
	return product
-----------------------------------------------------
MaxPairwiseProductFast(A[1...n]):
	index1 <- 1
	for i from 2 to n:
		if A[i] > A[index1]:
			index1 <- i
	if index1 = 1:
		index2 <- 2
	else:
		index2 <- 2
	for i from 1 to n:
		if i != index1 and A[i] > A[index2]:
			index2 <- i
	return A[index1]*A[index2]
-----------------------------------------------------
MaxPairwiseProductFast2(A[1...n]):
	index <- 1
	for i from 2 to n:
		if A[i] > A[index]:
			index <- i
	swap A[index] and A[n]
	index <- 1
	for i from 2 to n-1:
		if A[i] > A[index]:
			index <- i
	swap A[index] and A[n-1]
	return A[n-1]*A[n]
------------------------------------------------------
MaxPairwiseProductBySorting(A[1...n]):
	Sort(A)
	return A[n-1]*A[n]
------------------------------------------------------
StressTest(N, M):
	while true:
		n <- random integer between 2 and N
		allocate array A[1..n]
		for i from 1 to n:
			A[i] <- random integer between 0 and M
		print(A[1..n])
		result1 <- MaxPairwiseProductNaive(A)
		result2 <- MaxPairwiseProductFast(A)
		if result1 = result2:
			print("OK")
		else:
			print("Wrong answer:", result1, result2)
			return
*/

public class problem2 {

	static long getMaxPairwiseProductFast(int[] numbers) {
		int n = numbers.length;
		int index1 = 0;
		int index2;
		for (int i = 1; i < n; ++i) {
			if (numbers[i] > numbers[index1]) {
				index1 = i;
			}
		}
		if (index1 == 0) {
			index2 = 1;
		} else {
			index2 = 0;
		}
		for (int i = 0; i < n; ++i) {
			if (i != index1 && numbers[i] > numbers[index2]) {
				index2 = i;
			}
		}
		return (long)numbers[index1]*numbers[index2];
	}

	static void Swap(int p, int q) {
		int temp;
		temp = p;
		p = q;
		q = temp;
	}

	static long getMaxPairwiseProductFast2(int[] numbers) {
		int n = numbers.length;
		int index = 0;
		for (int i = 1; i < n; ++i) {
			if (numbers[i] > numbers[index]) {
				index = i;
			}
		}
		Swap(numbers[index], numbers[n-1]);
		index = 0;
		for (int i = 1; i < n-1; ++i) {
			if (numbers[i] > numbers[index]) {
				index = i;
			}
		}
		Swap(numbers[index], numbers[n-2]);
		return (long)numbers[n-1]*numbers[n-2];
	}

	static long getMaxPairwiseProductNaive(int[] numbers) {
		long product = 0;
		int n = numbers.length;
		for (int i = 0; i < n; ++i) {
			for (int j = i+1; j < n; ++j) {
				product = Math.max(product, (long)numbers[i]*numbers[j]);
			}
		}
		return product;
	}

	static void runStressTest(int N, int M) {
		Random rand = new Random();
		while (true) {
			int n = rand.nextInt((N-2)+1) + 2;
			int A[] = new int[n];
			for (int i = 0; i < n; ++i) {
				A[i] = rand.nextInt(M+1);
			}
			for (int j = 0; j < n; ++j) {
				System.out.print(A[j] + " ");
			}
			long result1 = getMaxPairwiseProductNaive(A);
			long result2 = getMaxPairwiseProductFast(A);
			if (result1 == result2) {
				System.out.println("OK");
			} else {
				System.out.println("Wrong answer: " + result1 + result2);
			}
			break;
		}
	}

	static long getMaxPairwiseProductBySorting(int[] numbers) {
		int n = numbers.length;
		Arrays.sort(numbers);
		return (long)numbers[n-1]*numbers[n-2];
	}

	public static void main(String[] args) {
		FastScanner scanner = new FastScanner(System.in);
		int n = scanner.nextInt();
		int[] numbers = new int[n];
		for (int i=0; i<n; i++) {
			numbers[i] = scanner.nextInt();
		}
		System.out.println(getMaxPairwiseProductBySorting(numbers));
		//runStressTest(200000, 200000);
	}

	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		FastScanner(InputStream stream) {
			try {
				br = new BufferedReader(new InputStreamReader(stream));
			} catch (Exception e) {
				e.printStackTrace();
			}
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}
	}

}