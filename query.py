import os
import tdclient
import time
import argparse
apikey = os.getenv("TD_API_KEY")
parser = argparse.ArgumentParser()
parser.add_argument('--engine','-e',default='presto',choices=['presto','hive'])
parser.add_argument('--format','-f',default='tsv')
parser.add_argument('--column_names','-c',default='*')
parser.add_argument('--min','-m',default='NULL')
parser.add_argument('--MAX','-M',default='NULL')
parser.add_argument('database_name')
parser.add_argument('table_name')
args= parser.parse_args()
database = args.database_name
query_type = args.engine
file_type = args.format
table = args.table_name
column = args.column_names
minimum = args.min
maximum = args.MAX

if minimum == 'NULL':
	minimum = str(0)

if maximum == 'NULL':
	maximum = str(253402300799)
	
with tdclient.Client(apikey) as client:
	job=client.query(database,"SELECT " +column+" FROM "+table+" WHERE symbol = 'WLFC' AND TD_TIME_RANGE(time,"+minimum+","+maximum+")", type=query_type)
	while not job.finished():
		time.sleep(2)
	f = open("query_results."+file_type,"w")
	for row in job.result_format(file_type):
		print row
		f.write(row+"\n")
	f.close()