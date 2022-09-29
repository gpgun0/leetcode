class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        answer = []
        
        std = -1
        while l <= r:
            mid = (l+r)//2
            
            if arr[mid] < x:
                l = mid+1
            elif arr[mid] > x:
                r = mid-1
            elif arr[mid] == x:
                std = mid
                break
        
        if l >= len(arr):
            return arr[len(arr)-k:]
        elif r < 0:
            return arr[:k]
        
        if std == -1:
            lp = r
            rp = l
            
            while k and lp >= 0 and rp < len(arr):
                if x-arr[lp] < arr[rp]-x:
                    answer.append(arr[lp])
                    lp -= 1
                elif x-arr[lp] > arr[rp]-x:
                    answer.append(arr[rp])
                    rp += 1
                elif x-arr[lp] == arr[rp]-x:
                    answer.append(arr[lp])
                    lp -= 1                    
                k -= 1
            
            if k:
                if lp < 0:               
                    while k:
                        answer.append(arr[rp])
                        rp += 1
                        k-=1
                elif rp >= len(arr):
                    while k:
                        answer.append(arr[lp])
                        lp -= 1
                        k-=1
                    
                
        if std != -1:
            answer.append(arr[std])
            lp = std-1
            rp = std+1
            k -= 1
            
            while k and lp >= 0 and rp < len(arr):
                if x-arr[lp] < arr[rp]-x:
                    answer.append(arr[lp])
                    lp -= 1
                elif x-arr[lp] > arr[rp]-x:
                    answer.append(arr[rp])
                    rp += 1
                elif x-arr[lp] == arr[rp]-x:
                    answer.append(arr[lp])
                    lp -= 1     
                    
                k -= 1
                
            print(lp, rp)
            if k:
                if lp < 0:               
                    while k:
                        answer.append(arr[rp])
                        rp += 1
                        k-=1
                elif rp >= len(arr):
                    while k:
                        answer.append(arr[lp])
                        lp -= 1
                        k-=1
        return sorted(answer)