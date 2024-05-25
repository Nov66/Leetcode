class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for n in operations:
            if n == "C":
                record.pop()
            elif n == "D":
                record.append(2*record[len(record) - 1])
            elif n == "+":
                record.append(record[-1] + record[-2])
            else:
                record.append(int(n))

        return sum(record)
        