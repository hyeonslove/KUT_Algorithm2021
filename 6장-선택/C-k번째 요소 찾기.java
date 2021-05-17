/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1198
 */
import java.util.Scanner;
 
public class Main {
 
    public static int Partition(int[] arr, int n) {
        int p = arr[0];
        int i = 1;
        for (int j = 1; j < n; j++) {
            if (arr[j] < p) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
            }
        }
 
        int temp = arr[0];
        arr[0] = arr[i - 1];
        arr[i - 1] = temp;
 
        return i;
    }
 
    public static int RSelect(int[] arr, int n, int target) {
        int pivot_idx = (int) (Math.random() * n);
        int pivot = arr[pivot_idx];
 
        int temp = arr[0];
        arr[0] = arr[pivot_idx];
        arr[pivot_idx] = temp;
 
        int pos = Partition(arr, n);
 
        int[] new_arr = new int[0];
        int new_target = target;
        int new_n = 0;
 
        if (pos == target) {
            return pivot;
        } else if (pos < target) { // ¿À¸¥ÂÊ
            new_target -= pos;
            new_n = n - pos;
            new_arr = new int[new_n];
            for (int i = 0; i < new_n; i++) {
                new_arr[i] = arr[i + pos];
            }
        } else if (pos > target) { // ¿ÞÂÊ
            new_n = pos - 1;
            new_arr = new int[new_n];
            for (int i = 0; i < new_n; i++) {
                new_arr[i] = arr[i];
            }
        }
        return RSelect(new_arr, new_n, new_target);
 
    }
 
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
 
        while (testcase > 0) {
            int length = sc.nextInt();
            int target = sc.nextInt();
            int[] arr = new int[length];
 
            for (int i = 0; i < length; i++) {
                arr[i] = sc.nextInt();
            }
            System.out.println(RSelect(arr, length, target));
            testcase--;
        }
    }
}