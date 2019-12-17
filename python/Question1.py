# modify this function, and create other functions below as you wish
def question01(initialLevelOfDebt, interestPercentage, repaymentPercentage):
    monthlyRepayment = (initialLevelOfDebt * repaymentPercentage) / 100

    currentDebt = initialLevelOfDebt

    interestPercentage = 1 + interestPercentage / 100

    count = 0

    while currentDebt > monthlyRepayment:

        currentDebt = currentDebt * interestPercentage - monthlyRepayment;
        count+=1


        # 50 = 1000 * 0.05

        #print(currentDebt, interest, currentDebt+interest, currentDebt + interest - monthlyRepayment)



    return round(count * monthlyRepayment + currentDebt + 0.1 * initialLevelOfDebt)

print(question01(1000, 0.05, 0.10))
