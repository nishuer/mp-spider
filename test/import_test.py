from app.run.robot_star import config
from app.robot.toutiao_lab import ToutiaoLab


title = '有一种天真叫, 竟与王珂这样挑衅, 有谁注意到刘涛的表情了?'

robot = ToutiaoLab(config)

print(robot.matchRiseKeyword(title))

