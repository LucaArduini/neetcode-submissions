class TimeMap:


    def __init__(self):
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

        # NB: nella maggior parte dei problemi di questo tipo (come su
        # LeetCode), l'input dei set è garantito essere cronologico.


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        values = self.map[key]
        left, right = 0, len(values) - 1
        res = ""
        
        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
                # questo valore è “utilizzabile”, lo salvo in res
                # ma cerco ancora a destra (magari c’è uno più recente ma ancora valido)
            else:
                right = mid - 1
                # scarto la metà destra
        
        return res