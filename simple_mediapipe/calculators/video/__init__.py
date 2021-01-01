from simple_mediapipe.calculator import CalculatorBase
from simple_mediapipe.registration import CALCULATOR
from logzero import logger
from simple_mediapipe.calculator import CalculatorContext
from simple_mediapipe.packet import Packet
from queue import Queue
import threading
import time

cv2 = None


def dynamic_import():
    global cv2
    import cv2


@CALCULATOR.register_module()
class OpenCvVideoEncoderCalculator(CalculatorBase):
    """
    use case
    node {
      calculator: "OpenCvVideoEncoderCalculator"
      input_side_packet: "VIDEO_URL:video_url"
      output_side_packet: "VIDEO_INFO:video_info"
      output_stream: "VIDEO:img_raw"
    }
    """
    def parse_video_url(self, url):
        try:
            url = int(url)
            logger.info('parse url %s to integer', url)
        except ValueError:
            logger.info('try parse %s to integer failed', url)
        return url

    def open(self, cc: CalculatorContext):
        dynamic_import()
        VIDEO_URL_PACKET = cc.input_side_packets().tag("VIDEO_URL")
        self.url = 0 if VIDEO_URL_PACKET.get() is None else self.parse_video_url(VIDEO_URL_PACKET.get())
        self.cap = cv2.VideoCapture(self.url)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        channel = self.cap.get(cv2.CAP_PROP_CHANNEL)
        logger.info('open video: %s, width: %d, height: %d, fps: %d', self.url, width, height, fps)
        info_packet = cc.output_side_packets().tag('VIDEO_INFO')
        if info_packet is not None:
            info_packet.set({
                'url': self.url,
                'fps': fps,
                'width': width,
                'height': height,
                'channel': channel
            })

    def process(self, cc: CalculatorContext):
        flag, frame = self.cap.read()
        if not flag:
            logger.error('can not read frame from video capture: %s', self.url)
            return
        packet = Packet(frame)
        cc.outputs().tag('VIDEO').add_packet(packet)

    def close(self, cc: CalculatorContext):
        self.cap.release()


@CALCULATOR.register_module()
class OpenCvShowImageCalculator(CalculatorBase):
    def open(self, cc: CalculatorContext):
        self.win_name = 'win'
        self.q = Queue()
        self.running = True

        def show_func():
            while self.running:
                frame = self.q.get()
                cv2.imshow(self.win_name, frame)
                cv2.waitKey(1)

        thread = threading.Thread(target=show_func)
        thread.start()

    def process(self, cc: CalculatorContext):
        packet = cc.inputs().tag('VIDEO').get()
        self.q.put(packet.data)

    def close(self, cc: CalculatorContext):
        self.running = False
        cv2.destroyWindow(self.win_name)


@CALCULATOR.register_module()
class OpenCvDrawFpsCalculator(CalculatorBase):
    def open(self, cc: CalculatorContext):
        self.tic_count = 0
        self.previous_time = time.time()
        self.total_time = 0

    def process(self, cc: CalculatorContext):
        packet = cc.inputs().tag('VIDEO').get()
        frame = packet.get()
        self.tic_count += 1
        tic = time.time()
        self.total_time += tic - self.previous_time
        self.previous_time = tic
        fps = 1 / (self.total_time / self.tic_count)
        cv2.putText(frame, 'fps: {:.2f}'.format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), thickness=2)
        # cv2.putText(frame, str(self.total_time), (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        # cv2.putText(frame, str(self.tic_count), (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))
        cc.outputs().tag('VIDEO').add_packet(Packet(data=frame, timestamp=packet.timestamp))
