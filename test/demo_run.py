import mediapipe.framework.calculator_pb2 as calculator_pb2
from google.protobuf import text_format
import argparse
from mediapipe.graph import CalculatorGraph
from logzero import logger


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('graph', type=str)
    parser.add_argument('--dependents', '-deps', nargs='+', type=str, help='sub graph dependents')
    return parser.parse_args()


def main():
    args = get_args()

    graph_config = calculator_pb2.CalculatorGraphConfig()
    text_format.Merge(open(args.graph).read(), graph_config)
    logger.info(graph_config)
    graph = CalculatorGraph()
    graph.initialize(graph_config)
    graph.start_run(None, None)


if __name__ == '__main__':
    main()
