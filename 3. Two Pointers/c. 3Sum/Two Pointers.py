# exercise: three sum with target = 0
# TIME COMPLEXITY: O(N^2)
# SPACE COMPLEXITY: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if val > 0:
                break

            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        # L'ordinamento è fondamentale per usare la tecnica dei due puntatori
        # e per gestire facilmente i duplicati
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            # OTTIMIZZAZIONE: Se il numero corrente è > 0, la somma non potrà mai 
            # essere zero perché l'array è ordinato e i numeri successivi saranno tutti positivi
            if val > 0:
                break

            # SALTO DUPLICATI: Se il valore corrente è uguale al precedente, lo saltiamo
            # per evitare di inserire la stessa combinazione di numeri nel risultato
            if i > 0 and val == nums[i - 1]:
                continue

            # TWO POINTERS: Cerchiamo gli altri due numeri nell'intervallo [i+1, fine]
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # Trovata una tripla!
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    # SALTO DUPLICATI (interno): Dopo aver aggiunto una tripla, saltiamo tutti i 
                    # valori uguali a quello appena inserito per evitare duplicati nel risultato.
                    # Nota: il check 'l < r' evita che il puntatore superi quello destro
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res