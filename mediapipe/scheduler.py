from enum import Enum
from logzero import logger
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


class TaskQueue:
    """
    Abstract base class for the task queue.
    NOTE: The task queue orders the ready tasks by their priorities. This
    enables the executor to run ready tasks in priority order.
    """

    def run_next_task(self):
        """
        Runs the next ready task in the current thread. Should be invoked by the
        executor. This method should be called exactly as many times as AddTask
        was called on the executor.
        :return:
        """


class Executor:
    def __init__(self): ...

    def add_task(self, task_queue): ...

    def scheduler(self, task): ...


class Scheduler:
    """The class scheduling a calculator graph."""
    class State(Enum):
        # State of the scheduler. The figure shows the allowed state transitons.
        #
        #   NOT_STARTED
        #        |
        #        v
        #     RUNNING--+
        #     | | ^    |
        #     | |  \   |
        #     | |   \  v
        #     | |  PAUSED
        #     | |    |
        #     | v    v
        #     | CANCELLING
        #     |     |
        #     v     v
        #   TERMINATING
        #        |
        #        v
        #    TERMINATED
        STATE_NOT_STARTED = 0  #　The initial state.
        STATE_RUNNING = 1      # The scheduler is running and scheduling nodes.
        STATE_PAUSED = 2       # The scheduler is not scheduling nodes.
        STATE_CANCELLING = 3   # The scheduler is being cancelled. The scheduler cannot be paused
                               # in this state so that scheduler_queue_ can be drained.
        STATE_TERMINATED = 4   # The scheduler has terminated.

    def __init__(self, graph):
        self._graph = graph # The calculator graph to run.
        # TODO set length
        self._default_queue = Queue()     # Queue of nodes that need to be run.
        # TODO set thread count
        self._default_executor = ThreadPoolExecutor(thread_name_prefix='mediapipe')
        self._scheduler_queues = []    # Holds pointers to all queues used by the scheduler, for convenience.
        self._non_default_queues = []  # Non-default scheduler queues, keyed by their executor names.
        self._state=Scheduler.State.STATE_NOT_STARTED
        self._handle_idle=False
        self.running = False
        self.exception_count = 0
        # TODO config it
        self.max_exception_count = 100
        #   // Number of queues which are not idle.
        #   // Note: this indicates two slightly different things:
        #   //  a. the number of queues which still have nodes running;
        #   //  b. the number of queues whose executors may still access the scheduler.
        #   // When a queue becomes idle, it has stopped running nodes, and the scheduler
        #   // decrements the count. However, it is not done accessing the scheduler
        #   // until HandleIdle returns. Therefore, a and b are briefly out of sync.
        #   // This is ok, because it happens within a single critical section, which is
        #   // guarded by state_mutex_. If we wanted to split this critical section, we
        #   // would have to separate a and b into two variables.
        self._non_idle_queue_count=0
        #   // Keeps track of sources that can be considered for scheduling. Sources are
        #   // scheduled in layers, and those that are not currently active will not be
        #   // scheduled even if ready. Sources are removed once they are closed.
        self._active_sources=[]
        #   // Priority queue of source nodes ordered by layer and then source process
        #   // order. This stores the set of sources that are yet to be run.
        self._sources_queue=[]
        # // True if all graph input streams are closed.
        self._graph_input_streams_closed=False
        # Number of throttled graph input streams.
        self._throttled_graph_input_stream_count = 0

    def set_executor(self, executor):
        """Sets the executor that will run the nodes. Must be called before the
           scheduler is started. This is the normal executor used for nodes that
           do not use a special one."""
    def set_non_default_executor(self, name, executor):
        """ Sets the executor that will run the nodes assigned to the executor
            named |name|. Must be called before the scheduler is started."""

    def handle_idle(self):
        if self._handle_idle:
            logger.warming('HandleIdle: already in progress')
            return
        self._handle_idle = True

        while self.is_idle() and self._state in (Scheduler.State.STATE_RUNNING, Scheduler.State.STATE_CANCELLING):
            # TODO Remove active sources that are closed.
            # CleanupActiveSources();
            # TODO Quit if we have errors, or if there are no more packet sources.

            # See if we can schedule the next layer of source nodes.
            if len(self._active_sources) == 0 and len(self._sources_queue) != 0:
                logger.info('HandleIdle: activating sources')
                continue

            #      // See if we can unthrottle some source nodes or graph input streams to
            #     // break deadlock. If we are still idle and there are active source nodes,
            #     // they must be throttled.
            if len(self._active_sources) != 0 or self._throttled_graph_input_stream_count > 0:
                logger.info('HandleIdle: unthrottling')
                continue

    def is_idle(self):
        return self._non_default_queues
    def reset(self):
        """Resets the data members at the beginning of each graph run."""
    def start(self, blocking=True):
        """Starts scheduling nodes."""
        logger.info('starting scheduler')
        assert self._state == Scheduler.State.STATE_NOT_STARTED
        self._state = Scheduler.State.STATE_RUNNING
        self.set_queues_running(True)

        def run_queue():
            while self.running:
                logger.debug('try execute task, the task queue length is {}, '
                             'thread pool worker queue length is {}'
                             .format(self._default_queue.qsize(), self._default_executor._work_queue.qsize()))
                task = self._default_queue.get(block=True)
                self._default_executor.submit(task)
                # TODO, WILL THROW EXCEPTION WHEN SUBMIT TASK
                # try:
                #     self._default_executor.submit(task)
                # except Exception as e:
                #     self.exception_count += 1
                #     logger.exception(e)
                #     logger.info('exception count is {}, max exception count is {}'
                #                 .format(self.exception_count, self.max_exception_count))
                #     if self.exception_count >= self.max_exception_count:
                #         logger.error("Excetion count >= Max exception count")
                #         self.set_queues_running(False)
                #         # TODO exit?

        if not blocking:
            single_thread_pool = ThreadPoolExecutor()
            single_thread_pool.submit(run_queue)
        else:
            run_queue()

        self.handle_idle()

    def add_task(self, task):
        self._default_queue.put(task)

    def pause(self):
        """Pauses the scheduler.  Does nothing if Cancel has been called."""
    def resume(self):
        """Resumes the scheduler."""
    def cancel(self):...
    def is_pause(self):...
    def is_terminated(self):...

    def set_queues_running(self, running):
        self.running = True
        for queue in self._scheduler_queues:
            queue.set_running(running)

    def closed_all_graph_input_stream(self):
        """Notifies the scheduler that all graph input streams have been closed."""

    def close_all_source_nodes(self):
        """Closes all source nodes at the next scheduling opportunity."""


