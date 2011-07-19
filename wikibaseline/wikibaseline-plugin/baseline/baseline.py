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
		if 'WIKI_BASELINE' in req.perm('wiki'):
			yield ('mainnav', 'baseline', tag.a('Baseline', href=req.href.baseline()))
	
	def match_request(self, req):
		return re.match(r'/baseline(?:_trac)?(?:/.*)?$', req.path_info)
	
	def get_permission_actions(self):        
		return ['WIKI_BASELINE']
	
	def process_request(self, req):        		       
		nome = req.args.get("nm_baseline")
		comando = req.path_info.rsplit("/",1)[1]
		check = req.args.get("checkbase") 
		comentario = req.args.get("comentario")
		baseline_id = req.args.get("baselineId")                
		autor = req.authname
		item = ItemBaseline(self.env,baseline_id)                                    	
		model = Baseline(self.env,nome,datetime.today(),comentario,autor)                                                     						 
				
		if comando == "insert":
			pass
		
		if comando == "view":
			return self.visualizarBaseline(item)
		  		
		return self.listarBaseline(model)

	def listarBaseline(self, model):		
		data = {}
		data["dados"] = model.popularBaseline()            
		return "baseline.html", data, None
	
	def visualizarBaseline(self, model):		
		data = {}		
		data["dados"] = model.popularItemBaselineByBaselineId()            
		return "baseline.html", data, None
	
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
