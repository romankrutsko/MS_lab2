from gettext import npgettext
from process import Process
import numpy as np

class Model:
    def __init__(self, elements: list):
        self.list = elements
        self.event = 0
        self.t_next = 0.0
        self.t_curr = self.t_next

    def event1(self):
        pass

    def printStatistic(self):
       print(f"numCreate = {self.numCreate} numProcess = {self.numProcess} failure = {self.failure}")
   
    def print_info(self):
        for item in self.list:
         item.print_info()
   
    def simulate(self, time):
        while self.t_curr < time:
            self.t_next = float('inf')

            for e in self.list:
                t_next_val = np.min(e.t_next)
                if t_next_val < self.t_next:
                    self.t_next = t_next_val
                    self.event = e.id

            for e in self.list:
                e.do_Statistics(self.t_next - self.t_curr)

            self.t_curr = self.t_next

            for e in self.list:
                e.t_curr = self.t_curr

            if len(self.list) > self.event:
                self.list[self.event].out_act()

            for e in self.list:
                if self.t_curr in e.t_next:
                    e.out_act()

            self.print_info()

        return self.print_result()

    def print_result(self):
        mean_length_of_queue_average = 0
        failure_probability_average = 0
        mean_load_average = 0
        
        # print("\n-------------RESULTS-------------")
        for e in self.list:
            e.result()
            if isinstance(e,Process):

                mean_load = e.mean_load / self.t_curr

                print(f"mean length of queue ={e.mean_queue / self.t_curr} \nfailure probability  = {e.failure / e.quantity}")
                print(f"mean_load ={mean_load}")

                mean_load_average += mean_load
                failure_probability_average += e.failure / e.quantity
                mean_length_of_queue_average += e.mean_queue / self.t_curr
        mean_load_average = mean_load_average / len(self.list)
        failure_probability_average = failure_probability_average / len(self.list)
        mean_length_of_queue_average = mean_length_of_queue_average / len(self.list)

        return {'mean_load_average': mean_load_average,
         'failure_probability_average': failure_probability_average,
         'mean_length_of_queue_average': mean_length_of_queue_average}
