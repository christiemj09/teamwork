"""
Parallel processing.
"""

import multiprocessing as mp


class Consumer(mp.Process):
    """Consumes tasks from a task queue."""
    
    def __init__(self, task_queue, result_queue):
        mp.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue
    
    def run(self):
        """Start task consumption."""
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown (the poison pill here is the value None)
                print('%s: Exiting' % proc_name)
                self.task_queue.task_done()
                break
            print('%s: %s' % (proc_name, next_task))
            answer = next_task()
            self.task_queue.task_done()
            self.result_queue.put(answer)


def process(Task, inputs, num_consumers=mp.cpu_count() * 2):
    """Process inputs in parallel."""
    # Establish communication queues
    tasks = mp.JoinableQueue()
    results = mp.Queue()
    
    # Start consumers
    print('Creating %d consumers' % num_consumers)
    consumers = [Consumer(tasks, results) for i in range(num_consumers)]
    for consumer in consumers:
        consumer.start()
    
    # Enqueue jobs
    num_jobs = 0
    for input in inputs:
        tasks.put(Task(input))
        num_jobs += 1
    
    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)
    
    # Wait for all of the tasks to finish
    tasks.join()
    
    # Start printing results
    while num_jobs:
        result = results.get()
        print('Result:', result)
        num_jobs -= 1
