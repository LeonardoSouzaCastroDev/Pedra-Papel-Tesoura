import customtkinter
from Centralizar import centralizar_janela 

def Pedra(Ran):

  JanelaJogo = customtkinter.CTk()
  JanelaJogo.geometry('300x200')
  JanelaJogo.title('Pedra Papel Tesoura')

  centralizar_janela(JanelaJogo, largura=425, altura= 250)
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()
    
def Papel(Ran):
  JanelaJogo = customtkinter.CTk()
  JanelaJogo.geometry('300x200')
  JanelaJogo.title('Pedra Papel Tesoura')

  centralizar_janela(JanelaJogo, largura=425, altura= 250)
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

def Tesoura(Ran): 
  JanelaJogo = customtkinter.CTk()
  JanelaJogo.geometry('300x200')
  JanelaJogo.title('Pedra Papel Tesoura')

  centralizar_janela(JanelaJogo, largura=425, altura= 250)
  match Ran:
    case 'Pedra':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Perdeu! ;-;'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Papel':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'GANHOU!!!!! ;)'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()

    case 'Tesoura':
      text = customtkinter.CTkLabel(JanelaJogo,
                                    text='A IA escolheu {}\n\n'
                                    'Empate!'.format(Ran),
                                    text_color='White',
                                    font=('Arial', 20))
      text.pack(pady=50)

      JanelaJogo.mainloop()


