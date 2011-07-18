class Baseline(object):

    def __init__(self,env = None,nome = None,dt = None):
        self.env = env
        self.db = self.env.get_db_cnx()
        self.nome = nome
        self.dt = dt

    def create(self):
        try:
            cursor = self.db.cursor()
            cursor.execute("SELECT name,version FROM wiki WHERE author<>'trac' ORDER BY name,version;")
            resultset = cursor.fetchall()
            #cursor.execute(sql,(self.id, self.name))
            return resultset
        except:
            return "Deu errado!"
