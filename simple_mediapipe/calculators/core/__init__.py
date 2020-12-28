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
            logger.debug('pass through packet %s', packet)
            output_stream.add_packet(packet)


@CALCULATOR.register_module()
class MergeCalculator(CalculatorBase):
    @staticmethod
    def get_contract(cc):
        """检查配置为多个输入，一个输出"""

    def open(self, cc):
        """设置"""

    def process(self, cc): ...


@CALCULATOR.register_module()
class SourceCalculator(CalculatorBase):
    def open(self, cc):
        ...

    def process(self, cc):
        ...
