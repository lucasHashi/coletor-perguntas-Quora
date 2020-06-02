from bs4 import BeautifulSoup
import pandas as pd
import requests

class Coletor_Quora(object):
    def __init__(self, nome_usuario):
        self.path_csv = 'users csv/'+str(nome_usuario)+'.csv'
        self.nome_usuario = nome_usuario
    
    def coletar_dados_perguntas(self):
        df = pd.read_csv(self.path_csv)
        dados_perguntas = []

        for _, linha in df.iterrows():
            url = linha[3]
            url = url.replace('/unanswered/','/')
            url_log = url + '/log'

            page = requests.get(url_log)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            try:
                pergunta = soup.select("a.question_link span.ui_qtext_rendered_qtext")[0].get_text()
                print(pergunta)
                
                seguidores = soup.select('div.QuestionStats div.u-flex-align--center span')[1].get_text()
                seguidores = int(seguidores.split()[0])
                print(seguidores)
                
                visualizacoes = soup.select('div.QuestionStats div.u-flex-align--center span')[3].get_text()
                visualizacoes = int(visualizacoes.split()[0].replace(',',''))
                print(visualizacoes)
                
                dados_perguntas.append([pergunta, seguidores, visualizacoes])
            except:
                pass
        
        df_perguntas = pd.DataFrame(data=dados_perguntas, columns=['pergunta', 'seguidores', 'visualizacoes'])
        self.df_perguntas = df_perguntas.copy()
    
    def print_csv(self):
        pasta = 'perguntas coletadas'

        self.df_perguntas.to_csv(pasta + '/' + self.nome_usuario + '.csv')

        