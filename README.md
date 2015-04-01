# TD_Coding_Exercise
Treasure Data Coding Exercise
A command line interface wrapper that allows the user to specify:
•database name 'db_name'
•table name 'table_name'
•comma separated list of columns 'col_list' as string (e.g. 'column1,column2,column3)
•minimum timestamp 'min_time' in unix timestamp or 'NULL'
•maximum timestamp 'max_time' in unix timestamp or 'NULL'. Note that max_time must be  min_time or NULL.
•query engine: 'hive' or 'presto'
•output format: csv or tabular
and it will run a "SELECT <col_list> FROM <table_name> WHERE TD_TIME_RANGE(time, <min_time>, <max_time>)" query where the arguments in between <> are substituted with the values provided to the command. In particular <min_time> and <max_time> will narrow the SELECT to only a subset of the records in the table specified based on the time column. 


Usage: query -f csv -e hive -c 'my_col1,my_col2,my_col5' -m 1427347140 -M 1427350725 my_db my_table

PS C:\Users\sramana\Documents\GitHub\TD_Coding_Exercise> ./query -h
usage: query.py [-h] [--engine {presto,hive}] [--format {csv,tsv}]
                [--column_names COLUMN_NAMES] [--min MIN] [--MAX MAX]
                database_name table_name

positional arguments:
  database_name         Required argument for database name
  table_name            Required argument for table name

optional arguments:
  -h, --help            show this help message and exit
  --engine {presto,hive}, -e {presto,hive}
                        Select hive or presto as query engine, if not defined
                        default is hive
  --format {csv,tsv}, -f {csv,tsv}
                        Optional export file format: either csv or tsv.
                        Default is tabular
  --column_names COLUMN_NAMES, -c COLUMN_NAMES
                        Optional column selector and accepts a comma separate
                        list of columns if not defined default is all columns
  --min MIN, -m MIN     Optional minimum timestamp. NULL by default
  --MAX MAX, -M MAX     Optional maximum timestamp. NULL by default
