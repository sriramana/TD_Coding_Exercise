import os
import tdclient
import time
import argparse

apikey = os.getenv("TD_API_KEY")
#Parsing Command Line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('--engine','-e',default='presto',choices=['presto','hive'], help="Select hive or presto as query engine, if not defined default is hive")
parser.add_argument('--format','-f',default='tsv', choices=['csv','tsv'], help="Optional export file format: either csv or tsv. Default is tabular")
parser.add_argument('--column_names','-c',default='*', help="Optional column selector and accepts a comma separate list of columns if not defined default is all columns")
parser.add_argument('--min','-m',default='NULL', help="Optional minimum timestamp. NULL by default")
parser.add_argument('--MAX','-M',default='NULL', help="Optional maximum timestamp. NULL by default")
parser.add_argument('database_name', help="Required argument for database name")
parser.add_argument('table_name', help="Required argument for table name")
args= parser.parse_args()
database = args.database_name
query_type = args.engine
file_type = args.format
table = args.table_name
column = args.column_names
minimum = args.min
maximum = args.MAX
# Modifiying Min time and Max time from NULL to unixtimestamps
if minimum == 'NULL':
	minimum = str(0)

if maximum == 'NULL':
	maximum = str(253402300799)

#TD Python API for Query	
with tdclient.Client(apikey) as client:
	job=client.query(database,"SELECT " +column+" FROM "+table+" WHERE symbol = 'WLFC' AND TD_TIME_RANGE(time,"+minimum+","+maximum+")", type=query_type)
	while not job.finished():
		time.sleep(2)
	f = open("query_results."+file_type,"w")
	for row in job.result_format(file_type):
		print row
		f.write(row+"\n")
	f.close()