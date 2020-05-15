
class Equipe():

    def getContext(self):
        return self.__contextEquipe(self)
    
    def __parceiros(self):
        parceiros = [
            {  
                "nome": "#TodosContraoCorona",
                "short": "todoscontraocorona",
                "url": "https://www.facebook.com/centrouniversitariodemineiros",
                "plataforma": "Facebook",
                "content": "Projeto de conscientização diária em relação ao combate ao Covid-19 promovido pela Unifimes."
            },
            {
                "nome":	"Covid Goiás",
                "short": "covid-goias",
                "url": "https://covidgoias.ufg.br/",
                "plataforma": "Link",
                "content": "Observatório estadual conduzido pelo LAPIG-UFG com dados sobre o Covid-19 do estado de Goiás."
            }
        ]
        return parceiros

    def __participantes(self):
        participantes = [
            {
                "nome": "Prof. Esdras L. Bispo Jr.",
                "short": "esdras",
                "url": "http://lattes.cnpq.br/1022072289836952",
                "plataforma": "Lattes",
                "content": "Idealizador do Observatório. Pesquisador na área de Educação e Inteligência Artificial"
            },
            {
                "nome": "Profa. Joslaine Jeske",
                "short": "joslaine",
                "url": "http://lattes.cnpq.br/2394348610492496",
                "plataforma": "Lattes",
                "content": "Responsável pelos dados da cidade de Rio Verde. Pesquisadora na área de Inteligência Artificial."
            },
            {
                "nome":	"Profa. Franciny Medeiros",
                "short": "franciny",
                "url": "http://lattes.cnpq.br/2821748091466181",
                "plataforma": "Lattes",
                "content": "Responsável pelos dados de Jataí e pela comunicação. Pesquisadora na área de Engenharia de Software."
            },
            {
                "nome":	"Prof. Márcio Lopes",
                "short": "marcio",
                "url": "http://lattes.cnpq.br/8846703586256426",
                "plataforma": "Lattes",
                "content": "Responsável pelos dados da cidade de Mineiros. Pesquisador na área de Computação em Névoa."
            },
            {
                "nome":	"Prof. Marcelo Freitas",
                "short": "marcelo",
                "url": "http://lattes.cnpq.br/0972390630476077",
                "plataforma": "Lattes",
                "content": "Responsável pelas notícias em relação ao Covid-19. Pesquisa sobre Sistemas Operacionais."
            },
            {
                "nome": "Prof. Zaqueu Souza",
                "short": "zaqueu",
                "url": "http://lattes.cnpq.br/8132493439297747",
                "plataforma": "Lattes",
                "content": "Colaborador-parceiro do Todos Contra o Corona. Professor de Engenharia Ambiental na Unifimes."
            },
            {
                "nome":	"Profa. Edlaine Vilela",
                "short": "edlaine",
                "url": "http://lattes.cnpq.br/8767578610764666",
                "plataforma": "Lattes",
                "content": "Consultora sobre questões epidemiológicas. Professora de Medicina na UFJ."
            },
            {
                "nome": "Prof. Manuel Ferreira",
                "short": "manuel",
                "url": "http://lattes.cnpq.br/4498594723433539",
                "plataforma": "Lattes",
                "content": "Colaborador-parceiro do Covid-Goiás. Professor da área de Geoprocessamento na UFG."
            },
            {
                "nome": "Prof. Luiz Pascoal",
                "short" :"luiz",
                "url": "http://lattes.cnpq.br/9189310566441445",
                "plataforma": "Lattes",
                "content": "Colaborador-parceiro do Covid-Goiás. Professor da área de Sistemas Distribuídos no SENAI."
            },
            {
                "nome": "Diego Costa",
                "short" :"diego",
                "url": "https://www.diegocosta.dev/",
                "plataforma": "Link",
                "content": "Colaborador no desenvolvimento da página. Analista Programador na Unimed na cidade de Rio Verde."
            },
            {
                "nome": "Felipe Nedopetalski",
                "short": "felipe",
                "url": "https://www.linkedin.com/in/felipe-nedopetalski-91b93b154/",
                "plataforma": "LinkedIn",
                "content": "Colaborador no desenvolvimento da página. Graduando em Ciências da Computação na UFJ."
            },
            {
                "nome": "Gabriel Santos",
                "short": "gabriel",
                "url": "https://www.linkedin.com/in/dev-gabriel-santos/",
                "plataforma": "LinkedIn",
                "content": "Colaborador no desenvolvimento da página. Graduando em Ciências da Computação na UFJ."
            }
        ]
        return participantes

    def __contextEquipe(self):
        context = {
            "script": "geral",
            "grupo": "equipe",
            "grupo_link": "saiba_mais",
            "titulo": "Observatório UFJ Covid-19 - Equipe",
            "parceiros": self.__parceiros(self),
            "querysets": self.__participantes(self)
        }
        return context

        