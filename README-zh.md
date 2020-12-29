# simple mediapipe

mediapipe的简化版本，根据自己的理解，用python重写了遍

## 开始

克隆项目

```shell
git clone ...
cd project
python test/demo_run.py simple_mediapipe/graphs/sample1.pbtxt
```

运行结果

```log
[I 201228 19:26:31 MainThread demo_run:22] node {
      calculator: "PassThroughCalculator"
      input_stream: "in"
      output_stream: "out1"
    }
    node {
      calculator: "PassThroughCalculator"
      input_stream: "out1"
      output_stream: "out"
    }
    input_stream: "in"
    output_stream: "out"
    
[D 201228 19:26:31 MainThread __init__:11] PassThroughCalculator get_contract
[D 201228 19:26:31 MainThread __init__:11] PassThroughCalculator get_contract
[I 201228 19:26:31 MainThread graph:197] Empty DataFrame
    Columns: [type, tag, index, name, tag_index_name, item, node_id, graph_id]
    Index: []
[I 201228 19:26:31 MainThread graph:198] Empty DataFrame
    Columns: [type, item, node_id, graph_id]
    Index: []
[I 201228 19:26:31 MainThread graph:199]   type                        ...                                                                     config
    0                             ...                          node {\n  calculator: "PassThroughCalculator"\...
    
    [1 rows x 4 columns]
[I 201228 19:26:31 MainThread graph:209] initialize graph success ^_^ 
[I 201228 19:26:31 MainThread scheduler:139] starting scheduler
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 0, thread pool worker queue length is 0
[I 201228 19:26:31 MainThread demo_run:30] output is None
[D 201228 19:26:31 simple-mediapipe_0 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_0 __init__:19] pass through packet Timestamp: 0, Data: data1
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 3, thread pool worker queue length is 0
[D 201228 19:26:31 simple-mediapipe_0 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_0 __init__:19] pass through packet Timestamp: 1, Data: data2
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 3, thread pool worker queue length is 0
[D 201228 19:26:31 simple-mediapipe_0 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_0 __init__:19] pass through packet Timestamp: 2, Data: data3
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 3, thread pool worker queue length is 0
[D 201228 19:26:31 simple-mediapipe_2 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_2 __init__:19] pass through packet Timestamp: 0, Data: data1
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 2, thread pool worker queue length is 0
[I 201228 19:26:31 MainThread demo_run:31] output is Timestamp: 0, Data: data1
[D 201228 19:26:31 simple-mediapipe_0 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_0 __init__:19] pass through packet Timestamp: 1, Data: data2
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 1, thread pool worker queue length is 0
[D 201228 19:26:31 simple-mediapipe_1 calculator:85] Node PassThroughCalculator execute!
[D 201228 19:26:31 simple-mediapipe_1 __init__:19] pass through packet Timestamp: 2, Data: data3
[D 201228 19:26:31 ThreadPoolExecutor-0_0 scheduler:148] try execute task, the task queue length is 0, thread pool worker queue length is 0
[I 201228 19:26:36 MainThread demo_run:34] output is Timestamp: 1, Data: data2
[I 201228 19:26:36 MainThread demo_run:34] output is Timestamp: 2, Data: data3
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
[I 201228 19:26:36 MainThread demo_run:34] output is None
```

## 功能对比

### 相同点

- 依旧使用pbtxt来进行配置，尽量能跑起来原本的配置
- 概念一样：图，流，

### 不同点

- 目前还没有side package

## 实现新的Calculator

例如实现一个定时生成数据的`GeneratePackageCalculator`

1. 写`node_options.pbtxt`（如果需要）

2. 使用`protobuf`将`node_options.pbtxt`转成`py`文件格式

3. 实现`GeneratePackageCalculator`

    
```python

```

4. 编写`graph.pbtxt`

```protobuf

```

5. 编写执行文件，读取配置，执行

```python

```

## 其他

### 文件介绍

- [mediapipe](mediapipe)文件夹放的官方实现的配置，可以使用[convert_proto.cmd](convert_proto.cmd)来更新配置
- [simple_mediapipe](simple_mediapipe)放的是本仓库的代码
- [convert_proto.cmd](convert_proto.cmd)更新mediapipe配置，将pbtxt转成py文件，使用方式：设置mediapipe仓库目录
    ```cmd
    set MEDIAPIPE_OFFICIAL_HOME=...
    convert_proto.cmd %MEDIAPIPE_OFFICIAL_HOME%
    ```

## TODO

- [ ] 添加side package
- [ ] 添加demo 

## 参考

- mediapipe
- mmdetection
