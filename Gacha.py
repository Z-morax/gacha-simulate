import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

class RealGacha:
    def __init__(self):
        self.base_rate = 0.006
        self.pity_5 = 0
        self.guaranteed = False

    def get_5star_probability(self):

        if self.pity_5 < 74:
            return self.base_rate
        else:

            return min(1.0, self.base_rate * (1.2 ** (self.pity_5 - 73)))

    def draw_once(self):

        self.pity_5 += 1

        prob = self.get_5star_probability()


        if random.random() < prob or self.pity_5 >= 90:
            self.pity_5 = 0


            if self.guaranteed:
                self.guaranteed = False
                return True

            if random.random() < 0.5:
                return True
            else:
                self.guaranteed = True
                return False

        return None

    def simulate(self, trials=500):
        results = []

        for _ in range(trials):
            self.pity_5 = 0
            self.guaranteed = False
            count = 0

            while True:
                count += 1
                result = self.draw_once()

                if result is True:  # 抽到UP
                    results.append(count)
                    break

        return results



gacha = RealGacha()
results = gacha.simulate(500)

print("真实抽卡模拟：")
print("平均抽数：", np.mean(results))
print("最欧：", min(results))
print("最非：", max(results))

# 画图
plt.hist(results, bins=50)
plt.title("真实抽卡分布（含50/50+保底）")
plt.xlabel("抽数")
plt.ylabel("人数")
plt.show()