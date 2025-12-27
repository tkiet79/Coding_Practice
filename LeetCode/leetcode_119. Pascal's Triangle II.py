class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def Rows(current_index):
            if current_index == 0:
                return [1] 

            prev_row = Rows(current_index - 1)
            new_row = [1]
            

            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i] + prev_row[i+1])
            new_row.append(1)
            return new_row
        return Rows(rowIndex)