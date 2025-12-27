class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generator(numRows):
            if numRows == 1:
                return [[1]]
            triangle = generator(numRows - 1)

            new_row = [1]
            prev_row = triangle[-1]
            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i] + prev_row[i+1])
            new_row.append(1)
            triangle.append(new_row)
            return triangle
        return generator(numRows)