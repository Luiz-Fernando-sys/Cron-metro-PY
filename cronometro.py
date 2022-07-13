import time #Importando a biblioteca 'time' do Python

def contagem_regressiva(tempo_a_ser_contado): #Criando a função 

    while tempo_a_ser_contado:
        mins, secs = divmod(tempo_a_ser_contado, 60)
        timer = '\n{:02d}:{:02d}'.format(mins, secs) #Formatação de como será exibido a contagem regressiva na tela
        print(timer, end="\r")
        time.sleep(1)
        tempo_a_ser_contado -= 1 #A cada vez o tempo vai sendo regressado em 1 unidade

    print('\nAcabou o tempo!!!') #Mensagem a ser exibida quando o tempo acabar


tempo_dito_pelo_usuario = input("Digite o tempo em segundos: ")
contagem_regressiva(int(tempo_dito_pelo_usuario))
