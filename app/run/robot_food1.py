from app.robot.toutiao_article import ToutiaoArticleRobot
from app.account import toutiao_account

robot = ToutiaoArticleRobot({
    "source": {
        "platform": "sohu",
        "category": "food"
    },
    "account": toutiao_account.food_18707496278,
    "profile_dir": "/Users/nishu/Library/Application Support/Firefox/Profiles/01ky36ih.robot2"
})

robot.run()
