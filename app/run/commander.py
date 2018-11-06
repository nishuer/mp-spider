import multiprocessing
import os

from .robot_food import robot as robot_food
from .robot_history import robot as robot_history
from .robot_joke import robot as robot_joke
from .robot_pet import robot as robot_pet

if __name__ == '__main__':
    print('Commander process %s.' % os.getpid())

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=robot_food.run, args=(lock,))
    p2 = multiprocessing.Process(target=robot_history.run, args=(lock,))
    p3 = multiprocessing.Process(target=robot_joke.run, args=(lock,))
    p4 = multiprocessing.Process(target=robot_pet.run, args=(lock,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    