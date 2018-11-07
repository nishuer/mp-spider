import multiprocessing
import os

from app.robot.toutiao_article import ToutiaoArticleRobot

from .robot_food import config as config_food
from .robot_history import config as config_history
from .robot_joke import config as config_joke
from .robot_pet import config as config_pet


def robotFactory(lock, config):
    robot = ToutiaoArticleRobot(config)
    robot.run(lock)

if __name__ == '__main__':
    print('Commander process %s.' % os.getpid())

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=robotFactory, args=(lock, config_food))
    p2 = multiprocessing.Process(target=robotFactory, args=(lock, config_history))
    p3 = multiprocessing.Process(target=robotFactory, args=(lock, config_joke))
    p4 = multiprocessing.Process(target=robotFactory, args=(lock, config_pet))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    