/*
    KOREATECH 2021 Algorithm
    https://judge.koreatech.ac.kr/problem.php?id=1192
*/

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;
 
public class Main {
 
    public static List<Integer> quick_sort(List<Integer> arr) {
        if (arr.size() <= 1)
            return arr;
         
        Random rand = new Random();
        int pivot = arr.get(arr.size()/2);
        List<Integer> left = new ArrayList<Integer>();
        List<Integer> mid = new ArrayList<Integer>();
        List<Integer> right = new ArrayList<Integer>();
 
        for (int num : arr) {
            if (num < pivot)
                left.add(num);
            else if (num > pivot)
                right.add(num);
            else
                mid.add(num);
        }
        return Stream.of(quick_sort(left), mid, quick_sort(right)).flatMap(Collection::stream)
                .collect(Collectors.toList());
 
    }
 
     
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
 
        while (testcase > 0) {
            int length = sc.nextInt();
            ArrayList<Integer> input_data = new ArrayList<Integer>();
            for (int i = 0; i < length; i++) {
                input_data.add(sc.nextInt());
            }
            for (int num : quick_sort(input_data)) {
                System.out.print(num + " ");
            }
 
            testcase--;
        }
    }
}