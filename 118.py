class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Generate the Pascal's triangle up to the given number of rows.

        Args:
            numRows: The number of rows to generate.

        Returns:
            A list of lists, where each inner list represents a row of the triangle.
        """
        results = []
        
        if numRows < 1:
            return results
        
        for i in range(0,numRows):
            row = []
            
            if i == 0:
                row.append(1)
                
            else:
                row.insert(0,1)
                row.insert(i,1)
                
                for j in range(1,i):
                    left_above = results[i-1][j-1]
                    right_above = results[i-1][j]
                    row.insert(j,left_above + right_above)
                    
            results.append(row)
            
        return results
        

## 118. Pascal's Triangle