# size = int(input())
matrix = []
# matrix = [[input() for _ in range(m)] for _ in range(n)]
if __name__ == "__main__":

    def chunked(lst, chunk_size):
        for i in range(0, len(lst), chunk_size):
            yield lst[i : i + chunk_size]

    def diag_sum(matrix: list) -> int:
        """cумма значений матрицы по диагонали"""
        res = 0
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i == j:
                    res += int(matrix[i][j])
        return res

    n = int(input())
    s = input().split()

    result = list(chunked(s, n))

    print(result)
    print("=" * 20)
    print(diag_sum(result))
