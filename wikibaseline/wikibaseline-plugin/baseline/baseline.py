# Baseline plugin
import re

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_stylesheet
from model import Baseline
from model import ItemBaseline
from trac.wiki.model import *
from datetime import datetime
from trac.perm import IPermissionRequestor

class BaselineModule(Component):
	implements(INavigationContributor, ITemplateProvider, IRequestHandler, IPermissionRequestor)

	def get_active_navigation_item(self, req):
		return 'baseline'

	def get_navigation_items(self, req):		
		if 'BASELINE_VIEW' in req.perm('BASELINE'):
			yield ('mainnav', 'baseline', tag.a('Baseline', href=req.href.baseline()))
	
	def match_request(self, req):		
		if 'BASELINE_VIEW' in req.perm('BASELINE'):					
			return re.match(r'/baseline(?:_trac)?(?:/.*)?$', req.path_info)
	
	def get_permission_actions(self):        
		return ['BASELINE_VIEW']
	
	def process_request(self, req):        		       
		nome = req.args.get("nm_baseline")
		comando = req.path_info.rsplit("/",1)[1]
		check = req.args.get("checkbase") 
		comentario = req.args.get("comentario")
		baseline_id = req.args.get("baselineId")
		pes = req.args.get("pesquisa")
		arg = req.args.get("argumento")                 
		autor = req.authname		
		item = ItemBaseline(self.env,baseline_id)                                    	
		baseline = Baseline(self.env,nome,datetime.today(),comentario,autor)                                                   						 
		add_stylesheet(req, 'hw/css/baseline.css')		
				
		if comando == "insert":
			return self.adicionarBaseline(baseline)
		
		if comando == "view":
			return self.visualizarBaseline(item)
		
		if comando == "inserindo":
			return self.inserindoBaseline(baseline,check)
		
		if comando == "pesquisar":
			return self.pesquisarBaseline(baseline,pes,arg)
		  				
		return self.listarBaseline(baseline)

	def listarBaseline(self, baseline):		
		data = {}
		data["dados"] = baseline.popularBaseline()            
		return "baseline.html", data, None
	
	def visualizarBaseline(self, item):		
		data = {}		
		data["dados"] = item.popularItemBaselineByBaselineId()            
		return "visualizarBaseline.html", data, None
	
	def adicionarBaseline(self,baseline):
		data={}
		data["dados"] = baseline.popularWikiPages()
		return "inserirBaseline.html", data, None
	
	def pesquisarBaseline(self,baseline,pes,arg):
		data={}
		if arg == "wiki":
			data["dados"] = baseline.pesquisarBaselineByItemBaseline(pes)
		else:			
			data["dados"] = baseline.pesquisarBaseline(arg,pes)
		return "baseline.html", data, None
		
	def inserindoBaseline(self,baseline,check):
		data={}
		if baseline.inserirBaseline():
			data["info"] = "Cadastro efetuado com sucesso!"
			id = baseline.getBaselineByName()
    		
			for x in check:
				dados = x.split("+")
				itemBase = ItemBaseline(self.env,id[0][0],dados[0],dados[1])
				itemBase.inserirItemBaseline()
		else:
			data["info"] = "Nao foi possivel efetuar cadastro!"                  
		return 'info.html', data, None	
	
	def get_templates_dirs(self):
		from pkg_resources import resource_filename
		return [resource_filename(__name__, 'templates')]
	
	def get_htdocs_dirs(self):
		"""Return a list of directories with static resources (such as style
		sheets, images, etc.)
	
		Each item in the list must be a `(prefix, abspath)` tuple. The
		`prefix` part defines the path in the URL that requests to these
		resources are prefixed with.
	
		The `abspath` is the absolute path to the directory containing the
		resources on the local file system.
		"""
		from pkg_resources import resource_filename
		return [('hw', resource_filename(__name__, 'htdocs'))]
