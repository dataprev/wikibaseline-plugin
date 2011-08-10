
class Baseline():
    """
    Class responsible for operations in the database on baseline
    """

    def __init__(self,env = None,name = None,dt = None,comment = None,author = None):
        """
        Method builder
        
        .. atritbute: env
        
        .. atribute: name
        
        Name of the baseline
        
        .. atribute: dt
        
        Date of the registration of a baseline
        
        .. atribute: comment
        
        Comments on a baseline                
        
        .. atribute: author
        
        Name the author of the baseline
        
        """
        self.env = env
        self.db = self.env.get_db_cnx()
        self.name = name
        self.dt = dt
        self.comment = comment
        self.author = author

    def getBaseline(self):
        """
        List all baselines
        """
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id,name,dt,author FROM baseline ORDER BY name;")
            resultset = cursor.fetchall()
            return resultset    
        except:
            return "Error!"
    
    def searchBaseline(self,arg,pes):
        """
        Search for a baseline
        
        .. atribute: arg
        
        Field name that is searched
        
        .. atribute: pes
        
        A term that is searched        
        
        """
        sql = "SELECT id,name,dt,author FROM baseline WHERE lower(%s) LIKE lower('%s%%');" %(arg,pes) 
        try:            
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def searchBaselineByItemBaseline(self,arg):
        """
        Search a baseline for wikis that are registered
        
        .. atribute: pes
        
        A term that is searched                  
        
        """
        
        sql = "SELECT DISTINCT baseline.id,baseline.name,baseline.dt,baseline.author FROM itembaseline INNER JOIN baseline ON (baseline_id = id) WHERE lower(wiki_name) LIKE lower('%s%%');" %arg
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()
            return resultset
        except:
            return "Error!"
	

    def getWikiPages(self,arg):
        """
        Search wiki pages
        
        .. atribute: arg
        
        A term that is searched                  
        
        """
        #sql = "SELECT DISTINCT name, MAX(version), author FROM wiki WHERE lower(name) LIKE lower('%%%s%%') GROUP BY name,author;" %arg
        #sql = "SELECT name, MAX(version), author FROM wiki WHERE lower(name) LIKE lower('%%%s%%') GROUP BY name;" %arg
        sql = "SELECT n.name,a.version,a.author from (select name,max(version) as version from wiki group by name) n, wiki a WHERE a.name = n.name AND a.version = n.version AND lower(n.name) LIKE lower('%%%s%%')  order by 1,2;" %arg
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def getBaselineByName(self):
        """
        Search by name a baseline
        """
        try:
            cursor = self.db.cursor()
            sql = "SELECT id FROM baseline WHERE name = '%s';" %self.name
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
    
    def getLastIdBaseline(self):                
        """
        Returns the last record id Inserts a new baseline
        """
        try:
            cursor = self.db.cursor()
            sql = "SELECT MAX(id) FROM baseline;"
            cursor.execute(sql)
            resultset = cursor.fetchall()
            return resultset
        except:
            return "Error!"            
                
    def insertBaseline(self):
        """
        Inserts a new baseline
        """
        id = self.getLastIdBaseline()        
        id = id[0][0]
        if self.getBaselineByName().__len__() != 0:
            return "existing name"
        else:            
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
    """
    Class responsible for operations in the database on itemBaseline
    """    
    
    def __init__(self,env = None,baseline_id = None, wiki_name = None, wiki_version = None):
        """
        Method builder
        
        .. atritbute: env
        
        .. atribute: baseline_id
        
        Reference to the id of a baseline
        
        .. atribute: wiki_name, wiki_version
        
        Reference to a wiki page
                
        """
        self.env = env
        self.db = self.env.get_db_cnx()
        self.baseline_id = baseline_id
        self.wiki_name = wiki_name
        self.wiki_version = wiki_version

    def insertItemBaseline(self):
        """
        Inserts a new itemBaseline
        """
        sql = "INSERT INTO itembaseline (baseline_id,wiki_name,wiki_version) VALUES ('%s','%s','%s');" %(self.baseline_id,self.wiki_name,self.wiki_version)    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0
        
    def getItemBaselineByBaselineId(self):        
        """
        Itembaseline search for a baseline by id
        """
        sql = "SELECT * FROM itembaseline WHERE baseline_id = '%s';" %self.baseline_id    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Error!"
        
