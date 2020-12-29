from simple_mediapipe.calculator import CalculatorBase
from simple_mediapipe.registration import CALCULATOR
from logzero import logger


@CALCULATOR.register_module()
class PassThroughCalculator(CalculatorBase):
    @staticmethod
    def get_contract(cc):
        """输入跟输出个数一致"""
        logger.debug('PassThroughCalculator get_contract')
        assert len(cc.inputs()) == len(cc.outputs()), 'inputs and outputs should be equal!'
        return True

    def process(self, cc):
        """输入复制到输出"""
        for input_stream, output_stream in zip(cc.inputs(), cc.outputs()):
            packet = input_stream.get()
            logger.info('pass through packet %s', packet)
            output_stream.add_packet(packet)


@CALCULATOR.register_module()
class MergeCalculator(CalculatorBase):
    @staticmethod
    def get_contract(cc):
        """检查配置为多个输入，一个输出"""

    def open(self, cc):
        """设置"""

    def process(self, cc): ...



import time
from simple_mediapipe.packet import Packet

@CALCULATOR.register_module()
class ProducerCalculator(CalculatorBase):
    seperate = 1
    id = 0
    def open(self, cc):...
        # self.seperate = 1
        # self.id = 0

    def process(self, cc):
        time.sleep(self.seperate)
        packet = Packet(data={'id':self.id}, timestamp=self.id)
        logger.info('after %s seconds produce %s', self.seperate, packet)
        for stream in cc.outputs():
            stream.add_packet(packet)
        self.id += 1


@CALCULATOR.register_module()
class ConsumerCalculator(CalculatorBase):
    def open(self, cc):
        ...

    def process(self, cc):
        for stream in cc.inputs():
            item = stream.get()
            logger.info('consume %s', item)

