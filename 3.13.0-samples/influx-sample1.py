import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "_UEBXXlTyi_FCT-kCeKKx2JPitc4c61G7REwyGcSLY-X1fMmdrLChdJ2m0c2xnaP6IX9zoDe_cqWoKj4S4ySlg=="
org = "test"
url = "http://localhost:8086/"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="testbucket"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org="test", record=point)
  time.sleep(1) # separate points by 1 second
