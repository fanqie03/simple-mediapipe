# simple mediapipe

Mediapipe python implement. Convenience to understand. Pure Python. 1000 line.

[English](README-en.md)

[中文](README.md)

## start

clone and install

```shell
git clone https://github.com/mengfu188/simple_mediapipe
cd simple_mediapipe
pip install requirements.txt
```

an example

```shell
python test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt
```

resule log

```log
[I 201231 19:38:42 MainThread demo_run:33] node {
      calculator: "ProducerCalculator"
      output_stream: "data"
    }
    node {
      calculator: "ConsumerCalculator"
      input_stream: "data"
    }
    
[I 201231 19:38:42 MainThread stream:38] stream <OUTPUT_STREAM:"data", current queue size is 0> add downstream <INPUT_STREAM:"data", current queue size is 0>
[I 201231 19:38:42 MainThread collection:14] collection add OUTPUT_STREAM:"data", current queue size is 0, data
[I 201231 19:38:42 MainThread stream:38] stream <INPUT_STREAM:"data", current queue size is 0> add downstream <<bound method CalculatorNode.input_stream_listener of ConsumerCalculator_1, inputs: [], outputs: []>>
[I 201231 19:38:42 MainThread collection:14] collection add INPUT_STREAM:"data", current queue size is 0, data
[I 201231 19:38:42 MainThread graph:285] initialize graph success ^_^ 
[I 201231 19:38:42 MainThread scheduler:115] starting scheduler
[I 201231 19:38:43 MainThread __init__:53] after 1 seconds produce Packet:None_None, Timestamp: 2020-12-31 19:38:43, Data: {'id': 0}
[I 201231 19:38:43 MainThread __init__:67] consume Packet:None_None, Timestamp: 2020-12-31 19:38:43, Data: {'id': 0}
[I 201231 19:38:44 MainThread __init__:53] after 1 seconds produce Packet:None_None, Timestamp: 2020-12-31 19:38:44, Data: {'id': 1}
[I 201231 19:38:44 MainThread __init__:67] consume Packet:None_None, Timestamp: 2020-12-31 19:38:44, Data: {'id': 1}
[I 201231 19:38:45 MainThread __init__:53] after 1 seconds produce Packet:None_None, Timestamp: 2020-12-31 19:38:45, Data: {'id': 2}
[I 201231 19:38:45 MainThread __init__:67] consume Packet:None_None, Timestamp: 2020-12-31 19:38:45, Data: {'id': 2}
[I 201231 19:38:46 MainThread __init__:53] after 1 seconds produce Packet:None_None, Timestamp: 2020-12-31 19:38:46, Data: {'id': 3}
[I 201231 19:38:46 MainThread __init__:67] consume Packet:None_None, Timestamp: 2020-12-31 19:38:46, Data: {'id': 3}
```

change log level show more infomation.

```shell
python test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt --log_level DEBUG
```

## step by step to create new calculator

implement a producer that generates data regularly `ConsumerCalculator`.

1. write`node_options.pbtxt` (You can skip this step without using a configuration file)

TODO

2. use `protobuf` convert `node_options.pbtxt` to `py` file format (You can skip this step without using a configuration file)

TODO

download [protocbuf](https://github.com/protocolbuffers/protobuf/releases),

3. implement [producer `ProducerCalculator` and consumer `ConsumerCalculator`](simple_mediapipe/calculators/core/__init__.py)

    
```python
from simple_mediapipe.calculator import CalculatorBase
from simple_mediapipe.registration import CALCULATOR
from logzero import logger
import time
from simple_mediapipe.packet import Packet

@CALCULATOR.register_module()
class ProducerCalculator(CalculatorBase):
    def open(self, cc):
        self.seperate = 1
        self.id = 0

    def process(self, cc):
        time.sleep(self.seperate)
        packet = Packet(data={'id':self.id})
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
```

4. write graph code [`graph.pbtxt`](simple_mediapipe/graphs/sample3.pbtxt)

```protobuf
# producer and consumer

node {
  calculator: "ProducerCalculator"
  output_stream: "data"
}

node {
  calculator: "ConsumerCalculator"
  input_stream: "data"
}
```

5. Write execution file, read configuration, execute

[source code](test/demo_run.py)

```python
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
```

run

```shell
python  test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt 
```

## other

### visualization


You can use it https://viz.mediapipe.dev/ visual `pbtxt` file

### file introduction

- [mediapipe](mediapipe) put mediapipe official configuration, can be updated by[convert_proto.cmd](convert_proto.cmd).
- [simple_mediapipe](simple_mediapipe) put this repository code.
- [convert_proto.cmd](convert_proto.cmd) update mediapipe official configuration, convert pbtxt file to py file
    ```cmd
    convert_proto.cmd /path/to/mediapipe/official/repository
    ```

## TODO

- [x] side package
- [ ] demo 
- [ ] graph profiler

scheduler

## reference

- [mediapipe](https://github.com/google/mediapipe)
- [mmcv](https://github.com/open-mmlab/mmcv)