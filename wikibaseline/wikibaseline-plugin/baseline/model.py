#from trac import Component
class Baseline():

    def __init__(self,env = None,nome = None,dt = None,comentario = None,autor = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.nome = nome
        self.dt = dt
        self.comentario = comentario
        self.autor = autor

    def popularBaseline(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT id,nome,data,autor FROM baseline ORDER BY nome;")
            resultset = cursor.fetchall()
            #cursor.execute(sql,(self.id, self.name))
            return resultset    
        except:
            return "Deu errados!"
    
    def pesquisarBaseline(self,arg,pes):
        sql = "SELECT id,nome,data,autor FROM baseline where %s LIKE $f$%s%%$f$;" %(arg,pes) 
        try:            
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Deu errado!"
    
    def pesquisarBaselineByItemBaseline(self,pes):
        sql = "SELECT baseline.id,baseline.nome,baseline.data,baseline.autor FROM itembaseline INNER JOIN baseline ON (baseline_id = id) WHERE wiki_nome LIKE '%s%%';" %pes
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()
            return resultset
        except:
            return "Deu errado!"
	

    def popularWikiPages(self,arg):
        sql = "SELECT DISTINCT name, MAX(version), author FROM wiki WHERE lower(name) LIKE lower('%%%s%%') GROUP BY name,author;" %arg 
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Deu errado!"
    
    def getBaselineByName(self):
        try:
            cursor = self.db.cursor()
            sql = "SELECT id FROM baseline WHERE nome = '%s';" %self.nome
            cursor.execute(sql)
            resultset = cursor.fetchall()
            #cursor.execute(sql,(self.id, self.name))
            return resultset    
        except:
            return "Deu errado!"
            
    
    def inserirBaseline(self):
        sql = "INSERT INTO baseline (nome,data,comentario,autor) VALUES ('%s','%s','%s','%s');" %(self.nome,self.dt,self.comentario,self.autor)    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0

class ItemBaseline(object):
        
    
    def __init__(self,env = None,baseline_id = None, wiki_nome = None, wiki_versao = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.baseline_id = baseline_id
        self.wiki_nome = wiki_nome
        self.wiki_versao = wiki_versao

    def inserirItemBaseline(self):
        sql = "INSERT INTO itembaseline (baseline_id,wiki_nome,wiki_versao) VALUES ('%s','%s','%s');" %(self.baseline_id,self.wiki_nome,self.wiki_versao)    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0
        
    def popularItemBaselineByBaselineId(self):        
        sql = "SELECT * FROM itembaseline where baseline_id = '%s';" %self.baseline_id    
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            resultset = cursor.fetchall()            
            return resultset    
        except:
            return "Deu errado!"
        
