from simple_mediapipe.list import List
from logzero import logger
import threading
import time

arr = List()


class ProduceThread(threading.Thread):
    def __init__(self, arr:List):
        threading.Thread.__init__(self)
        self.arr = arr

    def run(self):
        logger.info('sleep')
        time.sleep(2)
        logger.info('push element！')
        self.arr.push_last(1)
        logger.info('push element complete')


produce = ProduceThread(arr)
produce.start()
logger.info('get element')
logger.info('get element {}'.format(arr.get_first(blocking=10)))
logger.info('get element complete')
