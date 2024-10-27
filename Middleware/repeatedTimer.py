from time import sleep, time
import threading

class RepeatedTimer(threading.Thread):
    def __init__(self, interval, function, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval    #ms
        self.function = function
        self.is_running = False
        self.args = args
        self.kwargs = kwargs
        self.start_time=0
        self.start()

    def run(self):
        while self.is_running:
            now = int(time() * 1000)
            sleep_ms =  self.interval - (now - self.start_time)
            if sleep_ms < 0:
                self.function(*self.args, **self.kwargs)
                self.start_time = self.start_time +self.interval
            else:
                sleep(sleep_ms / 1000.0)
                self.function(*self.args, **self.kwargs)
                self.start_time = self.start_time +self.interval

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time=int(time() * 1000)
            super().start()

    def cancel(self):
        self.is_running = False
