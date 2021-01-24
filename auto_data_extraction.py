import os, json

META = None
PATH = os.path.dirname(os.path.realpath(__file__))

with open(f'{PATH}/META.json') as fp:
    META = json.load(fp)

OUTPUT = {}

for index in META:
    transmit_range = META[index]["transmit_range"]
    amount_nodes = META[index]["amount_nodes"]
    routing_protocol = META[index]["routing_protocol"]
    buffer_size = META[index]["buffer_size"]
    overhead_ratio = None
    latency_avg = None
    delivery_prob = None
    try:
        with open(f'{PATH}/the-one/reports/DTN_Simulation_{index}_MessageStatsReport.txt') as fp: 
            for line in fp:
                if 'overhead_ratio' in line:
                    overhead_ratio = float(line.replace('overhead_ratio: ', ''))
                elif 'latency_avg' in line:
                    latency_avg = float(line.replace('latency_avg: ', ''))
                elif 'delivery_prob' in line:
                    delivery_prob = float(line.replace('delivery_prob: ', ''))
    except:
        pass
    OUTPUT[index] = {
        'input': {
            "routing_protocol": routing_protocol,
            "transmit_range": transmit_range,
            "buffer_size": buffer_size,
            "amount_nodes": amount_nodes
        },
        'output': {
            "overhead_ratio": overhead_ratio,
            "latency_avg": latency_avg,
            "delivery_prob": delivery_prob
        }
    }
        
with open(f'{PATH}/DATA.json', 'w') as fp:
    json.dump(OUTPUT, fp, indent=2)
