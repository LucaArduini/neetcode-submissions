# TITOLO: Verifica Parentesi tramite Pila (Stack)
# SPIEGAZIONE: Verifica che la stringa abbia lunghezza pari, poi usa una lista come pila per memorizzare le parentesi aperte e confrontarle con le corrispettive chiusure.

class Solution:
    def isValid(self, s: str) -> bool:
        # Una stringa con lunghezza dispari non può avere tutte le parentesi accoppiate
        if len(s) % 2 != 0:
            return False
        
        pila = []
        # Mappa per associare ogni parentesi di chiusura alla rispettiva parentesi di apertura
        mappa_parentesi = {")": "(", "}": "{", "]": "["}
        
        for carattere in s:
            # Se il carattere è una parentesi di chiusura
            if carattere in mappa_parentesi:
                # Verifica se la pila è vuota o se l'ultimo elemento inserito non corrisponde
                if not pila or pila[-1] != mappa_parentesi[carattere]:
                    return False
                # Se corrisponde, rimuove la parentesi aperta dalla pila
                pila.pop()
            else:
                # Se è una parentesi aperta, viene aggiunta in fondo alla pila
                pila.append(carattere)
        
        # Ritorna True solo se tutte le parentesi aperte sono state correttamente chiuse (pila vuota)
        return len(pila) == 0