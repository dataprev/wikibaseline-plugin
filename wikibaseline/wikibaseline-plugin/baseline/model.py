
class Baseline():

    def __init__(self,env = None,name = None,dt = None,comment = None,author = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.name = name
        self.dt = dt
        self.comment = comment
        self.author = author

    def getBaseline(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id,name,dt,author FROM baseline ORDER BY name;")
            resultset = cursor.fetchall()
            return resultset    
        except:
            return "Error!"
    
    def searchBaseline(self,arg,pes):
        sql = "SELECT id,name,dt,author FROM baseline WHERE lower(%s) LIKE lower('%s%%');" %(arg,pes) 
        try:            
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def searchBaselineByItemBaseline(self,pes):
        sql = "SELECT DISTINCT baseline.id,baseline.name,baseline.dt,baseline.author FROM itembaseline INNER JOIN baseline ON (baseline_id = id) WHERE lower(wiki_name) LIKE lower('%s%%');" %pes
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()
            return resultset
        except:
            return "Error!"
	

    def getWikiPages(self,arg):
        sql = "SELECT DISTINCT name, MAX(version), author FROM wiki WHERE lower(name) LIKE lower('%%%s%%') GROUP BY name,author;" %arg 
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def getBaselineByName(self):
        try:
            cursor = self.db.cursor()
            sql = "SELECT id FROM baseline WHERE name = '%s';" %self.name
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def getLastIdBaseline(self):                
        try:
            cursor = self.db.cursor()
            sql = "SELECT MAX(id) FROM baseline;"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            return resultset
        except:
            return "Error!"            
                
    def insertBaseline(self):
        id = self.getLastIdBaseline()        
        id = id[0][0]
        if id == None:
            sql = "INSERT INTO baseline (id,name,dt,comment,author) VALUES (1,'%s','%s','%s','%s');" %(self.name,self.dt,self.comment,self.author)
        else:            
            sql = "INSERT INTO baseline (id,name,dt,comment,author) VALUES (%i,'%s','%s','%s','%s');" %(id+1,self.name,self.dt,self.comment,self.author)            
        
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0

class ItemBaseline(object):
        
    
    def __init__(self,env = None,baseline_id = None, wiki_name = None, wiki_version = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.baseline_id = baseline_id
        self.wiki_name = wiki_name
        self.wiki_version = wiki_version

    def insertItemBaseline(self):
        sql = "INSERT INTO itembaseline (baseline_id,wiki_name,wiki_version) VALUES ('%s','%s','%s');" %(self.baseline_id,self.wiki_name,self.wiki_version)    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0
        
    def getItemBaselineByBaselineId(self):        
        sql = "SELECT * FROM itembaseline WHERE baseline_id = '%s';" %self.baseline_id    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
        
