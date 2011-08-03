# -*- coding: utf-8 -*-

from trac.core import *
from trac.env import IEnvironmentSetupParticipant
from trac.db import Table, Column, Index


class BaselineProvider(Component):
    implements(IEnvironmentSetupParticipant)
    
    SCHEMA = [
        Table('baseline', key = ('id'))[
              Column('id','serial'),
              Column('name','varchar'),
              Column('dt','timestamp'),
              Column('comment'),
              Column('author','varchar'),              
              ],
        Table('itembaseline', key = ('baseline_id','wiki_name','wiki_version'))[
              Column('baseline_id','int'),
              Column('wiki_name','varchar'),
              Column('wiki_version','int'),
              ]
        ]

    # IEnvironmentSetupParticipant methods
    def environment_created(self):
        self._upgrade_db(self.env.get_db_cnx())

    def environment_needs_upgrade(self, db):
        cursor = db.cursor()
        #if self._need_migration(db):
        #    return True
        try:
            cursor.execute("select count(*) from baseline")
            cursor.fetchone()
            return False
        except:
            db.rollback()
            return True

    def upgrade_environment(self, db):
        self._upgrade_db(db)
        
    def _upgrade_db(self, db):
        try:
            try:
                from trac.db import DatabaseManager
                db_backend, _ = DatabaseManager(self.env)._get_connector()
            except ImportError:
                db_backend = self.env.get_db_cnx()

            cursor = db.cursor()
            for table in self.SCHEMA:
                for stmt in db_backend.to_sql(table):
                    self.env.log.debug(stmt)
                    cursor.execute(stmt)                        
            cursor.execute("ALTER TABLE baseline ADD CONSTRAINT fk_baseline_name UNIQUE (name);")
            cursor.execute("ALTER TABLE baseline ALTER COLUMN name SET NOT NULL;")
            cursor.execute("ALTER TABLE itembaseline ADD constraint fk_baseline_id foreign key (baseline_id) references baseline (id),\
                            ADD constraint fk_wiki foreign key (wiki_name, wiki_version) references wiki (name,version);")
            cursor.execute("INSERT INTO permission (username,action)VALUES('authenticated','BASELINE_VIEW');")
            db.commit()

        except:
            db.rollback()
            raise
