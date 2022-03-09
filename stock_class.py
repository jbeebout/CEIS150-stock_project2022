#Jesse Beebout 61929
class Stock:
    def __init__(self, symbol=None, name=None, shares=None):
        if symbol is not None and name is not None and shares is not None:
            self._symbol = symbol
            self._name = name
            # number of shares owned
            self._shares = shares
            self.DataList = []

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, whatever):
        raise RuntimeWarning("Cannot Change stock symbol")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, shares):
        raise RuntimeWarning("use buy_shares or sell_shares func")

    def buy_shares(self, shares):
        self._shares += shares

    def sell_shares(self, shares):
        if self._shares - shares > 0:
            self._shares -= shares
        else:
            raise RuntimeWarning("cannot sell more shares than owned")


    def add_data(self, stock_data):
        self.DataList.append(stock_data)

        #print(self.DataList[0].date, self.DataList[0].close, self.DataList[0].volume)



class DailyData:
    def __init__(self, date, close, volume):

        self.date = date
        self.close = close
        self.volume = volume
        #print(date, close, volume)


# Unit Test - Do Not Change Code Below This Line *** *** *** *** *** *** *** *** ***
# main() is used for unit testing only. It will run when stock_class.py is run.
# Run this to test your class code. Once you have eliminated all errors, you are
# ready to continue with the next part of the project.

def main():
    error_count = 0
    error_list = []
    print("Unit Testing Starting---")
    # Test Add Stock
    print("Testing Add Stock...", end="")
    try:
        testStock = Stock("TEST", "Test Company", 100)
        print("Successful!")
    except:
        print("***Adding Stock Failed!")
        error_count = error_count + 1
        error_list.append("Stock Constructor Error")
    # Test Change Symbol
    # print("Test Change Symbol...", end="")
    # try:
    #     testStock.symbol = "NEWTEST"
    #     if testStock.symbol == "NEWTEST":
    #         print("Successful!")
    #     else:
    #         print("***ERROR! Symbol change unsuccessful.")
    #         error_count = error_count + 1
    #         error_list.append("Symbol Change Error")
    # except:
    #     print("***ERROR! Symbol change failed.")
    #     error_count = error_count + 1
    #     error_list.append("Symbol Change Failure")
    print("Test Change Name...", end="")
    try:
        testStock.name = "New Test Company"
        if testStock.name == "New Test Company":
            print("Successful!")
        else:
            print("***ERROR! Name change unsuccessful.")
            error_count = error_count + 1
            error_list.append("Name Change Error")
    except:
        print("***ERROR! Name change failed.")
        error_count = error_count + 1
        error_list.append("Name Change Failure")
        print("Test Change Name...", end="")
    # try:
    #     testStock.shares = 2000
    #     if testStock.shares == 2000:
    #         print("Successful!")
    #     else:
    #         print("***ERROR! Shares change unsuccessful.")
    #         error_count = error_count + 1
    #         error_list.append("Shares Change Error")
    # except:
    #     print("***ERROR! Shares change failed.")
    #     error_count = error_count + 1
    #     error_list.append("Shares Change Failure")

    # Test add daily data
    print("Creating daily stock data...", end="")
    daily_data_error = False
    try:
        dayData = DailyData("1/1/20", float(14.50), float(100000))
        testStock.add_data(dayData)
        if testStock.DataList[0].date != "1/1/20":
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Date")
        if testStock.DataList[0].close != 14.50:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Closing Price")
        if testStock.DataList[0].volume != 100000:
            error_count = error_count + 1
            daily_data_error = True
            error_list.append("Add Daily Data - Problem with Volume")
    except:
        print("***ERROR! Add daily data failed.")
        error_count = error_count + 1
        error_list.append("Add daily data Failure!")
        daily_data_error = True
    if daily_data_error == True:
        print("***ERROR! Creating daily data failed.")
    else:
        print("Successful!")

    if (error_count) == 0:
        print("Congratulations - All Tests Passed")
        second_test()
    else:
        print("-=== Problem List - Please Fix ===-")
        for em in error_list:
            print(em)

    print("Goodbye")



def second_test():
    error_count2 = 0
    error_list2 = []
    try:
        print("Testing creating second stock object...", end="")
        testStock2 = Stock("TEST", "TestCo", 1)
        if(testStock2.name is "TestCo" and testStock2.symbol is "TEST" and testStock2.shares == 1):
            print("Successful!")
        #print("stock attributes: \n", testStock2.symbol, testStock2.name, testStock2.shares)

    except:
        error_list2.append("Creating second stock object failed.")
    try:
        print("Testing buy_shares function...", end="")

        testStock2.buy_shares(2)
        #print("stock attributes: \n", testStock2.symbol, testStock2.name, testStock2.shares)
        if(testStock2.shares == 3):
            print("Successful!")
        else:
            error_list2.append("incorrect share count after buy_shares")
            raise Exception
    except:
        error_list2.append("buying shares failed")
    try:
        print("Testing sell_shares function...", end="")

        testStock2.sell_shares(2)
        #print("stock attributes: \n", testStock2.symbol, testStock2.name, testStock2.shares)
        if(testStock2.shares == 1):
            print("Successful")
        else:
            error_list2.append("incorrect share count after selling shares")
            raise Exception
    except:
        error_list2.append("selling shares failed")
    try:
        print("Testing sell_shares function...", end="")
        testStock2.sell_shares(4)
        #print("stock attributes: \n", testStock2.symbol, testStock2.name, testStock2.shares)

    except:
        if(testStock2.shares == 1):
            print("Successful!")
            #print("stock attributes: \n", testStock2.symbol, testStock2.name, testStock2.shares)
        else:
            error_list2.append("Failure: was able to sell more stock than owned.")

    error_count2 = len(error_list2)
    if(error_count2 > 0):
        print("Tests failed!")
        for item in error_list2:
            print(item, "\n")
    else:
        print("Congratulations - All Second Tests Passed")





    # Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    main()
