#from trac import Component
class Baseline():

    def __init__(self,env = None,nome = None,dt = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.nome = nome
        self.dt = dt

    def popularBaseline(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT DISTINCT name, MAX(version), author FROM wiki WHERE author<>'trac' GROUP BY name,author;")
            resultset = cursor.fetchall()
            #cursor.execute(sql,(self.id, self.name))
            return resultset    
        except:
            return "Deu errado!"
    
    def inserirBaseline(self):
        sql = "INSERT INTO baseline (nome) VALUES ('%s');" %self.nome    

        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()                                        
            return 1
        except:
            return 0