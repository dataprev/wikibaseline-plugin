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
            cursor.execute("SELECT DISTINCT name, MAX(version), author FROM wiki GROUP BY name,author;")
            resultset = cursor.fetchall()
            #cursor.execute(sql,(self.id, self.name))
            return resultset    
        except:
            return "Deu errado!"
    
    def getBaselineByName(self,nome):
        try:
            cursor = self.db.cursor()
            sql = "SELECT id FROM baseline WHERE nome = '%s';" %nome
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

class itemBaseline():
    
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
