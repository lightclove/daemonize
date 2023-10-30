"""
 Три тестовых метода, которые проверяют различные сценарии применения правил, включая kill, suspend и resume состояний процесса.
"""
import unittest
from Process_Manager_Abstract import Process, Rule, ProcessManager, ProcessRuleProcessor

class TestProcessManager(unittest.TestCase):
    def test_process_rule_killing(self):
        process = Process(123, "test_process", 70, 0)
        rule = Rule("Test Rule", "test_process", "KILL", 50)
        rule_processor = ProcessRuleProcessor()

        rule_processor.process_rule(process, rule)
        self.assertFalse(psutil.pid_exists(123), "Process should be killed")

    def test_process_rule_pausing(self):
        process = Process(456, "test_process", 0, 90)
        rule = Rule("Test Rule", "test_process", "PAUSE", 80)
        rule_processor = ProcessRuleProcessor()

        rule_processor.process_rule(process, rule)
        self.assertTrue(psutil.pid_exists(456), "Process should be paused")

    def test_process_rule_resuming(self):
        process = Process(789, "test_process", 0, 30)
        rule = Rule("Test Rule", "test_process", "RESUME", 40)
        rule_processor = ProcessRuleProcessor()

        rule_processor.process_rule(process, rule)
        self.assertTrue(psutil.pid_exists(789), "Process should be resumed")

if __name__ == '__main__':
    unittest.main()

