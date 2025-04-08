import customtkinter
from Resultado import Pedra, Papel, Tesoura
from Centralizar import centralizar_janela

def escolha(Ran):
  JanelaEscolha = customtkinter.CTk()
  JanelaEscolha.geometry('300x200')
  JanelaEscolha.title('Pedra Papel Tesoura')

  centralizar_janela(JanelaEscolha, largura=425, altura= 250) 

  text = customtkinter.CTkLabel(JanelaEscolha,
                                text='A IA já escolheu a dela!\nQual sua escolha?',
                                text_color='White',
                                font=('Arial', 20))
  text.pack(pady=25)

  frame_botoes = customtkinter.CTkFrame(JanelaEscolha, fg_color="transparent")
  frame_botoes.pack(pady=60)
 
  pedraB = customtkinter.CTkButton(frame_botoes,
                                  text='Pedra',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: Pedra(Ran))
  pedraB.grid(row=0, column=0, padx=10)

  papelB = customtkinter.CTkButton(frame_botoes,
                                  text='Papel',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: Papel(Ran))
  papelB.grid(row=0, column=1, padx=10)

  tesouraB = customtkinter.CTkButton(frame_botoes,
                                  text='Tesoura',
                                  text_color='White',
                                  corner_radius=17,
                                  width=100,
                                  font=('Arial', 16),
                                  command=lambda: Tesoura(Ran))
  tesouraB.grid(row=0, column=2, padx=10)
  
  JanelaEscolha.mainloop()