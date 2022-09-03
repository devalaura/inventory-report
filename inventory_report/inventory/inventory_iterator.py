from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.current_data_index = 0

    def __next__(self):
        data = self.data[self.current_data_index]
        if not data:
            raise StopIteration()
        else:
            self.current_data_index += 1

        return data
