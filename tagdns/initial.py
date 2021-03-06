from .endpoint import Endpoint
from .records import Records
from .manager import ManageResolvNodes, ManageAutoRenewNodes
from .utils.config import Config
from .utils.log import Log

from queue import Queue

import re
import socket

class Initial():
    def __init__(self, path):
        conf = Config(path)
        self.config = conf.read()
        self.inboundQueue = Queue()
        self.outboundQueue = Queue()
        self.logger = Log(self.config)

    def __createEndpoint(self):
        endpoint = Endpoint(self.inboundQueue, self.outboundQueue, self.config)
        endpoint.daemon = True
        endpoint.start()
        return endpoint

    def __deployRecords(self):
        return Records(self.config)

    def __createResolvNodes(self, records):
        mgr = ManageResolvNodes(self.inboundQueue, \
                                self.outboundQueue, \
                                records, self.logger, self.config)
        mgr.start()
        return mgr

    def __createAutoRenewNodes(self, records):
        renew = ManageAutoRenewNodes(records, self.config)
        renew.start()
        return renew

    def init(self):
        initialData = dict()
        initialData["inboundQueue"] = self.inboundQueue
        initialData["outboundQueue"] = self.outboundQueue
        initialData["endpoint"] = self.__createEndpoint()
        initialData["records"] = self.__deployRecords()
        initialData["resolver"] = self.__createResolvNodes(initialData["records"])
        initialData["autoRenew"] = self.__createAutoRenewNodes(initialData["records"])
        initialData["logger"] = self.logger
        return initialData
