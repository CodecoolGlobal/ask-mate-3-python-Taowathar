from datetime import datetime


def get_max_id(questions):
    id_list = []
    for question in questions:
        id_list.append(question[0])
    return int(max(id_list)) if len(id_list) != 0 else 0


def get_submission_time():
    now = datetime.now().replace(microsecond=0)
    timestamp = datetime.timestamp(now)
    return int(timestamp)


def from_timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp)


def sorter(sorting, sorting_direction, data):
    check_list = ["title", "message"]
    if sorting in check_list:
        if sorting == "title":
            sort_id = 4
        elif sorting == "message":
            sort_id = 5
        new_data = []
        while data:
            minimum = data[0][sort_id]
            minimum_row = data[0]
            for row in data:
                if row[sort_id] < minimum:
                    minimum = row[sort_id]
                    minimum_row = row
            new_data.append(minimum_row)
            data.remove(minimum_row)
        if sorting_direction == "asc":
            return new_data
        else:
            return list(reversed(new_data))
    else:
        if sorting == "sub_time":
            sort_id = 0
        elif sorting == "num_view":
            sort_id = 2
        elif sorting == "num_vote":
            sort_id = 3
        new_data = []
        while data:
            minimum = int(data[0][sort_id])
            minimum_row = data[0]
            for row in data:
                if int(row[sort_id]) < minimum:
                    minimum = int(row[sort_id])
                    minimum_row = row
            new_data.append(minimum_row)
            data.remove(minimum_row)
        if sorting_direction == "asc":
            return new_data
        else:
            return list(reversed(new_data))
