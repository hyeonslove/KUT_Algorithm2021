/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1196
 */
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
 
        while (testcase > 0) {
            int length = sc.nextInt();
            int[] arr = new int[length];
            for (int i = 0; i < length; i++)
                arr[i] = sc.nextInt();
 
            int max, min;
            if (arr[0] < arr[1]) {
                max = arr[1];
                min = arr[0];
            } else {
                max = arr[0];
                min = arr[1];
            }
 
            for (int i = 2; i < length - 1; i += 2) {
                if (arr[i] < arr[i + 1]) {
                    if (arr[i] < min)
                        min = arr[i];
                    if (arr[i + 1] > max)
                        max = arr[i + 1];
                } else {
                    if (arr[i] > max)
                        max = arr[i];
                    if (arr[i + 1] < min)
                        min = arr[i + 1];
                }
            }
            if (length % 2 == 1) {
                if (max < arr[length - 1])
                    max = arr[length - 1];
 
                if (min > arr[length - 1])
                    min = arr[length - 1];
            }
            System.out.println(max + " " + min);
            testcase--;
        }
    }
 
}