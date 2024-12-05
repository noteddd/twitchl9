import tkinter as tk
import pyautogui
import threading
import time
import keyboard
import os

clicando = False
velocidade_base = 0.673
velocidade = velocidade_base

def clicar():
    global clicando
    while clicando:
        pyautogui.click(button='left')  # Clique esquerdo
        pyautogui.click(button='right')  # Clique direito, sem delay
        time.sleep(1 / velocidade)  # Espera apenas entre os ciclos de cliques

def toggle_loop():
    global clicando
    clicando = not clicando
    if clicando:
        thread = threading.Thread(target=clicar)
        thread.daemon = True
        thread.start()

def ajustar_velocidade(fator):
    global velocidade
    velocidade = velocidade_base * fator
    velocidade_label.config(text=f"CPS: {velocidade:.2f} ataques por segundo")

def fechar():
    janela.quit()

janela = tk.Tk()
janela.title("made by siul")
janela.geometry("500x200")
janela.configure(bg="black")
icon_path = os.path.join(os.path.dirname(__file__), 'twitch.ico')
janela.iconbitmap('twitch.ico')


texto_topo = tk.Label(janela, text="TWITCH L9 HAHAHA xD", bg="black", fg="white", font=("Arial", 20, "bold"))
texto_topo.pack(pady=10)

frame_botoes = tk.Frame(janela, bg="black")
frame_botoes.pack(pady=10)

botao_1 = tk.Button(frame_botoes, text="1x", command=lambda: ajustar_velocidade(1), width=10, height=2, bg="white", fg="black", font=("Arial", 12, "bold"))
botao_1.grid(row=0, column=0, padx=5)

botao_1_5 = tk.Button(frame_botoes, text="1.5x", command=lambda: ajustar_velocidade(4.5), width=10, height=2, bg="white", fg="black", font=("Arial", 12, "bold"))
botao_1_5.grid(row=0, column=1, padx=5)

botao_2 = tk.Button(frame_botoes, text="2x", command=lambda: ajustar_velocidade(6), width=10, height=2, bg="white", fg="black", font=("Arial", 12, "bold"))
botao_2.grid(row=0, column=2, padx=5)

botao_2_5 = tk.Button(frame_botoes, text="2.5x", command=lambda: ajustar_velocidade(7.45), width=10, height=2, bg="white", fg="black", font=("Arial", 12, "bold"))
botao_2_5.grid(row=0, column=3, padx=5)

velocidade_label = tk.Label(janela, text=f"CPS: {velocidade:.2f} ataques por segundo", bg="black", fg="white", font=("Arial", 14, "bold"))
velocidade_label.pack(pady=10)

janela.after(100, lambda: keyboard.add_hotkey('insert', toggle_loop))
janela.after(100, lambda: keyboard.add_hotkey('esc', fechar))

janela.mainloop()
