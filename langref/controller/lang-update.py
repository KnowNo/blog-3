import sys
import os
import sqlite3
from string import Template
import tempfile
import logging

#TODO: error handling

# set log
FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('lang-update.py')
#logger.setLevel(20)

# get input language and construct
scriptName = os.path.basename(sys.argv[0])
assert len(sys.argv) == 3, 'Incorrect syntax, should be: %s <language> <construct>' % scriptName
language = sys.argv[1]
construct = sys.argv[2]

# retrieve data if exist
dbFile = os.path.realpath(os.path.join(sys.argv[0], '../../model/langref.sdb'))
logger.info("Database file: " + dbFile)
conn = sqlite3.connect(dbFile)
c = conn.cursor()
t = (language, construct)
c.execute("select * from langref where language_name=? and construct_name=?", t)
row = c.fetchone()

# Show data in a text file for edit
d = dict(language_name=language, construct_name=construct)
d['snippet'] = row[2] if row else ''
d['comment'] = row[3] if row else ''
s = Template(
"""
language_name = '$language_name'

construct_name = '$construct_name'

snippet = '''
$snippet
'''

comment = '''
$comment
'''
"""
)
content = s.substitute(d)

temp = tempfile.NamedTemporaryFile(delete=False)
print temp.name
temp.write(content)
temp.close()
import subprocess
subprocess.call(['notepad', temp.name])

ns = {}
execfile(temp.name, ns)
logger.info(ns['language_name'])

# now let's write the data back to database
statement = ''
if row:
    statement = "update langref set snippet='%s', comment='%s'" % \
        (ns['snippet'], ns['comment'])
else:
    statement = "insert into langref values('%s', '%s', '%s', '%s')" % \
        (ns['language_name'], ns['construct_name'], ns['snippet'], ns['comment'])
        
statement =  statement + " where language_name='%s' and construct_name='%s'" % (language, construct)
logger.info("The update statement is: " + statement)

c.execute(statement)
conn.commit()
conn.close()
    

