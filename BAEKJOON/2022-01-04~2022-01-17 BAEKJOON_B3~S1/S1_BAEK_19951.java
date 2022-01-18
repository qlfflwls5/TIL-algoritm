// 태상이의 훈련소 생활
// 2020년 5월 14일 논산훈련소에 입대한 태상이는 첫 총기 훈련에서 가스 조절기를 잃어버리는 중대한 실수를 범했다. 그로 인해, 태상이는 조교들에게 눈총을 받게 되었다. 
// 조교들은 태상이에게 연병장(운동장)의 흙을 옮기는 일을 주고 제대로 수행하지 못하면 징계를 내리려고 한다.
// 연병장은 일렬로 이어진 N개의 칸으로 이루어져 있으며 각 칸마다 높이를 가지고 있고, 첫 번째 칸부터 순서대로 1번, 2번, 3번, ..., N번 칸으로 명칭이 붙어있다. 
// 조교들은 총 M명이 있으며, 각 조교들은 태상이에게 a번 칸부터 b번 칸까지 높이 k만큼 흙을 덮거나 파내라고 지시한다. 
// 흙은 주변 산에서 얼마든지 구할 수 있으므로 절대로 부족하지 않다.
// 태상이는 각 조교의 지시를 각각 수행하면, 다른 조교의 지시로 흙을 덮어둔 칸을 다시 파내기도 하는 비효율적인 일이 발생하는 것을 깨달았다. 
// 그래서 태상이는 각 조교의 지시를 모아 연병장 각 칸의 최종 높이를 미리 구해 한 번에 일을 수행하려고 한다.
// 불쌍한 태상이를 위해 조교들의 지시를 모두 수행한 뒤 연병장 각 칸의 높이를 구하자.


import java.util.*;
import java.util.stream.Stream;


public class S1_BAEK_19951 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String[] strs = sc.nextLine().split(" ");
    int N = Integer.parseInt(strs[0]);
    int M = Integer.parseInt(strs[1]);
    int[] arr = Stream.of(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    int[] accStart = new int[N];
    int[] accEnd = new int[N];
    for(int i = 0; i < M; i++) {
      int A = sc.nextInt();
      int B = sc.nextInt();
      int H = sc.nextInt();
      accStart[A-1] += H;
      accEnd[B-1] += H;
    }

    int accStack = 0;
    for(int i = 0; i < N; i++) {
      accStack += accStart[i];
      arr[i] += accStack;
      accStack -= accEnd[i];
    }

    sc.close();
    System.out.println(String.join(" ", Arrays.stream(arr).mapToObj(String::valueOf).toArray(String[]::new)));
  }
}
