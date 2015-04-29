import java.util.*;

public class Solution {
	public List<Integer> spiralOrder (int[][] matrix) {
		List<Integer> spiralSol = new ArrayList<Integer>();
		if(matrix == null || matrix.length == 0) return spiralSol;

		int i = 0;
		int j = 0;
		int rowNum = matrix.length;
		int columnNum = matrix[0].length;
		int num1, num2;
		num1 = 0, num2 = 0;

		while(( i < rowNum-num1 && j < columnNum-num2)) {

			while( (matrix[i+1][j] != Integer.MIN_VALUE) || (i < rowNum - 1 )) {
				spiralSol.add(matrix[i+1][j]);
				matrix[i+1][j] =Integer.MIN_VALUE;
				i++;

			}
			while((i == rowNum - 1 && j < columnNum - 1) || (matrix[i+1][j] == Integer.MIN_VALUE && matrix[i][j+1] != Integer.MIN_VALUE)) {
				spiralSol.add(matrix[i][j+1]);
				matrix[i][j+1] = Integer.MIN_VALUE;
				j++;
			}
			while(((j == columnNum-1) && (i > 0)) || ( (matrix[i][j+1] == Integer.MIN_VALUE ) && (matrix[i+1][j] == Integer.MIN_VALUE) && (matrix[i][j-1] == Integer.MIN_VALUE)) ){
				spiralSol.add(matrix[i-1][j]);
				matrix[i-1][j] = Integer.MIN_VALUE;
				i--;

			}
			while(((  matrix[i+1][j] == Integer.MIN_VALUE) && ( matrix[i][j+1] == Integer.MIN_VALUE ) && ( matrix[i-1][j] == Integer.MIN_VALUE)) || ((i == 0) && (j > 0))){
				spiralSol.add(matrix[i][j-1]);
				matrix[i][j-1] = Integer.MIN_VALUE;
				j--;
			}
		}

		return spiralSol;
	}
}

