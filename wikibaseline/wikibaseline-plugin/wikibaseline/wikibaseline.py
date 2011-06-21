import re

from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider

class WikiBaselinePlugin(Component):
    implements(INavigationContributor, IRequestHandler, ITemplateProvider)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'baseline'
    
    def get_navigation_items(self, req):
        yield ('mainnav', 'baseline',
               tag.a('Baseline', href=req.href.baseline()))
    
    # IRequestHandler methods
    def match_request(self, req):
        return re.match(r'/baseline(?:_trac)?(?:/.*)?$', req.path_info)
    
    def process_request(self, req):
        data = {}
        return 'baseline.html', data, None

    def get_templates_dirs(self):
        from pkg_resources import resource_filename
        return [resource_filename(__name__, 'templates')]

#        req.send_response(200)
#        req.send_header('Content-Type', 'text/plain')
#        req.end_headers()
#        req.write('Hello world!')
