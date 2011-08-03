# Baseline plugin
import re

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_stylesheet, add_script
from model import Baseline
from model import ItemBaseline
from baselineBusinessController import *
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
		name = req.args.get("name")
		command = req.path_info.rsplit("/",1)[1]
		check = req.args.get("checkbase")  
		comment = req.args.get("comment")
		baseline_id = req.args.get("baselineId")
		termsearch = req.args.get("termsearch")
		wiki_name = req.args.get("wiki_name")		
		arg = req.args.get("arg")		               
		author = req.authname		
		item = ItemBaseline(self.env,baseline_id)                                    	
		baseline = Baseline(self.env,name,datetime.today(),comment,author) 
		bbc = BaselineBusinessController()                                                  						 			
		add_stylesheet(req, 'hw/css/baseline.css')				
		
		if command == "insert":
			return bbc.insertBaseline(baseline)
		
		if command == "view":
			return bbc.viewBaseline(item)
		
		if command == "info":			
			return bbc.infoInsertBaseline(baseline,check,self.env)
		
		if command == "search":
			return bbc.searchBaseline(baseline,termsearch,arg)
		
		if command == "searchWikiNames":
			return bbc.searchWikiNames(baseline,wiki_name)
		  				
		return bbc.getBaseline(baseline)		
	
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
