# -*- coding: utf-8 -*-

import logging
from suds import WebFault
from suds.xsd.doctor import Import,  ImportDoctor
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.plugin import MessagePlugin
from suds.sax.text import Raw
from xml.dom.minidom import *

#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)

ID_PROJETO = 'Teste_Aula05'

class NikuDataBus:
	niku_args = {
		'include_tasks': 'true'
		,'include_dependencies': 'false'
		,'include_subprojects': 'false'
		,'include_resources': 'false'
		,'include_custom': 'false'
	}
	def __init__(self,projectID='001', mode='read'):
		self.mode = mode
		doc = Document()

		self.global_xml = doc
		niku_root = doc.createElement("NikuDataBus")
		
		self.niku_data_bus = niku_root

		niku_root.setAttribute('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
		niku_root.setAttribute('xsi:noNamespaceSchemaLocation','../xsd/nikuxog_read.xsd')
		niku_header = doc.createElement("Header")
		niku_header.setAttribute('version','6.0.11')
		niku_header.setAttribute('action', self.mode)
		niku_header.setAttribute('objectType','project')
		niku_header.setAttribute('externalSource','NIKU')
		niku_root.appendChild(niku_header)

		self.set_args_header(niku_header)
		self.set_query('projectID',projectID)

		doc.appendChild(niku_root)

	def set_args(self,arg,value,node):
		el = self.global_xml.createElement('args')
		el.setAttribute('name',arg)
		el.setAttribute('value',value)
		node.appendChild(el)

	def set_args_header(self,node):
		for k,v in self.niku_args.iteritems():
			el = self.global_xml.createElement('args')
			el.setAttribute('name',k)
			el.setAttribute('value',v)
			node.appendChild(el)

	def set_query(self,att_filter,att_value):
		el = self.make_element('Query')
		el_filter = self.make_element('Filter')
		el_filter.setAttribute('criteria','EQUALS')
		self.create_content(att_value,el_filter)
		el_filter.setAttribute('name',att_filter)
		self.niku_data_bus.appendChild(el)
		el.appendChild(el_filter)

	def make_element(self,el):
		et = self.global_xml.createElement(el)
		return et

	def create_content(self,content,node):
		ct = self.global_xml.createTextNode(content)
		node.appendChild(ct)

	def __str__(self):
		return self.global_xml.toxml()

project = NikuDataBus('Teste_Aula05')
imp = Import('http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add('http://www.nikus.com/xog/Projects')
imp.filter.add('http://www-dprojetos/niku/xog')
d = ImportDoctor(imp)

URL = "http://www-dprojetos/niku/wsdl/Object/Projects"

client = Client(URL)

try:
	id = client.service.Login('d339954', 'foobar')
	auth = client.factory.create("Auth")
	auth.SessionID = id
	client.set_options(soapheaders=auth)


	xml_w = """
<NikuDataBus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../xsd/nikuxog_timeperiod.xsd">
    <Header version="6.0.11" action="write" objectType="timeperiod" externalSource="NIKU"/>
	<TimePeriods>
	 <TimePeriod finish="2011-05-22T00:00:00" start="2011-05-16T00:00:00">
            <TimeSheets>
                <TimeSheet ID="-1" resourceID="d339954" version="1" action="add" status="0">
                    <TimeSheetEntries>
                        <TimeSheetEntry  assignmentFinish="2011-05-16T17:00:00" assignmentStart="2011-05-16T08:00:00" chargeCodeID="08. Secretaria" projectID="Teste_Aula05" taskID="00000478">
                            <DailyActuals>
                                <Actual actualDate="2011-05-16" amount="2"/>
                                <Actual actualDate="2011-05-17" amount="4"/>
                                <Actual actualDate="2011-05-18" amount="4"/>
                                <Actual actualDate="2011-05-19" amount="2"/>
                                <Actual actualDate="2011-05-20" amount="3"/>
                                <Actual actualDate="2011-05-21" amount="2"/>
                                <Actual actualDate="2011-05-22" amount="2"/>
							</DailyActuals>
					     </TimeSheetEntry>                       
                    </TimeSheetEntries>
			    </TimeSheet>
           </TimeSheets>
     </TimePeriod>
  </TimePeriods>
</NikuDataBus>
"""


	xml_r = """
<NikuDataBus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../xsd/nikuxog_read.xsd">
    <Header version="6.0.11" action="read" objectType="timeperiod" externalSource="NIKU"/>
    <Query>
        
<!--    <Filter name="start" criteria="BETWEEN">2011-06-08, 2011-06-14</Filter>
-->
    <Filter name="resourceID" criteria="EQUALS">d339954</Filter>
<!--
        <Filter name="resourceID" criteria="EQUALS">XOGProg1Res</Filter>
        <Filter name="status" criteria="EQUALS">4</Filter>
        <Filter name="modifiedDate" criteria="AFTER">2002-01-01T15:36:03</Filter>
        <Filter name="includeAdjusted" criteria="EQUALS">true</Filter>
        <Filter name="createTimesheet" criteria="EQUALS">true</Filter>
    -->
    </Query>
</NikuDataBus>

"""
	xml_projects = """
<NikuDataBus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../xsd/nikuxog_read.xsd">
  <Header version="6.0.11" action="read" objectType="project" externalSource="NIKU">
    <!-- you change the order by simply swap 1 and 2 number in the name attribute -->
    <args name="order_by_1" value="name"/>
    <args name="order_by_2" value="projectID"/>
    <args name="include_tasks" value="true"/>
  </Header>
  <Query>
  <Filter name="projectID" criteria="EQUALS">Teste_Aula05</Filter>
  </Query>
</NikuDataBus>

"""

	sql = """
<NikuDataBus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xsi:noNamespaceSchemaLocation="../xsd/nikuxog_read.xsd">
<Header action="read" externalSource="NIKU" objectType="project" 
version="6.0.11">
<args name="order_by_1" value="name"/>
<args name="order_by_2" value="projectID"/>
<args name="include_tasks" value="true"/>
</Header>
<Query>
<Filter criteria="EQUALS" name="projectID">Teste_Aula05</Filter>
</Query>
</NikuDataBus>

"""

   #hack! hugh! python minidom wrappers doesn't accept xml-declaration headers.
   # see DOM specification for more information or implement NikuDataBus using
	# ElementTree or lxml2
	raw = project.__str__().replace('<?xml version="1.0" ?>','')

#	rp = client.service.WriteTimeperiod(Raw(xml_w))

	rp = client.service.ReadProject(Raw(sql))
	print rp

	client.service.Logout(id)
except WebFault, e:
 	print e

