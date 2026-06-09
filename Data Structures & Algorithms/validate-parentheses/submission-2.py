# TITOLO: Verifica Parentesi tramite Pila (Stack)
# SPIEGAZIONE: Verifica che la stringa abbia lunghezza pari, poi usa una lista come pila per memorizzare le parentesi aperte e confrontarle con le corrispettive chiusure.
# TIME COMPLEXITY: O(N) - Scorre i caratteri della stringa una sola volta. Le operazioni sulla pila (append e pop) costano O(1).
# SPACE COMPLEXITY: O(N) - Nel caso peggiore (es. stringa composta solo da parentesi aperte "((((("), la pila conterrà tutti gli N caratteri.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pila = []
        mappa_parentesi = {")": "(", "}": "{", "]": "["}
        
        for carattere in s:
            if carattere in mappa_parentesi:
                if not pila or pila[-1] != mappa_parentesi[carattere]:
                    return False
                pila.pop()
            else:
                pila.append(carattere)
        
        return len(pila) == 0