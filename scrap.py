import requests
from lxml import html
import pickle
#import logging
#import http.client as http_client

#http_client.HTTPConnection.debuglevel = 1

#logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
#requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

class SIGAA:
	"""Acessa SIGGA para retorno das turmas"""
	listaTurmas = []

	def __init__(self):
		pass

	def retorna_turmas():

		with requests.Session() as c:
		    url = 'https://sigaa.unifei.edu.br/sigaa/logar.do?dispatch=logOn'
		    USERNAME = '35072984818'
		    PASSWORD = '@Ftp1992ftp'
		    c.get(url)
		    login_data = {
			'user.login': USERNAME,
			'user.senha': PASSWORD,
			'width': '1366',
			'heigth': '768',
			'urlRedirect': '',
			'subsistemaRedirect': '',
			'acao': '',
			'acessibilidade': ''
		    }
		    c.post(url, data=login_data, headers={"Referer": "https://sigaa.unifei.edu.br/sigaa/verTelaLogin.do"})

		    search_data = {
			'form':'form',
			'form:checkNivel':'on',
			'form:selectNivelTurma':'G',
			'form:checkAnoPeriodo':'on',
			'form:inputAno':'2018',
			'form:inputPeriodo':'1',
			'form:checkUnidade':'on',
			'form:selectUnidade':'254',
			'form:inputCodDisciplina':'',
			'form:inputCodTurma':'',
			'form:inputLocal':'',
			'form:inputHorario':'',
			'form:inputNomeDisciplina':'',
			'form:inputNomeDocente':'',
			'form:checkCurso':'on',
			'form:selectCurso':'43969913',
			'form:selectSituacaoTurma':'1',
			'form:selectTipoTurma':'0',
			'form:selectModalidade':'0',
			'form:selectOpcaoOrdenacao':'1',
			'turmasEAD':'false',
			'form:buttonBuscar':'Buscar',
			'javax.faces.ViewState':'j_id2'
		    }

		    url_busca = 'https://sigaa.unifei.edu.br/sigaa/ensino/turma/busca_turma.jsf'
		    c.get(url_busca)
		    resposta = c.post(url_busca, data=search_data)

		    tree = html.fromstring(resposta.content)

		    listaTurmas = tree.xpath('//*[@id="lista-turmas"]/tbody/tr[not(contains(@style,"display:none"))]/*/text()')

		    disciplinas = tree.xpath('//*[@id="lista-turmas"]/tbody/tr[contains(@class,"destaque")]/td/text()')

		    disciplinas = [w.replace('\t', '').replace('\n', '').strip() for w in disciplinas]

		    disciplinas = list(filter(None, disciplinas))

		    #print(disciplinas)

		    listaTurmas = [w.replace('\t', '').replace('\n', '').strip() for w in listaTurmas]

		    listaTurmas = list(filter(None, listaTurmas))

		    #print('Lista das Turmas: \n', listaTurmas)

		    #codCursos = tree.xpath('//*[@id="form:selectCurso"]/*/@value')
		    #cursos = tree.xpath('//*[@id="form:selectCurso"]/*/text()')

		    #print('Codigos dos Cursos: \n', codCursos)
		    #print('Cursos: \n', cursos)
		return listaTurmas, disciplinas

	def format(detalhes, disciplinas):
		from collections import defaultdict

		d = defaultdict(list)
		subjects = set(disciplinas)

		for item in detalhes:
		    if item in subjects:
		        current_item = item
		    else:
		        d[current_item].append(item)
		return d

	#def separa_turma():
		

	def save_obj(obj, name ):
	    with open('obj/'+ name + '.pkl', 'wb') as f:
	        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL) # pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

	def load_obj(name):
	    with open('obj/' + name + '.pkl', 'rb') as f:
	        return pickle.load(f)
