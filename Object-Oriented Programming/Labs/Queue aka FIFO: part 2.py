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
        print(f'Appended {elem}, Now = {self.queue}')

    def get(self):
        if self.queue:
            cur = self.queue.pop()
            return cur
        else:
            raise QueueError()


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return False if self.queue else True


que = SuperQueue()

que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")