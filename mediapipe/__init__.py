import importlib
from pathlib import Path

from google.protobuf import descriptor_pool
from logzero import logger
from .calculators import *


def register_descriptor(root):
    for file in Path(root).glob("**/*"):
        pool = descriptor_pool.Default()
        from google.protobuf.pyext import _message
        if file.suffix == '.py':
            try:
                aa = importlib.import_module('.'.join(file.parts).rstrip('.py'))
                bb = aa.__dict__.get("DESCRIPTOR")
                if bb is not None and isinstance(bb, _message.FileDescriptor):
                    pool.AddFileDescriptor(bb)
                    logger.debug(f'registry {bb.name}')
            except Exception as e:
                logger.exception(e)

# register_descriptor('.')
