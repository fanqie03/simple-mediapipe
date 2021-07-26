# simple mediapipe

mediapipe的简化版本，根据自己的理解，用python重写了遍，大概有1000行左右的代码，以及没有漫长的安装过程。。。


[English](README-en.md)

[中文](README.md)

## 开始

克隆，安装

```shell
git clone https://github.com/mengfu188/simple_mediapipe
cd simple_mediapipe
pip install requirements.txt
```

执行例子

```shell
python test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt
```

运行结果

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

可以使用一下日志级别显示更多信息

```shell
python test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt --log_level DEBUG
```

## 实现新的Calculator

例如实现一个定时生成数据的生产者`ConsumerCalculator`

1. 写`node_options.pbtxt`（不用配置文件可以跳过这一步）

TODO

2. 使用`protobuf`将`node_options.pbtxt`转成`py`文件格式（不用配置文件可以跳过这一步）

TODO

下载[protocbuf](https://github.com/protocolbuffers/protobuf/releases),

3. 实现[生产者`ProducerCalculator`和消费者`ConsumerCalculator`](simple_mediapipe/calculators/core/__init__.py)

    
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

4. 编写[`graph.pbtxt`](simple_mediapipe/graphs/sample3.pbtxt)

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

5. 编写执行文件，读取配置，执行

[源码](test/demo_run.py)

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

执行

```shell
python  test/demo_run.py simple_mediapipe/graphs/sample3.pbtxt 
```

## 其他

### 可视化

可以用https://viz.mediapipe.dev/ 可视化pbtxt文件

### 文件介绍

- [mediapipe](mediapipe)文件夹放的官方实现的配置，可以使用[convert_proto.cmd](convert_proto.cmd)来更新配置
- [simple_mediapipe](simple_mediapipe)放的是本仓库的代码
- [convert_proto.cmd](convert_proto.cmd)更新mediapipe配置，将pbtxt转成py文件，使用方式：设置mediapipe仓库目录
    ```cmd
    convert_proto.cmd /path/to/mediapipe/official/repository
    ```

## TODO

- [x] 添加side package
- [ ] 添加demo 
- [ ] graph profiler

## 参考

- [mediapipe](https://github.com/google/mediapipe)
- [mmcv](https://github.com/open-mmlab/mmcv)
