class building:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def msg(self):
        print(self.area, self.price)

    @classmethod
    def after_buyin_area(cls, area, price):
        return cls(area*area, price)


b2 = building.after_buyin_area(23, 5000)
b2.msg()
