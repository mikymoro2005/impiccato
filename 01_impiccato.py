import random
import string

def ottieni_parola_valida():
    parole = ['python', 'programmazione', 'computer', 'gioco', 'sviluppo']
    parola = random.choice(parole)
    return parola.upper()

def impiccato():
    parola = ottieni_parola_valida()
    lettere_parola = set(parola)  # lettere nella parola
    alfabeto = set(string.ascii_uppercase)
    lettere_usate = set()  # lettere che l'utente ha indovinato

    vite = 6  # numero di tentativi

    # ottieni input dall'utente finché ci sono lettere da indovinare
    while len(lettere_parola) > 0 and vite > 0:
        print('Hai', vite, 'vite rimaste e hai usato queste lettere: ', ' '.join(lettere_usate))

        # mostra lo stato attuale della parola
        parola_lista = [lettera if lettera in lettere_usate else '_' for lettera in parola]
        print('Parola attuale: ', ' '.join(parola_lista))

        lettera_utente = input('Indovina una lettera o la parola intera: ').upper()
        
        # Controlla se l'utente ha inserito la parola intera
        if lettera_utente == parola:
            print('Complimenti! Hai indovinato la parola', parola, '!!')
            return
            
        if len(lettera_utente) == 1 and lettera_utente in alfabeto - lettere_usate:
            lettere_usate.add(lettera_utente)
            if lettera_utente in lettere_parola:
                lettere_parola.remove(lettera_utente)
                print('')
            else:
                vite = vite - 1
                print('\nLa tua lettera,', lettera_utente, 'non è nella parola.')
        
        elif lettera_utente in lettere_usate:
            print('\nHai già usato questa lettera. Prova con un\'altra!')
        
        else:
            print('\nCarattere non valido. Inserisci una lettera dell\'alfabeto.')
            
    # arriva qui quando len(lettere_parola) == 0 O quando vite == 0
    if vite == 0:
        print('Mi dispiace, hai perso! La parola era', parola)
    else:
        print('Complimenti! Hai indovinato la parola', parola, '!!')

while True:
    impiccato()
    if input("Vuoi giocare ancora? (s/n): ").lower() != 's':
        break

print("Grazie per aver giocato!")
