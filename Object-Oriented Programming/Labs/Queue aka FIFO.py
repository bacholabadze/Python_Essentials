class QueueError(BaseException):  # Choose base class for the new exception.
    """Exception raised when queue is empty.

      Attributes:
          message -- explanation of the error
    """
    def __init__(self, message="The queue is empty!"):
        self.message = message
        super().__init__(self.message)


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if self.queue:
            cur = self.queue.pop()
            return cur
        else:
            raise QueueError()


que = Queue()
que.put(1)
que.put("dog")
que.put(False)


try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
