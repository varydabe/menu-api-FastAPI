def transform(items):
    array = []

    for item in items:
        array.append(single_transform(item))
    return array


def single_transform(values):

    return {
        "id": str(values.id),
        "nama": str(values.nama),
        "harga": int(values.harga)
    }