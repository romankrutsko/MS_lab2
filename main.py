import pandas as pd
from tabulate import tabulate
from create import Create
from model import Model
from process import Process

count = 10
delays = {
    "create": [4, 2, 5, 2, 1, 3, 7, 3, 7, 2],
    "p1": [4, 4, 4, 3, 5, 3, 5, 2, 1, 3],
    "p2": [4, 3, 4, 7, 3, 3, 2, 2, 2, 2],
    "p3": [4, 2, 5, 6, 4, 3, 1, 2, 4, 2],
}
max_queue = {
    "p1": [5, 5, 2, 5, 1, 4, 3, 3, 2, 2],
    "p2": [5, 3, 2, 2, 1, 4, 3, 2, 1, 2],
    "p3": [5, 2, 5, 5, 1, 2, 3, 3, 2, 5],
}

df = pd.DataFrame()
rows = []
for i in range(count):
    # two processes

    # c = Create(5)
    # p1 = Process(5, 3)
    # c.next_element = p1
    #
    # c.distribution = "exp"
    # p1.distribution = "exp"
    #
    # c.name = "creator"
    # p1.name = "processor"
    #
    # elementsList = [c, p1]

    c = Create(delays["create"][i])
    p1 = Process(delays["p1"][i])
    p2 = Process(delays["p2"][i])
    p3 = Process(delays["p3"][i])

    c.next_element = p1
    p1.next_element = [p2]
    p2.next_element = [p3]

    p1.max_queue = max_queue["p1"][i]
    p2.max_queue = max_queue["p2"][i]
    p3.max_queue = max_queue["p3"][i]

    c.name = "CREATOR"
    p1.name = "PROCESSOR1"
    p2.name = "PROCESSOR2"
    p3.name = "PROCESSOR3"

    c.distribution = "exp"
    p1.distribution = "exp"
    p2.distribution = "exp"
    p3.distribution = "exp"

    elements_list = [c, p1, p2, p3]

    model = Model(elements_list)
    result = model.simulate(1000.0)

    param = {
        'delay_create': delays["create"][i],
        'delay_p1': delays["p1"][i],
        'delay_p2': delays["p2"][i],
        'delay_p3': delays["p3"][i],
        'max_queue_p1': max_queue["p1"][i],
        'max_queue_p2': max_queue["p2"][i],
        'max_queue_p3': max_queue["p3"][i],
        'p1_processed': p1.quantity,
        'process1_failed': p1.failure,
        'p2_processed': p2.quantity,
        'process2_failed': p2.failure,
        'p3_processed': p3.quantity,
        'process3_failed': p3.failure
    }

    rows.append({**param, **result})

df = df.append(rows)
df.to_excel("results.xlsx")
print(tabulate(df, headers='keys', tablefmt='fancy_grid', numalign="center"))