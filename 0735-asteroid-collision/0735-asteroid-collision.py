class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        answer = [asteroids[0]]
        
        for i in range(1, len(asteroids)):            
            while True:
                if not len(answer) or (answer[-1] < 0 or asteroids[i] > 0): # no collision
                    answer.append(asteroids[i])
                    break
                    
                if abs(answer[-1]) > abs(asteroids[i]):
                    break

                if abs(answer[-1]) == abs(asteroids[i]):
                    answer.pop()
                    break

                if abs(answer[-1]) < abs(asteroids[i]):
                    answer.pop()
                
        
        return answer