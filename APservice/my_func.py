def convert(raw_time):
    hour = round(raw_time // 3600)
    minute = round((raw_time % 3600) // 60)
    second = int(raw_time % 60)
    return '{:0>2d}:{:0>2d}:{:0>2d}'.format(hour, minute, second)