from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "pet"
    },
    "account": toutiao_account.pet_13975896275,
    "profile_dir": r"C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\ivft84z1.robot3",
})

robot.run()
