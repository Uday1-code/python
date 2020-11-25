import random


class CouponNumbers:

    def inputCoupons(self):
        try:
            numberOfCoupons = int(input("Enter number of distinct coupons"))
        except ValueError as e:
            print(e)
            self.inputCoupons()
        return numberOfCoupons

    @staticmethod
    def distinctCoupons(totalCoupons):
        distinctNumbers = []
        while len(distinctNumbers) <= totalCoupons:
            rand = random.randint(1, totalCoupons)
            if rand not in distinctNumbers:
                distinctNumbers.append(rand)
        return distinctNumbers


if __name__ == "__main__":
    couponNumbers = CouponNumbers()
    numbersOfCoupons = couponNumbers.inputCoupons()
    allDistinctCoupons = couponNumbers.distinctCoupons(numbersOfCoupons)
    print("All Distinct coupons are: ", allDistinctCoupons)
