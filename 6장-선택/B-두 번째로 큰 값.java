/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1197
 */
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
 
        while (testcase > 0) {
            int length = sc.nextInt();
            int[] arr = new int[length * 2 - 1];
            for (int i = 0; i < length; i++)
                arr[i + length - 1] = sc.nextInt();
 
            int end_pos = length * 2 - 2;
            for (int pos = length - 2; pos >= 0; pos--) {
                arr[pos] = Math.max(arr[end_pos - (length - pos - 2) * 2], arr[end_pos - (length - pos - 2) * 2 - 1]);
            }
            int first_max = arr[0];
            int second_max = -2147483648;
            for (int i = 1; i < length * 2 - 2; i++) {
                if (arr[i] == first_max || arr[i + 1] == first_max) {
                    if (arr[i] == first_max) {
                        if (second_max < arr[i + 1])
                            second_max = arr[i + 1];
 
                    } else {
                        if (second_max < arr[i])
                            second_max = arr[i];
                    }
                }
            }
            System.out.println(second_max);
            testcase--;
        }
    }
}