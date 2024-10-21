import openai
import tkinter as tk
from tkinter import scrolledtext

# Clé API OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

# Fonction pour appeler l'API GPT et obtenir une réponse
def get_gpt_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Utiliser GPT-3 ou GPT-4 selon ce qui est disponible
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Je suis désolé, je ne peux pas répondre pour l'instant."

# Fonction pour envoyer un message
def send_message():
    user_message = message_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Vous : " + user_message + "\n")
    
    # Obtenir une réponse de GPT-4
    response = get_gpt_response(user_message)
    chat_window.insert(tk.END, "TUI : " + response + "\n\n")
    
    chat_window.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

# Créer l'interface graphique de l'écran d'iPhone 16
def create_iphone_screen():
    window = tk.Tk()
    window.title("iPhone 16 - TUI Écoresponsable")

    # Définir les dimensions de la fenêtre pour simuler un écran d'iPhone 16
    window.geometry("430x900")
    window.resizable(False, False)

    # Zone de chat (ScrolledText pour défiler les messages)
    global chat_window
    chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=25, state=tk.DISABLED)
    chat_window.pack(padx=10, pady=10)

    # Champ de saisie de message
    global message_entry
    message_entry = tk.Entry(window, width=40)
    message_entry.pack(pady=10)

    # Bouton pour envoyer le message
    send_button = tk.Button(window, text="Envoyer", command=send_message)
    send_button.pack()

    # Lancer la fenêtre
    window.mainloop()

# Exécuter l'application
create_iphone_screen()
