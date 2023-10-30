"""
Создание демона с использованием модуля daemonize.
Демон - это фоновый процесс, который продолжает работу,
даже если пользователь вышел из сессии или компьютер был перезапущен.
Пример кода для создания демона, который управляет процессом, может выглядеть следующим образом:
"""
import time
import os
import daemonize

class Process:
    def __init__(self, name):
        self.name = name
        self.state = "Stopped"

    def start(self):
        self.state = "Running"
        print(f"{self.name} is starting")

    def stop(self):
        self.state = "Stopped"
        print(f"{self.name} is stopping")

    def update_state(self, state):
        self.state = state
        print(f"{self.name} state updated to {state}")

class ProcessManager:
    def __init__(self):
        self.processes = [Process("Process 1"), Process("Process 2")]
        self.pid_file = "/var/run/process_manager.pid"
