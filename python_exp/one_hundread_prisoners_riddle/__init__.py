# idea from Vertasium video: https://www.youtube.com/watch?v=iSNsgj1OCLA

from typing import Callable
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


def no_strategy(number: int, boxes: list[int]) -> bool:
    open_boxes = random.sample(boxes, int(len(boxes) / 2))
    return number in open_boxes


def loop_strategy(number: int, boxes: list[int]) -> bool:
    found = False
    num_box_opened = 1
    limit = int(len(boxes) / 2)
    next = boxes[number]
    while not found and num_box_opened <= limit:
        if next == number:
            found = True
        else:
            next = boxes[next]
            num_box_opened += 1
    return found


def test(
    sample_size: int, num_prisoners: int, strategy: Callable[[int, list[int]], bool]
):
    samples = []
    for _ in range(0, sample_size):
        boxes = list(range(0, num_prisoners))
        np.random.shuffle(boxes)

        total_found = 0
        for n in range(0, num_prisoners):
            if strategy(n, boxes):
                total_found += 1
        samples.append(total_found)
    return samples


if __name__ == "__main__":
    num_prisoners = 100
    sample_size = 1000

    loop_strategy_samples = test(sample_size, num_prisoners, loop_strategy)
    no_strategy_samples = test(sample_size, num_prisoners, no_strategy)

    plt.hist(
        loop_strategy_samples, bins=100, density=True, color="b", label="Loop strategy"
    )
    plt.hist(
        no_strategy_samples, bins=100, density=True, color="g", label="No strategy"
    )
    plt.xlabel("Number of prisoners who found their numbers")
    plt.ylabel("Probability")
    plt.xticks(np.arange(start=0, stop=101, step=10), rotation=45)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.legend()
    plt.show()
