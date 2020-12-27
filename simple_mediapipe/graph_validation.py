# TODO validate graph is DAG and config is accord with Calculator
from .registration import CALCULATOR
from .calculator import CalculatorBase
from logzero import logger


def validate_graph(graph_config):
    for i, node in enumerate(graph_config.node):
        name = node.calculator
        calculator = CALCULATOR.get(name)
        assert calculator is not None
        assert issubclass(calculator, CalculatorBase)
        # TODO add cc parameter
        status = calculator.get_contract(None)

        if not status:
            logger.error('{} Index[{}] node config is not correct. Please check calculator config detail'.format(name, i))
            return False
        else:
            logger.debug('{} Index[{}] node check success'.format(name, i))
    return True


