from mediapipe.calculator import CalculatorBase
from mediapipe.registration import CALCULATOR


@CALCULATOR.register_module()
class PassThroughCalculator(CalculatorBase):

    def get_contract(cc):
        """输入跟输出个数一致"""
        return True

    def process(self, cc):
        """输入复制到输出"""


@CALCULATOR.register_module()
class MergeCalculator(CalculatorBase):
    def get_contract(cc):
        """检查配置为多个输入，一个输出"""

    def open(self, cc):
        """设置"""

    def process(self, cc): ...
