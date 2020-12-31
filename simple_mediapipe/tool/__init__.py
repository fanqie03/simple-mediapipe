from typing import Dict


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


def parse_side_packets(kvstr) -> Dict:
    if kvstr in ['', None]:
        return {}
    elif isinstance(kvstr, str):
        ret = {}
        for item in kvstr.split(','):
            kv = item.split('=')
            ret[kv[0]] = kv[1]
        return ret
    elif isinstance(kvstr, dict):
        return kvstr


class Stats:
    Failed = 0
    Ok = 1
    Stop = 2