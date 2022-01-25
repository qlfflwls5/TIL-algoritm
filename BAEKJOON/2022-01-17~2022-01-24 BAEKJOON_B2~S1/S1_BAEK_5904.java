// Moo 게임
// Moo는 술자리에서 즐겁게 할 수 있는 게임이다. 이 게임은 Moo수열을 각 사람이 하나씩 순서대로 외치면 되는 게임이다.
// Moo 수열은 길이가 무한대이며, 다음과 같이 생겼다. 
// m o o m o o o m o o m o o o o m o o m o o o m o o m o o o o o 
// Moo 수열은 다음과 같은 방법으로 재귀적으로 만들 수 있다. 
// 먼저, S(0)을 길이가 3인 수열 "m o o"이라고 하자. 1보다 크거나 같은 모든 k에 대해서, S(k)는 S(k-1)과 o가 k+2개인 수열 "m o ... o" 와 S(k-1)을 합쳐서 만들 수 있다.
// S(0) = "m o o"
// S(1) = "m o o m o o o m o o"
// S(2) = "m o o m o o o m o o m o o o o m o o m o o o m o o"
// 위와 같은 식으로 만들면, 길이가 무한대인 문자열을 만들 수 있으며, 그 수열을 Moo 수열이라고 한다.
// N이 주어졌을 때, Moo 수열의 N번째 글자를 구하는 프로그램을 작성하시오.


import java.util.*;


public class S1_BAEK_5904 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int cnt = 2;
    StringBuilder sb = new StringBuilder("moo");
    for(int i = 1; i < 30; i++) {
      cnt += 1;
      String repeated = new String(new char[cnt]).replace("\0", "o");
      sb = sb.append(sb).append("m").append(repeated).append(sb);
    }

    System.out.println(sb.charAt(N-1));
  }
}