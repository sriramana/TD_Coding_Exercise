<html>
<body>
<header><h3>Treasure Data Coding Exercise</h3></header>
<p>A command line interface wrapper that allows the user to specify:</p>
<ul style="list-style-type:square">
<li>database name 'db_name'</li>
<li>table name 'table_name'</li>
<li>comma separated list of columns 'col_list' as string (e.g. 'column1,column2,column3)</li>
<li>minimum timestamp 'min_time' in unix timestamp or 'NULL'</li>
<li>maximum timestamp 'max_time' in unix timestamp or 'NULL'. Note that max_time must be  min_time or NULL.</li>
<li>query engine: 'hive' or 'presto'</li>
<li>output format: csv or tabular</li>
</ul>

<p>It will run a "SELECT &lt;col_list&gt; FROM &lt;table_name&gt; WHERE TD_TIME_RANGE(time, &lt;min_time&gt;, &lt;max_time&gt;)" query where the arguments in between &lt;&gt; are substituted with the values provided to the command. In particular &lt;min_time&gt; and &lt;max_time&gt; will narrow the SELECT to only a subset of the records in the table specified based on the time column. </p>


<p><b>Usage: query -f csv -e hive -c 'my_col1,my_col2,my_col5' -m min_unixtime -M max_unixtime my_db my_table</b></p>

<pre><code>
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
</code></pre>

</body>
</html>