class SchedulerQueue(TaskQueue):
    """Manages a priority queue of nodes to be run on the associated executor."""
    class Item:
        """Item in the queue. Wraps a node pointer and helps with priority sorting."""
        def __init__(self, node, context=None):
            self.node=node
            self.context=context
            self.source_process_order=0
            self.id = 0
            self.layer=0
            self.is_source=False
            self.is_open_node=False  # True if the task should run OpenNode().
            self._running_count = 0

        def set_running(self, running):
            self._running_count += 1 if running else -1
            assert self._running_count <= 1

        def __cmp__(self, other):
            """
            This comparison is meant to be used with a std::priority_queue. Since
            the priority queue returns higher priority items first, this function
            means "this is lower priority than that", i.e. "this runs after that".
            - Non-sources have priority over sources.
            - Sources are sorted by layer (lower layer numbers run first), then by
            Calculator::SourceProcessOrder (smaller values run first), then by
            node id: smaller ids run first, since they come earlier in the config.
            - Non-sources are sorted by node id: larger ids run first, because they
            are closer to the leaves.
            :param other: SchedulerQueue.Item
            :return:
            """
            if self.is_open_node or other.is_open_node:
                # OpenNode() runs before ProcessNode().
                if not other.is_open_node: return False
                # ProcessNode() runs after OpenNode().
                if not self.is_open_node: return True
                # If both are OpenNode(), higher ids run after lower ids.
                return self.id > other.id
            if self.is_source:
                # Sources run after non-sources.
                if not other.is_source: return True
                # Higher layer sources run after lower layer sources.
                if self.layer != other._layer: return self.layer > other.layer
                # Higher SourceProcessOrder values run after lower values.
                if self.source_process_order != other.source_process_order:
                    return self.source_process_order > other.source_process_order
                # For sources, higher ids run after lower ids.
                return self.id > other.id
            else:
                # Non-sources run before sources.
                if other.is_source: return False
                # For non-sources, higher ids run before lower ids.
                return self.id < other.id