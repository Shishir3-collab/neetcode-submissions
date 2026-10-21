class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position,speed),reverse= True)
        max_time = 0 
        fleet = 0 
        for p,s in car:
            time = (target-p)/s
            if time > max_time:
                fleet +=1
                max_time = time
        return fleet

        