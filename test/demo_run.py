import mediapipe.framework.calculator_pb2 as calculator_pb2
from google.protobuf import text_format
import argparse
from simple_mediapipe.graph import CalculatorGraph
from logzero import logger
import logzero
import logging
from simple_mediapipe.packet import Packet
import time


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('graphs', nargs='+', default=[], type=str,
                        help="graph location, first is main graph, other is sub graph")
    parser.add_argument('--input_side_packet', type=str, default='',
                        help="input side packet, name=value,name=value...")
    parser.add_argument('--output_side_packet', type=str, default='',
                        help="output side packet, name=value,name=value...")
    return parser.parse_args()


def main():
    args = get_args()

    logzero.loglevel(logging.DEBUG)
    graph_configs = []
    for graph in args.graphs:
        graph_config = calculator_pb2.CalculatorGraphConfig()
        text_format.Merge(open(graph).read(), graph_config)
        logger.info(graph_config)
        graph_configs.append(graph_config)
    graph = CalculatorGraph()
    graph.initialize(graph_configs[0], graph_configs[1:])
    graph.start_run(args.input_side_packet, None, True)
    # graph.add_packet(tag='', index=0, packet=Packet('data1', 0))
    # graph.add_packet(tag='', index=0, packet=Packet('data2', 1))
    # graph.add_packet(tag='', index=0, packet=Packet('data3', 2))
    # graph.add_packet(tag='', index=0, packet=Packet('data4-0', 0))
    # # graph.add_packet('', 0, Packet('data', 0))
    # logger.info('output is %s', graph.pop_packet(tag='', index=0))
    # logger.info('output is %s', graph.pop_packet(tag='', index=0, blocking=2))
    # time.sleep(5)
    # for i in range(10):
    #     logger.info('output is %s', graph.pop_packet(tag='', index=0))


if __name__ == '__main__':
    main()
