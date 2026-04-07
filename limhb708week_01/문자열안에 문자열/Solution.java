class Solution {
    public int solution(String str1, String str2) {
        // str1 안에 str2가 포함되어 있으면 1, 아니면 2 반환
        if (str1.contains(str2)) {
            return 1;
        }

        return 2;

    }
}