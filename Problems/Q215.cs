// Q215.cs
// https://programmers.co.kr/learn/courses/30/lessons/12950?language=csharp

public class Solution {
    public int[,] solution(int[,] arr1, int[,] arr2) {
        int row = arr1.GetLength(0);
        int column = arr1.GetLength(1);
        int[,] answer = new int[row, column];

        for(int i = 0; i < row; i ++)
        {
            for(int j = 0; j < column; j ++)
            {
                answer[i, j] = arr1[i, j] + arr2[i, j];
            }
        }
        return answer;
    }
}