
import os
import sys

comd1 = "python setup.py bdist_egg"
comd2 = "cp /home/guilherme/udsl/wikibaseline/wikibaseline-plugin/dist/Baseline-1.1-py2.7.egg /home/guilherme/pTrac/plugins/"
comd3 = "tracd -p 8000 --basic-auth='pTrac,/home/guilherme/pTrac/.htpasswd,pTrac' /home/guilherme/pTrac"
os.system(comd1)
os.system(comd2)
os.system(comd3)


