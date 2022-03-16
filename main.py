#Jesse Beebout 61929

from pynput.keyboard import Key, Listener

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




class MainMenu:
    def __init__(self):
        self._option_sel = 0
        self._option_menu = ["1: Buy Stock", "2: Sell Stock", "3: List Stock", "4: New DB"]
        MainMenu.print_menu(self)

    def print_menu(self):
        #print("\033[H\033[J")
        silly_count = 0
        for item in self._option_menu:
            if silly_count == self._option_sel:
                print("--->" + str(item) + "<---")
            else:
                print(str(item))
            silly_count += 1
        #MainMenu.grab_keys(self)

    #doesnt work well
    #def grab_keys(self):
        #keyboard.add_hotkey('page down', MainMenu.down_menu(self))
        #keyboard.add_hotkey('page up', MainMenu.up_menu(self))
        #keyboard.add_hotkey('enter', MainMenu.select_menu(self))
        #keyboard.wait('esc')

    def on_press(key):
        # print('{0} pressed'.format(
        # key))
        MainMenu.check_key(key)

    def on_release(key):
        # print('{0} release'.format(
        # key))
        if key == Key.esc:
            # Stop listener
            return False

    def check_key(self, key):
        #if key  [Key.up, Key.down, Key.left, Key.right]:
        if key == Key.up:
            MainMenu.down_menu(key)
        elif key == Key.down:
            MainMenu.up_menu(key)
        elif key == Key.enter:
            MainMenu.select_menu(key)

    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


    def select_menu(self):
        #TODO select case for different list items
        print('placeholder')
        if self._option_sel == 1:
            sharebuy = int(input("Buy how many shares?"))
            #Stock.buy_shares(self, sharebuy)
        elif self._option_sel == 2:
            sharesell = int(input("Sell how many shares?"))
            #Stock.sell_shares(self, sharesell)
        elif self._option_sel == 3:
            Stock.print_stocks
        elif self._option_sel == 4:
            DailyData(date, close, vol)
        else:
            #uh-oh
            raise



    def down_menu(self):
        if self._option_sel < len(self._option_menu)+1:
            self._option_sel += 1
            MainMenu.print_menu(self)

    def up_menu(self):
        if self._option_sel > 0:
            self._option_sel -= 1
            MainMenu.print_menu(self)






class DailyData:
    def __init__(self, date, close, volume):

        self.date = date
        self.close = close
        self.volume = volume
        #print(date, close, volume)



    # Program Starts Here
if __name__ == "__main__":
    # run unit testing only if run as a stand-alone script
    MainMenu()
