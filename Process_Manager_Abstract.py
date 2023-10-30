import psutil
import time
import datetime


"""
    Интерфейс для обработки правил
    интерфейс RuleProcessor, который предоставляет метод process_rule,
    который будет реализован классом ProcessRuleProcessor.
    Логика обработки правил вынесена в отдельный класс ProcessRuleProcessor согласно SRP
    Это позволяет применять принцип инверсии зависимостей.
    Но можно сделать и через протоколы проще.
"""
class RuleProcessor:
    def process_rule(self, process, rule):
        pass


# Класс, выполняющий действия над процессами на основе правил , все согласно SRP
class ProcessRuleProcessor(RuleProcessor):
    def process_rule(self, process, rule):
        if rule.action == "KILL" and process.memory_usage > rule.value:
            print(f"{process.name} is using too much memory ({process.memory_usage}%), killing...")
            process.kill()
        elif rule.action == "PAUSE" and process.cpu_usage > rule.value:
            print(f"{process.name} is using too much CPU ({process.cpu_usage}%), pausing...")
            process.suspend()
        elif rule.action == "RESUME" and process.cpu_usage < rule.value:
            print(f"{process.name} is using less CPU ({process.cpu_usage}%), resuming...")
            process.resume


# Класс для представления процесса
class Process:
    def __init__(self, pid, name, memory_usage, cpu_usage):
        self.pid = pid
        self.name = name
        self.memory_usage = memory_usage
        self.cpu_usage = cpu_usage

    def kill(self):
        psutil.Process(self.pid).kill()

    def suspend(self):
        psutil.Process(self.pid).suspend()

    def resume(self):
        psutil.Process(self.pid).resume()


# Класс для представления правила
class Rule:
    def __init__(self, name, process_name, action, value):
        self.name = name
        self.process_name = process_name
        self.action = action
        self.value = value


# Класс, отвечающий за управление процессами и применение правил
class ProcessManager:
    def __init__(self):
        self.active_processes = []
        self.rules = []

    def get_processes(self):
        self.active_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
            try:
                process = Process(proc.info['pid'], proc.info['name'], proc.info['memory_percent'],
                                  proc.info['cpu_percent'])
                self.active_processes.append(process)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def add_rule(self, rule):
        self.rules.append(rule)
    # Применение правил вынесено в метод apply_rules,
    # который принимает экземпляр RuleProcessor для обработки правил
    # согласно принципу инверсии зависимостей и разделению интерфейсов

    def apply_rules(self, rule_processor):
        for rule in self.rules:
            for process in self.active_processes:
                if process.name == rule.process_name:
                    rule_processor.process_rule(process, rule)

    def run(self, interval=60):
        while True:
            self.get_processes()
            self.apply_rules(ProcessRuleProcessor())
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{timestamp} Active processes: {len(self.active_processes)}")
            time.sleep(interval)


if __name__ == '__main__':
    pm = ProcessManager()
    pm.add_rule(Rule("Kill high memory usage", "chrome.exe", "KILL", 50))
    pm.add_rule(Rule("Pause high CPU usage", "python.exe", "PAUSE", 80))
    pm.add_rule(Rule("Resume low CPU usage", "python.exe", "RESUME", 50))
    pm.run()
