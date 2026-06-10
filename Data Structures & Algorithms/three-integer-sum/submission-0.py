# exercise: three sum with target = 0

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
        for i in range(len(nums)):
            num_freq[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums)):
                num_freq[nums[j]] -= 1
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                target = -nums[i] - nums[j]
                if target in num_freq and num_freq[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                num_freq[nums[j]] += 1
                
        return res

