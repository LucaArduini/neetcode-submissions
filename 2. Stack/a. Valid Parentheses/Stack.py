# TITOLO: Verifica Parentesi tramite Pila (Stack)
# SPIEGAZIONE: Verifica che la stringa abbia lunghezza pari, poi usa una lista come pila per memorizzare le parentesi aperte e confrontarle con le corrispettive chiusure.
# TIME COMPLEXITY: O(N)
# SPACE COMPLEXITY: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pila = []
        # Dizionario che mappa chiusura -> apertura attesa
        mappa_parentesi = {")": "(", "}": "{", "]": "["}
        
        for carattere in s:
            if carattere in mappa_parentesi:
                # Se è una chiusura, controlla l'ultima parentesi aperta nella pila
                if not pila or pila[-1] != mappa_parentesi[carattere]:
                    return False
                pila.pop()
            else:
                # Se è un'apertura, la inserisce nella pila
                pila.append(carattere)
        
        # È valida solo se non sono rimaste parentesi aperte in sospeso
        return len(pila) == 0