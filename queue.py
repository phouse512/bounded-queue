class Queue:
    """ A bounded queue implementation in Python using only arrays and integers. 

    Attributes:
        current_size: An integer representing the current size of the queue
        front: An integer that holds the index of the first element in the queue
        back: An integer that holds the index of the last element in the queue
        queue_array: An array of set size that holds the objects of the queue
    """

    def __init__(self, size):
        """ Initialize an empty queue of user-defined size """
        self.queue_array = [None] * size
        self.current_size = 0
        self.front = 0
        self.back = -1

    def enqueue(self, value):
        """ Attempts to add an integer to the queue
                - return True if value successfully added
                - retur False if queue is already full
        """
        if self.current_size == len(self.queue_array): return False

        self.back = self.__increment(self.back)
        self.queue_array[self.back] = value
        self.current_size += 1
        return True

    def dequeue(self):
        """ Attempts to remove the first element from the queue
                - return the 'oldest' item in the queue if not empty
                - return False if the queue was already empty
        """
        if self.current_size == 0: return False

        to_return = self.queue_array[self.front]
        self.front = self.__increment(self.front)
        self.current_size -= 1
        return to_return

    def __increment(self, value):
        """ increment moves the index that front/back holds up in 
            the case of enqueue or dequeue
                - private method that returns the new index value
        """
        return 0 if value == len(self.queue_array)-1 else value + 1
