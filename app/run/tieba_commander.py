import multiprocessing
import os

from app.robot.tieba_poster import TiebaPoster
from app.robot.tieba_police import TiebaPolice
from app.robot.tieba_archive import TiebaArchive

from .tieba_poster_robot import config as tieba_poster_robot_config
from .tieba_police_robot import config as tieba_police_robot_config
from .tieba_archive_robot import config as tieba_archive_robot_config


def robotPosterFactory(*args):
    robot = TiebaPoster(*args)
    robot.run()

def robotPoliceFactory(*args):
    robot = TiebaPolice(*args)
    robot.run()

def robotArchiveFactory(*args):
    robot = TiebaArchive(*args)
    robot.run()

if __name__ == '__main__':
    print('Commander process %s.' % os.getpid())

    lock = multiprocessing.Lock()
    queue =  multiprocessing.Queue()

    # p1 = multiprocessing.Process(target=robotPosterFactory, args=(lock, queue, tieba_poster_robot_config))
    # p2 = multiprocessing.Process(target=robotPoliceFactory, args=(lock, queue, tieba_police_robot_config))
    p3 = multiprocessing.Process(target=robotArchiveFactory, args=(lock, queue, tieba_archive_robot_config))

    # p1.start()
    # p2.start()
    p3.start()

    # p1.join()
    # p2.join()
    p3.join()