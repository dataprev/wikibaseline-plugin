# -*- coding: utf-8 -*-

import logging
from suds import WebFault
from suds.client import Client
from suds.sax.attribute import Attribute
from suds.sax.text import Raw
from xml.dom.minidom import *

# intializers
XSD_DIR = '../xsd/'
XSD_EXT = '.xsd'
EXT_SOURCE = 'NIKU'
DEBUG = True

class NikuData(object):
	"""
	Nikudata main class. Among others things it's  handler to webservice
	communication, error handling and request and response. Beside it also handle
	XML building. 
	"""
	no_namespace_schema_location = XSD_DIR+'nikuxog_timeperiod'+XSD_EXT
	object_type = 'projects'
	xlmns = 'http://www.w3.org/2001/XMLSchema-instance'
	document_root = 'NikuDataBus'
	def __init__(self):

		self.action = 'read'

		# the minidom ref
		try:
			self.md = Document()
		except ImportError, e:
			print 'it was impossible getting a XML handler'

	def _build_header(self):
		# The niku root Element
		# There is a strange behavior in NikuDataBus whereas we haven't a WSDL
		# complexType to define NikuDataBus structure, although we need to
		# building a xml request based on XSD. I guess it wasn't clear, but
		# that's it!!!  
		niku_root = self.md.createElement(self.document_root)
		self.md.appendChild(niku_root)
		self.action = self.mode

	@property
	def action(self):
		return self._action

	@action.setter
	def action(self, value):
		niku_root = self.md.getElementsByTagName(self.document_root)[0]
		niku_root.setAttribute('action',value)

	@action.getter
	def action(self):
		return self._action

	def __repr__(self):
		return self.md.toprettyxml()

if __name__ == '__main__':
	n = NikuData()
	n._build_header()
	print n.action
	print n
