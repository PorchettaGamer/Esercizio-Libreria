from libro import aggiungi_libro, disponibilita_libro, mostra_libri_disponibili, mostra_libri_prestati, prestare_libro, restituire_libro

def main():
    while True:
        print("\n--- Gestione Libreria ---")
        print("1. Aggiungi libro")
        print("2. Prestare libro")
        print("3. Restituire libro")
        print("4. Controlla disponibilità libro")
        print("5. Libri disponibili")
        print("6. Libri prestati")
        print("7. Esci")
        
        scelta = input("Scegli un'opzione (1-7): ")

        if scelta == '1':
            aggiungi_libro()
        
        elif scelta == '2':
            prestare_libro()
        
        elif scelta == '3':
            restituire_libro()
        
        elif scelta == '4':
            disponibilita_libro()
        
        elif scelta == '5':
            mostra_libri_disponibili()
        
        elif scelta == '6':
            mostra_libri_prestati()
        
        elif scelta == '7':
            print("Uscita dal programma.")
            break
        
        else:
            print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()