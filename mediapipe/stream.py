from enum import Enum
class NodeReadiness(Enum):
    kNotReady=0
    kReadyForProcess=1
    kReadyForClose=2