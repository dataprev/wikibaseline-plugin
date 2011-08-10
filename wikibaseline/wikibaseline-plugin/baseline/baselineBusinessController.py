from model import Baseline
from model import ItemBaseline

class BaselineBusinessController():                
    """
    Class responsible for control of business rules
    """
    def searchWikiNames(self,baseline,pes):
        """
        Search the wiki pages
        
        .. atribute: baseline
        
        Object Class Baseline
        
        .. atribute: pes
        
        Search term
        
        """
        data={}
        data["data"] = baseline.getWikiPages(pes)
        return "table.html", data, None
    
    def getBaseline(self, baseline):        
        """
        List baselines
        
        .. atribute: baseline
        
        Object Class Baseline             
        
        """
        data = {}
        data["data"] = baseline.getBaseline()            
        return "baseline.html", data, None
    
    def viewBaseline(self, item):        
        """
        Lists the registered items of a baseline
        
        .. atribute: item
        
        Object Class itemBaseline             
        
        """
        data = {}        
        data["data"] = item.getItemBaselineByBaselineId()            
        return "viewBaseline.html", data, None
        
    
    def insertBaseline(self,baseline):
        """
        Inserts a new baseline
        
        .. atribute: baseline
        
        Object Class Baseline             
        
        """
        data={}
        data["data"] = baseline.getWikiPages("")        
        return "insertBaseline.html", data, None
    
    def searchBaseline(self,baseline,pes,arg):
        """
        Search for a baseline
        
        .. atribute: baseline
        
        Object Class Baseline  
        
        .. atribute: arg
        
        Field name that is searched
        
        .. atribute: pes
        
        A term that is searched        
        
        """
        data={}
        if arg == "wiki":
            data["data"] = baseline.searchBaselineByItemBaseline(pes)
        else:            
            data["data"] = baseline.searchBaseline(arg,pes)
        return "baseline.html", data, None
        
    def infoInsertBaseline(self,baseline,check,env):
        """
        Profit for the registration of the new baseline
        
        .. atribute: baseline
        
        Object Class Baseline
        
        .. atribute: check
        
        Values of the registration form checkbox baselines        
        
        """
        data={}            
        #There now exists a baseline registered with that name
        if baseline.insertBaseline() == "existing name":
            data["info"] = "There is a baseline already registered with that name!"
            return 'info.html', data, None
            
        if baseline.insertBaseline():            
            id = baseline.getBaselineByName()
            if isinstance(check, list):
                for x in check:
                    wiki = x.split("+")             
                    itemBase = ItemBaseline(env,id[0][0],wiki[0],wiki[1])
                    itemBase.insertItemBaseline()
            else:
                wiki = check.split("+")        
                itemBase = ItemBaseline(env,id[0][0],wiki[0],wiki[1])
                itemBase.insertItemBaseline()
                
            data["info"] = "Baseline inserted successfully!"
        else:
            data["info"] = "Could not you register!"                  
        return 'info.html', data, None    