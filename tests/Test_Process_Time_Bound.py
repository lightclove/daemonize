import unittest
from Process_Time_Bound import Process, ProcessManager

class TestProcessManager(unittest.TestCase):
    def setUp(self):
        self.process_manager = ProcessManager()
        self.test_process = Process("TestProcess", 1)

    def test_add_process(self):
        self.process_manager.add_process(self.test_process)
        self.assertIn(self.test_process, self.process_manager.processes)

    def test_start_stop_process(self):
        self.process_manager.add_process(self.test_process)
        self.process_manager.start_process("TestProcess")
        self.assertTrue(self.test_process.running)
        self.process_manager.stop_process("TestProcess")
        self.assertFalse(self.test_process.running)

    def test_pause_resume_process(self):
        self.process_manager.add_process(self.test_process)
        self.process_manager.start_process("TestProcess")
        self.assertTrue(self.test_process.running)
        self.process_manager.pause_process("TestProcess")
        self.assertFalse(self.test_process.running)
        self.process_manager.resume_process("TestProcess")
        self.assertTrue(self.test_process.running)

    def test_get_running_processes(self):
        self.process_manager.add_process(self.test_process)
        self.process_manager.start_process("TestProcess")
        running_processes = self.process_manager.get_running_processes()
        self.assertIn("TestProcess", running_processes)

if __name__ == '__main__':
    unittest.main()
