libri_disponibili = []
libri_prestati = []

def aggiungi_libro():
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci l'autore del libro: ")
    libro = {"titolo": titolo, "autore": autore, "disponibile": True}
    libri_disponibili.append(libro)
    print("Il libro '{titolo}' è stato aggiunto alla libreria.")

def prestare_libro():
    titolo = input("Inserisci il titolo del libro da prestare: ")
    for libro in libri_disponibili:
        if libro["titolo"].lower() == titolo.lower() and libro["disponibile"]:
            libro["disponibile"] = False
            libri_prestati.append(libro)
            print("Il libro '{libro['titolo']}' è stato prestato.")
            return
    print("Il libro non è disponibile per il prestito.")

def restituire_libro():
    titolo = input("Inserisci il titolo del libro da restituire: ")
    for libro in libri_prestati:
        if libro["titolo"].lower() == titolo.lower():
            libro["disponibile"] = True
            libri_prestati.remove(libro)
            libri_disponibili.append(libro)
            print("Il libro '{libro['titolo']}' è stato restituito.")
            return
    print("Il libro non è stato trovato tra i prestiti.")

def disponibilita_libro():
    titolo = input("Inserisci il titolo del libro per verificarne la disponibilità: ")
    for libro in libri_disponibili:
        if libro["titolo"].lower() == titolo.lower():
            if libro["disponibile"]:
                print("Il libro '{libro['titolo']}' è disponibile.")
            else:
                print("Il libro '{libro['titolo']}' non è disponibile.")
            return
    print("Il libro non è presente nella libreria.")

def mostra_libri_disponibili():
    if len(libri_disponibili) == 0:
        print("Nessun libro disponibile nella libreria.")
    else:
        print("Libri disponibili nella libreria:")
        for libro in libri_disponibili:
            print("{libro['titolo']} di {libro['autore']}")

def mostra_libri_prestati():
    if len(libri_prestati) == 0:
        print("Nessun libro è stato prestato.")
    else:
        print("Libri prestati:")
        for libro in libri_prestati:
            print("{libro['titolo']} di {libro['autore']}")