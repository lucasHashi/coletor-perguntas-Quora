from coletor_quora import Coletor_Quora



def main():
    nome_usuario_scrap = 'Vincent Pisano'

    coletor = Coletor_Quora(nome_usuario_scrap)

    coletor.coletar_dados_perguntas()
    coletor.print_csv()
























if __name__ == "__main__":
    main()