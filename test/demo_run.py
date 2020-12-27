import mediapipe.framework.calculator_pb2 as calculator_pb2
from google.protobuf import text_format
import argparse
from simple_mediapipe.graph import CalculatorGraph
from logzero import logger
from simple_mediapipe.packet import Packet
import time


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
    graph.start_run(None, None, False)
    graph.add_packet(tag='', index=0, packet=Packet('data1', 0))
    graph.add_packet(tag='', index=0, packet=Packet('data2', 1))
    graph.add_packet(tag='', index=0, packet=Packet('data3', 2))
    # graph.add_packet('', 0, Packet('data', 0))
    logger.info('output is {}'.format(graph.pop_packet(tag='', index=0)))
    logger.info('output is {}'.format(graph.pop_packet(tag='', index=0, blocking=2)))
    time.sleep(5)
    for i in range(10):
        logger.info('output is {}'.format(graph.pop_packet(tag='', index=0)))


if __name__ == '__main__':
    main()
