import fun_rand as fun


class Element:
    nextId = 0

    def __init__(self,  delay=None, name=None, distribution=None):
        self.name = name
        self.t_next = [0]
        self.delay_mean = delay
        self.delay_dev = None
        self.distribution = distribution
        self.quantity = 0
        self.t_curr = self.t_next
        self.state = 0
        self.next_element = None
        self.id = Element.nextId
        Element.nextId += 1

    def get_delay(self):
        if 'exp' == self.distribution:
            return fun.exp(self.delay_mean)
        elif 'norm' == self.distribution:
            return fun.norm(self.delay_mean, self.delay_dev)
        elif 'uniform' == self.distribution:
            return fun.uniform(self.delay_mean, self.delay_dev)
        else:
            return self.delay_mean

    def in_act(self):
        pass

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def set_t_next(self, t_next_new):
        self.t_next = t_next_new

    def get_t_curr(self):
        return self.t_curr

    def out_act(self):
        self.quantity += 1

    def result(self):
        print(f'{self.name} quantity = {str(self.quantity)} state = {self.state}')

    def print_info(self):
        print(f'{self.name} state = {self.state} quantity = {self.quantity} t_next = {self.t_next}')

    def do_Statistics(self, delta):
        pass