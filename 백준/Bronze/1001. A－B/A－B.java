import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		int A;
		int B;
		
		Scanner scanner =new Scanner(System.in);
		
		A=scanner.nextInt();
		B=scanner.nextInt();
		if(A>0&&B<10) {
		System.out.println(A-B);
		}
		else {
			System.out.println("시스템 오류");
		}
	}
	
	
}
