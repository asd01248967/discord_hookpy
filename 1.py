data = {
    {'status': 'firing', 'labels': {'alertname': 'hostCpuUsageAlert', 'instance': '172.31.38.32:9100', 'severity': 'page'}, 'annotations': {'description': '172.31.38.32:9100 CPU usage above 85% (current value: 0.9999999999999942)', 'summary': 'Instance 172.31.38.32:9100 CPU usgae high'}, 'startsAt': '2020-02-25T09:54:26.907228146Z', 'endsAt': '0001-01-01T00:00:00Z', 'generatorURL': 'http://ip-172-31-36-163.ap-northeast-1.compute.internal:9090/graph?g0.expr=sum+by%28instance%29+%28avg+without%28cpu%29+%28irate%28node_cpu_seconds_total%7Bmode%21%3D%22idle%22%7D%5B5m%5D%29%29%29+%3E+0.85&g0.tab=1', 'fingerprint': '2def8978503d35a8'},
    {'status': 'firing', 'labels': {'alertname': 'hostCpuUsageAlert', 'instance': 'localhost:9100', 'severity': 'page'}, 'annotations': {'description': 'localhost:9100 CPU usage above 85% (current value: 0.9989989989989553)', 'summary': 'Instance localhost:9100 CPU usgae high'}, 'startsAt': '2020-02-25T09:54:26.907228146Z', 'endsAt': '0001-01-01T00:00:00Z', 'generatorURL': 'http://ip-172-31-36-163.ap-northeast-1.compute.internal:9090/graph?g0.expr=sum+by%28instance%29+%28avg+without%28cpu%29+%28irate%28node_cpu_seconds_total%7Bmode%21%3D%22idle%22%7D%5B5m%5D%29%29%29+%3E+0.85&g0.tab=1', 'fingerprint': '7d698ac9afe034a7'}
}

print(data)

