import os, json


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

    def generate(self):
        dic = {}
        for config in self.__get_next_config():
            dic[f'{self.index:03}'] = config
            self.index += 1
        with open(f'{self.base_dir}/META.json', 'w') as fp:
            json.dump(dic, fp)

if __name__ == '__main__':
    config = Config.get_instance()
    config.generate()
