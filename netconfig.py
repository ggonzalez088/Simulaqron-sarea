import sys
import json
from simulaqron.network import Network
from simulaqron.settings import Config


class Netconfig: 
    def __init__(self): 
        self.network = None


    #network.json fitxategia konfiguratu beharrezko ekipo eta topologiarekin, eta sartu diren IP helbideen arabera
    def configNetworkFile(self, AliceIP, BobIP):
        #sarearen datuak beharrezko formatuan egituratu
        data = { 
            "newnet": { 
                "nodes": { 
                    "Alice": { 
                        "app_socket": [AliceIP, 8003], 
                        "cqc_socket": [AliceIP, 8001], 
                        "vnode_socket": [AliceIP, 8002] 
                    }, 
                    "Bob": { 
                        "app_socket": [BobIP, 9000], 
                        "cqc_socket": [BobIP, 9001], 
                        "vnode_socket": [BobIP, 9002]
                    } 
                },
                "topology":None
                
            } 
        }
        
        #sortutako sarearen datuak network.json fitxategian iraultzea
        with open('/home/ubuntu/.local/lib/python3.10/site-packages/simulaqron/config/network.json','w') as json_file:
            json.dump(data,json_file,indent=4)


    #network.json fitxategian dagoen sarea hasieratu, eta qubit eta log parametroak konfiguratu
    def createNetwork(self,role):
        if role == 'Alice':
            #ekipoaren rola Alice bada, IP helbide lokala Alice ekipoaren IP helbidea da
            aliceIP = sys.argv[2]
            bobIP = sys.argv[3]
            self.configNetworkFile(aliceIP,bobIP)
        elif role =='Bob':
            #ekipoaren rola Bob bada, IP helbide lokala Bob ekipoaren IP helbidea da
            aliceIP = sys.argv[3]
            bobIP = sys.argv[2]
            self.configNetworkFile(aliceIP,bobIP)
        else:
            raise TypeError("Ez da rol onargarria sartu")

        #simulaqron sarearen objektua sortu, network.json fitxategian dagoen newnet sarean oinarrituta
        self.network = Network(name="newnet", nodes=None, topology=None, new=False)
        
        #beharrezko simulaqron parametroak ezarri
        settings=Config()
        settings.max_qubits=10000
        settings.log_level=40

        #sarearen objektua hasieratu
        self.network.start()



    
   


