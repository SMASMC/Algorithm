import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		int A;
		int B;
		A = scanner.nextInt();
		B = scanner.nextInt();
		int tot_1 = 0;
		int tot_10 = 0;
		int tot_100 = 0;

		// 일의 자리와 곱해주고 십의 자리와 곱해주고 백의 자리와 곱해주고

		tot_1 = (A * (B % 10));
		System.out.println(tot_1);// 일의자리와 곱
		tot_10 = (A * ((B / 10) % 10));
		System.out.println(tot_10);// 십의자리와 곱
		tot_100 = (A * (((B / 10) / 10) % 10));
		System.out.println(tot_100);// 백의자리와 곱
		System.out.println(A * B);

	}
}