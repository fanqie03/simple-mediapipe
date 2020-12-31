from logzero import logger
from .tool import parse_tag_index_name
from .stream import Stream
from .packet import Packet
from typing import Union


class Collection:
    def __init__(self):
        self._tag_map = {}
        self._all_item_list = []

    def add(self, tag_index_names, items):
        logger.info('collection add %s, %s', items, tag_index_names )
        if not isinstance(tag_index_names, (list, tuple, set)):
            tag_index_names = [tag_index_names]
            items = [items]

        for tag_index_name, item in zip(tag_index_names, items):
            tag, index, name = parse_tag_index_name(tag_index_name)
            if self._tag_map.get(tag) is None:
                self._tag_map[tag] = []
            item_list = self._tag_map[tag]
            if index < -1:
                raise Exception('{} out of range, which index is {}'.format(tag_index_name, index))
            elif index == -1:
                item_list.append(item)
            elif index >= len(item_list):
                for i in range(index - len(item_list)):
                    item_list.append(None)
                item_list.append(item)
            else:
                if item_list[index] is not None:
                    logger.warning('%s:%s conflict, will be override by %s', tag, index, tag_index_name)
                item_list[index] = item
            self._all_item_list.append(item)

    def has_tag(self, tag):
        return self._tag_map.get(tag) is not None

    def tag(self, tag) -> Union[Stream, None, Packet]:
        return self.get(tag, 0)

    def get(self, tag, index) -> Union[Stream, None, Packet]:
        t = self._tag_map.get(tag)
        if t is None:
            return None
        return t[index]

    def __getitem__(self, index) -> Union[Stream, Packet]:
        return self._all_item_list[index]

    def __len__(self):
        return len(self._all_item_list)

    def __str__(self):
        return '[' + ', '.join(map(lambda x: str(x), self._all_item_list)) + ']'
