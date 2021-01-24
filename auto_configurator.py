# 6h de simulação (21600s)
# Alcance de transmissão {transmit_range} variando de 5 a 50, step de 5
# 3 tipos de grupos: pedestres, carros e bondes
# Protocolos {routing_protocol} 'ProphetRouter', 'SprayAndWaitRouter', 'EpidemicRouter', 'WaveRouter'
# {buffer_size} variando entre '25M', '50M', '75M', '100M'
# Message TTL de 120 minutes (2 hours)
# group1 (pedestrians) de 5-10 Km/h (1.4-2.8 m/s)
# group2 (cars) de 20-60 km/h (5.6-16.7 m/s)
# group3 (trams) de 20-40 Km/h (5.6-11.1 m/s)
# Group.immunityTime = 120 -- waverouter -- 2 min
# Group.custodyFraction = 300 -- waverouter -- 5 min

# CONFIGURAÇÃO COMBINATÓRIA
# =========================
# 864 combinações de configurações do simulador
# assert len(transmit_range_list) * len(routing_protocol_list) * len(buffer_size_list) * len(amount_nodes_list) == 864


import os, time


class Config:
    __INSTANCE = None
    
    @staticmethod
    def get_instance():
        if not Config.__INSTANCE:
            Config.__INSTANCE = Config()
        return Config.__INSTANCE

    def __init__(self):
        self.index = 1
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.transmit_range_list = list(range(5, 50, 5))
        self.routing_protocol_list = ['ProphetRouter', 'SprayAndWaitRouter', 'EpidemicRouter', 'WaveRouter']
        self.buffer_size_list = ['25M', '50M', '75M', '100M']
        self.amount_nodes_list = list(range(20, 140, 20))
        self.template = \
            '''
            Scenario.name = DTN_Simulation_{file_name}
            Scenario.simulateConnections = true
            Scenario.updateInterval = 0.1
            Scenario.endTime = 10800
            Scenario.nrofHostGroups = 3

            highspeedInterface.type = SimpleBroadcastInterface
            highspeedInterface.transmitSpeed = 10M
            highspeedInterface.transmitRange = {transmit_range}

            PointsOfInterest.poiFile1 = data/CentralPOIs.wkt
            PointsOfInterest.poiFile2 = data/WestPOIs.wkt
            PointsOfInterest.poiFile3 = data/ParkPOIs.wkt

            Group.movementModel = ShortestPathMapBasedMovement
            Group.router = {routing_protocol}
            Group.bufferSize = {buffer_size}
            Group.waitTime = 0, 120
            Group.nrofInterfaces = 1
            Group.interface1 = highspeedInterface
            Group.msgTtl = 120
            Group.immunityTime = 120
            Group.custodyFraction = 300

            Group1.groupID = p
            Group1.speed = 1.4, 2.8
            Group1.nrofHosts = {num_pedestrians}
            Group1.pois = 1,0.4, 2,0.1, 3,0.2

            Group2.groupID = c
            Group2.okMaps = 1
            Group2.speed = 5.6, 16.7
            Group2.nrofHosts = {num_cars}
            Group2.pois = 1,0.4, 2,0.1

            Group3.groupID = t
            Group3.movementModel = MapRouteMovement
            Group3.routeFile = data/tram3.wkt
            Group3.routeType = 1
            Group3.speed = 5.6, 11.1
            Group3.nrofHosts = {num_trams}
            Group3.pois = 1,0.4, 2,0.1

            Events.nrof = 1
            Events1.class = MessageEventGenerator
            Events1.interval = 25, 35
            Events1.size = 500k, 10M
            Events1.hosts = 0, {amount_nodes}
            Events1.prefix = M

            MovementModel.rngSeed = 1
            MovementModel.worldSize = 4500, 3400
            MovementModel.warmup = 1000

            MapBasedMovement.nrofMapFiles = 4
            MapBasedMovement.mapFile1 = data/roads.wkt
            MapBasedMovement.mapFile2 = data/main_roads.wkt
            MapBasedMovement.mapFile3 = data/pedestrian_paths.wkt
            MapBasedMovement.mapFile4 = data/shops.wkt

            Report.nrofReports = 2
            Report.warmup = 0
            Report.reportDir = reports/
            Report.report1 = MessageStatsReport
            Report.report2 = ContactTimesReport

            ProphetRouter.secondsInTimeUnit = 30
            SprayAndWaitRouter.nrofCopies = 6
            SprayAndWaitRouter.binaryMode = true

            Optimization.cellSizeMult = 5
            Optimization.randomizeUpdateOrder = true

            GUI.UnderlayImage.fileName = data/helsinki_underlay.png
            GUI.UnderlayImage.offset = 64, 20
            GUI.UnderlayImage.scale = 4.75
            GUI.UnderlayImage.rotate = -0.015
            GUI.EventLogPanel.nrofEvents = 100
            '''

    def __get_next_config(self):
        for transmit_range in self.transmit_range_list:
            for routing_protocol in self.routing_protocol_list:
                for buffer_size in self.buffer_size_list:
                    for amount_nodes in self.amount_nodes_list:
                        num_pedestrians = int(0.6 * amount_nodes) # ~60%
                        num_cars = int(0.3 * amount_nodes) # ~30%
                        num_trams = amount_nodes - num_cars - num_pedestrians  # ~10%
                        yield self.__build_config(transmit_range, 
                                                  routing_protocol, 
                                                  buffer_size, 
                                                  amount_nodes, 
                                                  num_pedestrians, 
                                                  num_cars, 
                                                  num_trams,
                                                  f'{self.index:03}')

    def __build_config(self, 
                       transmit_range, 
                       routing_protocol, 
                       buffer_size, 
                       amount_nodes, 
                       num_pedestrians, 
                       num_cars, 
                       num_trams,
                       file_name):
        return {
            'transmit_range': transmit_range,
            'routing_protocol': routing_protocol,
            'buffer_size': buffer_size,
            'amount_nodes': amount_nodes,
            'num_pedestrians': num_pedestrians,
            'num_cars': num_cars,
            'num_trams': num_trams,
            'file_name': file_name,
        }

    def __get_timestamp(self):
        return '_'.join(time.ctime().replace(':', '_').split())

    def __build_config_file(self, template, config):
        batch = template.format(**config)
        full_path = f'{self.base_dir}/input/{self.index:03}.txt'
        with open(full_path, 'w') as fp:
            fp.write(batch)
        return full_path
    
    def generate(self):
        for config in self.__get_next_config():
            self.__build_config_file(self.template, config)
            self.index += 1


if __name__ == '__main__':
    config = Config.get_instance()
    config.generate()
