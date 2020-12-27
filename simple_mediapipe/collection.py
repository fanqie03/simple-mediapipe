from logzero import logger
from collections import Iterable


def parse_tag_index_name(tag_index_name: str):
    """
    // Examples:
    //   "VIDEO:frames2"  -> tag: "VIDEO", index: 0,  name: "frames2"
    //   "VIDEO:1:frames" -> tag: "VIDEO", index: 1,  name: "frames"
    //   "raw_frames"     -> tag: "",      index: -1, name: "raw_frames"
    :param tag_index_name:
    :return: tag, index, name
    """
    tag, index, name = "", 0, ""
    parts = tag_index_name.split(':')
    if len(parts) == 1 and parts[0].islower():
        name = parts[0]
        index = -1
    elif len(parts) == 2 and parts[0].isupper() and parts[1].islower():
        tag = parts[0]
        name = parts[1]
    elif len(parts) == 3 and parts[0].isupper() and parts[1].isnumeric() and parts[2].islower():
        tag, index, name = parts
    else:
        raise Exception('{} can not be parsed', tag_index_name)
    return tag, index, name


class Collection:
    def __init__(self):
        self._tag_map = {}
        self._all_item_list = []

    def add(self, tag_index_names, items):
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
                    logger.warning('{}:{} conflict, will be override by {}'.format(tag, index, tag_index_name))
                item_list[index] = item
            self._all_item_list.append(item)

    def has_tag(self, tag):
        return self._tag_map.get(tag) is not None

    def tag(self, tag):
        return self.get(tag, 0)

    def get(self, tag, index):
        t = self._tag_map.get(tag)
        if t is None:
            return None
        return t[index]

    def __getitem__(self, index):
        return self._all_item_list[index]

    def __len__(self):
        return len(self._all_item_list)
