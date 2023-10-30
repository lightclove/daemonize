import unittest
from your_module import Process, ProcessManager

class TestProcess(unittest.TestCase):
    def test_start(self):
        process = Process("TestProcess")
        process.start()
        self.assertEqual(process.state, "Running")

    def test_stop(self):
        process = Process("TestProcess")
        process.stop()
        self.assertEqual(process.state, "Stopped")

    def test_update_state(self):
        process = Process("TestProcess")
        process.update_state("NewState")
        self.assertEqual(process.state, "NewState")

class TestProcessManager(unittest.TestCase):
    def test_process_manager_initialization(self):
        process_manager = ProcessManager()
        self.assertEqual(len(process_manager.processes), 2)

if __name__ == '__main__':
    unittest.main()
