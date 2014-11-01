import unittest
from queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(10)

    def test_queue_half_full(self):
        """ Test if normal queue and dequeue operations work """
        [self.queue.enqueue(i) for i in range(1,6)]
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 5)

    def test_enqueue_full(self):
        """ Test enqueue behavior when queue is full """
        [self.queue.enqueue(i) for i in range(1,11)]
        self.assertFalse(self.queue.enqueue(2041))

    def test_dequeue_empty(self):
        """ Test dequeue behavior when queue is empty """
        self.assertFalse(self.queue.dequeue())

    def test_queue(self):
        """ Test queue behavior over many inserts/removals
            - test front/back index wraparounds
        """
        [self.queue.enqueue(i) for i in range(1,11)]
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 5)
        [self.queue.enqueue(i) for i in range(23,29)]
        self.assertEqual(self.queue.dequeue(), 6)
        self.assertEqual(self.queue.dequeue(), 7)
        self.assertEqual(self.queue.dequeue(), 8)
        self.assertEqual(self.queue.dequeue(), 9)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 23)
        self.assertEqual(self.queue.dequeue(), 24)
        self.assertEqual(self.queue.dequeue(), 25)
        self.assertEqual(self.queue.dequeue(), 26)
        self.assertEqual(self.queue.dequeue(), 27)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)