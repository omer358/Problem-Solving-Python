from basic_data_structure.queue import Queue


def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        print("{} has been eliminate from the game".format(sim_queue.dequeue()))
    return "{} is the last one standing!".format(sim_queue.dequeue())


if __name__ == "__main__":
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
                      "Brad"], 7))
