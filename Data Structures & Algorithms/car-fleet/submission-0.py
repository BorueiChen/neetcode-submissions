class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        table = {} # pos: speed

        for pos, s in zip(position, speed):
            table[pos] = s
        
        position.sort()

        last_used = -1
        fleet = []
        for idx, pos in enumerate(position[::-1]):
            used = (target - pos) / table[pos]
            if last_used < used:
                fleet.append(pos)
                last_used = used

        return len(fleet)
