class MatrixAnalysis:
    @staticmethod
    def sum(matrix: list[list[int]]) -> int:
        sum = 0
        for row in matrix:
            for num in row:
                sum += num
        return sum

    @staticmethod
    def min(matrix: list[list[int]]) -> int:
        min_value = matrix[0][0]
        for row in matrix:
            for num in row:
                if num < min_value:
                    min_value = num
        return min_value

    @staticmethod
    def max(matrix: list[list[int]]) -> int:
        max_value = matrix[0][0]
        for row in matrix:
            for num in row:
                if num > max_value:
                    max_value = num
        return max_value

    @staticmethod
    def mode(matrix: list[list[int]]) -> int:
        numbers_count: dict = {}
        for row in matrix:
            for num in row:
                numbers_count[num] = numbers_count.get(num, 0) + 1
        max_value = 0
        max_key = None
        for key, value in numbers_count.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key
