from abc import ABCMeta, abstractmethod
import time
import requests

class Service(metaclass=ABCMeta):
    @abstractmethod
    def stop_systems(self):
        raise NotImplementedError('Please implement the method <stop_systems>!')

    @abstractmethod
    def get_content(self):
        raise NotImplementedError('Please implement the method <get_content>!')		

    @abstractmethod
    def health_check_systems(self):
        raise NotImplementedError('Please implement the method <health_check_systems>!')
        
class WebSite(Service):
    __sites = ['https://www.google.com/']
    def stop_systems(self):
        for system in self.__sites:
            print(f"Stopping system: {system}")
            time.sleep(0.5)

    def get_content(self):
        for system in self.__sites:
            res = requests.get(system)
            print(res.text)

    def health_check_systems(self):
        for system in self.__sites:
            print("Checking system: {}".format(system))
            time.sleep(0.5)

class Infrastructure(object):
	def stop_all(self, service_object):
		print('Stopping platfrom: {}'.format(service_object))
		return eval(service_object)().stop_systems()

	def start_all(self, service_object):
		print('Starting platfrom: {}'.format(service_object))
		return eval(service_object)().get_content()		

	def hc_all(self, service_object):
		print('Checking platfrom: {}'.format(service_object))
		return eval(service_object)().health_check_systems()

	def make_magic_happen(self,service_object):
		self.hc_all(service_object)
		self.stop_all(service_object)
		self.start_all(service_object)
		self.hc_all(service_object)

IS = Infrastructure()
PFORMS = ['WebSite']
for services in PFORMS:
	IS.hc_all(services)
	IS.stop_all(services)
	IS.start_all(services)
	IS.hc_all(services)