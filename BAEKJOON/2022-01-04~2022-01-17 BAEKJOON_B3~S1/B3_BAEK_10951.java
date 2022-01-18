// A+B-4
// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.


import java.util.*;


/**
 * B3_BAEK_10951
 */
public class B3_BAEK_10951 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (true) {
      try {
        int A = sc.nextInt();
        int B = sc.nextInt();
        System.out.println(A + B);
      } catch (Exception e) {
        break;
      }
    }
    
    sc.close();
  }
}