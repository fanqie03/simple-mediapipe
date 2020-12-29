from simple_mediapipe.calculator import CalculatorBase
from simple_mediapipe.registration import CALCULATOR
from logzero import logger
from simple_mediapipe.calculator import CalculatorContext
from simple_mediapipe.packet import Packet
from queue import Queue
import cv2
import threading


@CALCULATOR.register_module()
class OpenCvVideoEncoderCalculator(CalculatorBase):

    def open(self, cc: CalculatorContext):
        self.url = 0
        self.cap = cv2.VideoCapture(self.url)
        fps = self.cap.get(cv2.CAP_PROP_FPS)
        width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        logger.info('open video: %s, width: %d, height: %d, fps: %d', self.url, width, height, fps)

    def process(self, cc: CalculatorContext):
        flag, frame = self.cap.read()
        if not flag:
            logger.error('can not read frame from video capture: %s', self.url)
            return
        packet = Packet(frame)
        cc.outputs().tag('IMAGE').add_packet(packet)

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
                cv2.waitKey(33)

        thread = threading.Thread(target=show_func)
        thread.start()

    def process(self, cc: CalculatorContext):
        packet = cc.inputs().tag('IMAGE').get()
        self.q.put(packet.data)

    def close(self, cc: CalculatorContext):
        self.running = False
        cv2.destroyWindow(self.win_name)
