class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pre = [1]
        arr = []
        answer = []

        for num in range(1, numRows+1):
            arr = arr + [1]
            
            for i in range(1, num-1):
                arr[i] = pre[i-1] + pre[i]
            
            answer.append(arr)

            pre = arr[:]

        return answer