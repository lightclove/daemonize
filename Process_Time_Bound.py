import multiprocessing
import time

# Класс, представляющий отдельный процесс
class Process:
    def __init__(self, name, interval):
        self.name = name
        self.interval = interval
        self.running = False

    # Метод для выполнения процесса
    def execute(self):
        self.running = True
        while self.running:
            print(f"{self.name} is running")
            time.sleep(self.interval)

    # Остановка выполнения процесса
    def stop(self):
        self.running = False
        print(f"{self.name} is stopped")

    # Приостановка выполнения процесса
    def pause(self):
        self.running = False
        print(f"{self.name} is paused")

    # Возобновление выполнения процесса
    def resume(self):
        self.running = True
        print(f"{self.name} is resumed")

# Класс, управляющий процессами
class ProcessManager:
    def __init__(self):
        self.processes = []  # Список доступных процессов
        self.process_jobs = {}  # Словарь для отслеживания выполняемых процессов

    # Добавление процесса в список доступных
    def add_process(self, process):
        self.processes.append(process)

    # Запуск процесса по его имени
    def start_process(self, name):
        for process in self.processes:
            if process.name == name:
                p = multiprocessing.Process(target=process.execute)
                p.start()
                self.process_jobs[name] = p
                break

    # Остановка выполнения процесса по его имени
    def stop_process(self, name):
        if name in self.process_jobs:
            self.process_jobs[name].terminate()
            del self.process_jobs[name]

    # Приостановка выполнения процесса по его имени
    def pause_process(self, name):
        if name in self.process_jobs:
            process = self.processes[self.processes.index(self.process_jobs[name].name)]
            process.pause()
            self.process_jobs[name].terminate()
            del self.process_jobs[name]

    # Возобновление выполнения процесса по его имени
    def resume_process(self, name):
        for process in self.processes:
            if process.name == name:
                p = multiprocessing.Process(target=process.resume)
                p.start()
                self.process_jobs[name] = p
                break

    # Получение списка выполняемых процессов
    def get_running_processes(self):
        return list(self.process_jobs.keys())
