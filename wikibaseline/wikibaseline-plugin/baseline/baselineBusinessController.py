from model import Baseline
from model import ItemBaseline

class BaselineBusinessController():        
        
    def searchWikiNames(self,baseline,pes):
        data={}
        data["data"] = baseline.getWikiPages(pes)
        return "table.html", data, None
    
    def getBaseline(self, baseline):        
        data = {}
        data["data"] = baseline.getBaseline()            
        return "baseline.html", data, None
    
    def viewBaseline(self, item):        
        data = {}        
        data["data"] = item.getItemBaselineByBaselineId()            
        return "viewBaseline.html", data, None
        
    
    def insertBaseline(self,baseline):
        data={}
        data["data"] = baseline.getWikiPages("")        
        return "insertBaseline.html", data, None
    
    def searchBaseline(self,baseline,pes,arg):
        data={}
        if arg == "wiki":
            data["data"] = baseline.searchBaselineByItemBaseline(pes)
        else:            
            data["data"] = baseline.searchBaseline(arg,pes)
        return "baseline.html", data, None
        
    def infoInsertBaseline(self,baseline,check,env):
        data={}
        if baseline.insertBaseline():
            data["info"] = "Registration done successfully!"
            id = baseline.getBaselineByName()
            
            for x in check:
                wiki = x.split("+")
                itemBase = ItemBaseline(env,id[0][0],wiki[0],wiki[1])
                itemBase.insertItemBaseline()
        else:
            data["info"] = "Could not you register!"                  
        return 'info.html', data, None    