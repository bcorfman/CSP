import heapq
from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return f'Stack({self._data})'

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        return self._data[item]

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, item):
        return item in self._data

    def push(self, item, _priority=None):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def isEmpty(self):
        return len(self._data) == 0

    def update(self, item, _priority=None):
        """ Add the item into the queue if not there; otherwise,
        update in place if cost is lower. """
        if item not in self._data:
            self._data.append(item)
        else:
            idx = self._data.index(item)
            if item.cost < self._data[idx].cost:
                self._data[idx] = item


class Queue:
    """ A container with a first-in-first-out (FIFO) queuing policy. """
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self._data = deque(lst)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'Queue({self._data})'

    def __getitem__(self, item):
        return self._data[item]

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, item):
        return item in self._data

    def push(self, item, _priority=None):
        self._data.appendleft(item)

    def pop(self):
        return self._data.pop()

    def isEmpty(self):
        return len(self._data) == 0

    def update(self, item, _priority=None):
        """ Add the item into the queue if not there; otherwise,
        update in place if cost is lower. """
        if item not in self._data:
            self._data.appendleft(item)
        else:
            idx = self._data.index(item)
            if item.cost < self._data[idx].cost:
                self._data[idx] = item


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.
    """
    def __init__(self, heap=None, _count=None):
        if heap is None:
            heap = []
        self._data = heap

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f'PriorityQueue({self._data})'

    def __contains__(self, item):
        for p, c, i in self._data:
            if i.state == item.state:
                return True
        return False

    def push(self, item, priority=None):
        if priority is None:
            priority = item.cost
        entry = (priority, len(self._data), item)
        heapq.heappush(self._data, entry)

    def pop(self):
        (_, _, item) = heapq.heappop(self._data)
        return item

    def isEmpty(self):
        return len(self._data) == 0

    def update(self, item, priority):
        for index, (p, c, i) in enumerate(self._data):
            if i == item:
                if p <= priority:
                    break
                del self._data[index]
                self._data.append((priority, c, item))
                heapq.heapify(self._data)
                break
        else:
            self.push(item, priority)
