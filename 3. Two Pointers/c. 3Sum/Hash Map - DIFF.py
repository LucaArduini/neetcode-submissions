# exercise: three sum with target = 0
# TIME COMPLEXITY: O(N^2)
# SPACE COMPLEXITY: O(N)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        # scorro array e creo hashmap num-freq
        num_freq = {}
        for num in nums:
            # if num in num_freq:
            #     num_freq[num] += 1
            # else:
            #     num_freq[num] = 1

            # "se il numero esiste, incrementalo di 1, altrimenti inizialo a 1"
            num_freq[num] = num_freq.get(num, 0) + 1

        # # oppure scorrendo array e calcolando frequenza al volo
        # num_freq_2 = {}
        # if nums:  # Controlla che l'array non sia vuoto
        #     count = 1
        #     for i in range(len(nums)):
        #         # Se non siamo all'ultimo elemento e il prossimo è uguale
        #         if i + 1 < len(nums) and nums[i] == nums[i+1]:
        #             count += 1
        #         else:
        #             # Siamo all'ultimo elemento o il prossimo è diverso: salviamo il conteggio
        #             num_freq_2[nums[i]] = count
        #             count = 1  # Resettiamo il contatore per il numero successivo

        res = []
        # Ciclo principale: 'i' identifica il primo numero della terna
        for i in range(len(nums)):
            # Riduciamo la frequenza del numero corrente nella mappa per "toglierlo" dal set disponibile
            num_freq[nums[i]] -= 1
            
            # Controllo duplicati: se il numero è uguale al precedente, lo saltiamo 
            # per evitare di generare triplette identiche
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Ciclo interno: 'j' identifica il secondo numero della terna
            for j in range(i + 1, len(nums)):
                # Riduciamo temporaneamente anche il secondo numero
                num_freq[nums[j]] -= 1
                
                # Controllo duplicati per il secondo numero
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Calcoliamo il terzo numero necessario per arrivare a zero (x + y + z = 0  => z = -(x + y))
                target = -nums[i] - nums[j]
                
                # Verifichiamo se il complemento (target) esiste ancora nella nostra mappa
                # (deve avere frequenza > 0, ovvero essere ancora disponibile)
                if target in num_freq and num_freq[target] > 0:
                    res.append([nums[i], nums[j], target])

            # Ripristino (Backtracking): dopo aver finito il ciclo interno per un dato 'i',
            # dobbiamo ripristinare le frequenze dei numeri che abbiamo usato come 'j'
            # per permettere al ciclo successivo di 'i' di avere una mappa corretta.
            for j in range(i + 1, len(nums)):
                num_freq[nums[j]] += 1
                
        return res

