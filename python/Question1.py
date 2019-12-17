# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    monthlyRepayment = (initialLevelOfDebt * repaymentPercentage)

    currentDebt = initialLevelOfDebt

    count = 0

    while currentDebt > monthlyRepayment:

        interest = currentDebt * interestPercentage
        # 50 = 1000 * 0.05

        print(currentDebt, interest, currentDebt+interest, currentDebt + interest - monthlyRepayment)

        currentDebt = currentDebt + interest - monthlyRepayment
        # 950 = 1000 + 50 - 100

        count+=1

    return round(count * monthlyRepayment + monthlyRepayment + currentDebt + currentDebt)

print(question01(1000, 0.05, 0.10))
