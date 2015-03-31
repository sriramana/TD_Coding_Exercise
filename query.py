import os
import tdclient
import time

apikey = os.getenv("TD_API_KEY")

with tdclient.Client(apikey) as client:
	job=client.query("sample_datasets","SELECT symbol,time,volume FROM NASDAQ WHERE symbol = 'WLFC' AND TD_TIME_RANGE(time,1388534400,1391126400)")
	while not job.finished():
		time.sleep(2)
	for row in job.result_format('csv'):
		print row