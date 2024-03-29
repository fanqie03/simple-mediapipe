pb = """
# MediaPipe graph that performs object detection and tracking with TensorFlow
# Lite on CPU.
# Used in the examples in
# mediapipie/examples/desktop/object_tracking/

# Images on CPU coming into and out of the graph.
input_stream: "input_video"
output_stream: "output_video"

# Resamples the images by specific frame rate. This calculator is used to
# control the frequecy of subsequent calculators/subgraphs, e.g. less power
# consumption for expensive process.
node {
  calculator: "PacketResamplerCalculator"
  input_stream: "DATA:input_video"
  output_stream: "DATA:throttled_input_video"
  node_options: {
    [type.googleapis.com/mediapipe.PacketResamplerCalculatorOptions] {
      frame_rate: 3
    }
  }
}

# Subgraph that detections objects (see object_detection_cpu.pbtxt).
node {
  calculator: "ObjectDetectionSubgraphCpu"
  input_stream: "IMAGE:throttled_input_video"
  output_stream: "DETECTIONS:output_detections"
}

# Subgraph that tracks objects (see object_tracking_cpu.pbtxt).
node {
  calculator: "ObjectTrackingSubgraphCpu"
  input_stream: "VIDEO:input_video"
  input_stream: "DETECTIONS:output_detections"
  output_stream: "DETECTIONS:tracked_detections"
}

# Subgraph that renders annotations and overlays them on top of input images (see renderer_cpu.pbtxt).
node {
  calculator: "RendererSubgraphCpu"
  input_stream: "IMAGE:input_video"
  input_stream: "DETECTIONS:tracked_detections"
  output_stream: "IMAGE:output_video"
}
"""
import mediapipe.framework.calculator_pb2 as calculator_pb2
from google.protobuf import text_format
graph = calculator_pb2.CalculatorGraphConfig()
text_format.Merge(pb, graph)
print(graph)