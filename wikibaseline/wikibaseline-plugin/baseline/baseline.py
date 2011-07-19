# Baseline plugin
import re

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_stylesheet
from model import Baseline
from model import itemBaseline
from trac.wiki.model import *
from datetime import datetime
from trac.perm import IPermissionRequestor

class BaselineModule(Component):
	implements(INavigationContributor, ITemplateProvider, IRequestHandler, IPermissionRequestor)

	def get_active_navigation_item(self, req):
		return 'baseline'

	def get_navigation_items(self, req):
		if 'WIKI_BASELINE' in req.perm('wiki'):
			yield ('mainnav', 'baseline', tag.a('Baseline', href=req.href.baseline()))
	
	def match_request(self, req):
		return re.match(r'/baseline(?:_trac)?(?:/.*)?$', req.path_info)
	
	def get_permission_actions(self):        
		return ['WIKI_BASELINE']
	
	def process_request(self, req):        
		data = {}          
		nome = req.args.get("nm_baseline")
		op = req.path_info.rsplit("/")[1]
		check = req.args.get("checkbase") 
		comentario = req.args.get("comentario")                
		autor = req.authname                                    	
		model = Baseline(self.env,nome,datetime.today(),comentario,autor)                                                     
		if op == "listar":            
			return self.listarBaseline(model)
	
	
		elif:        
			pass
		if model.inserirBaseline():
			data["info"] = "Cadastro efetuado com sucesso!"
			id = model.getBaselineByName(nome)
	
			for x in check:
				dados = x.split("+")
				itemBase = itemBaseline(self.env,id[0][0],dados[0],dados[1])
				itemBase.inserirItemBaseline()           
		else:
			data["info"] = "Nao foi possivel efetuar cadastro!"          
			return 'teste.html', data, None
	
	
		# This tuple is for Genshi (template_name, data, content_type)
		# Without data the trac layout will not appear.                
		add_stylesheet(req, 'hw/css/baseline.css')
		return 'baseline.html', data, None        
	
	def listarBaselines(self,model):
		data["dados"] = model.popularBaseline()		    
		return "baseline.html",data,None

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
