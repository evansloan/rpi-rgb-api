from datetime import datetime


def process_request(data, required):
    for field, types in required.items():
        if field not in data:
            return False

        try:
            if len(types) > 1:
                data[field] = types[0](types[1](val) for val in data[field])
            else:
                data[field] = types[0](data[field])
        except ValueError:
            return False
        
    return data


def set_duration(duration):
    if duration != 0:
        return datetime.now().timestamp() + duration
    return None


def duration_check(target_time):
    if target_time is not None:
        return datetime.now().timestamp() > target_time


def get_color_diff(color):
    return int(color / 255) if color != 0 else 0
