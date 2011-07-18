# Baseline plugin
import re

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_stylesheet
from model import Baseline

class BaselineModule(Component):
    implements(INavigationContributor, ITemplateProvider, IRequestHandler)

    def get_active_navigation_item(self, req):
        return 'baseline'

    def get_navigation_items(self, req):
        yield ('mainnav', 'baseline',
               tag.a('Baseline', href=req.href.baseline()))


    def match_request(self, req):
        return re.match(r'/baseline(?:_trac)?(?:/.*)?$', req.path_info)

    def process_request(self, req):
        data = {}
        nome = req.args.get("nm_baseline")
        dt = req.args.get("dt_baseline")
        add_stylesheet(req, 'hw/css/baseline.css')
        model = Baseline(self.env,nome,dt) 
        data["teste"] = model.create()
        # This tuple is for Genshi (template_name, data, content_type)
        # Without data the trac layout will not appear.                
        return 'baseline.html', data, None
     
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
