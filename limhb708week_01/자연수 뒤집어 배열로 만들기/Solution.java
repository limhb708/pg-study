import java.util.*;

class Solution {
    public int[] solution(long n) {
        // 숫자를 문자열로 변환
        String str = String.valueOf(n);

        // 뒤에서부터 각 자리 숫자를 배열에 담기
        int[] answer = new int[str.length()];
        for (int i = 0; i < str.length(); i++) {
            answer[i] = str.charAt(str.length() - 1 - i) - '0';
        }

        return answer;
    }
}
