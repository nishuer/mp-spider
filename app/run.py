from .robot.toutiao_article import ToutiaoArticleRobot
from .account import toutiao_account

toutiao_history_robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "history"
    },
    "account": toutiao_account.account_15387579110,
    "profile_dir": "/Users/nishu/Library/Application Support/Firefox/Profiles/2m3vd669.robot"
})

toutiao_history_robot.run()
