from .robot.toutiao_article import ToutiaoArticleRobot
from .account import toutiao_account


toutiao_animation_robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "animation"
    },
    "account": toutiao_account.account_15200878087
})

toutiao_animation_robot.run()
