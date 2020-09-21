class bot(object):
    """docstring"""

    def __init__(self, message, mekind, device):
        """объявляем переменные"""
        self.message = message
        self.mekind = mekind
        self.device = device
        self.time= input()

    def write(self):
        """сообщение"""
        return "writing a %s '%s' on %s at %s" % (self.mekind, self.message, self.device,self.time)

    def stop(self):
        """ответ на сообщение"""
        return "your %s '%s' is boring" % (self.mekind, self.message)


if __name__ == "__main__":
    vk = bot('я сделаю бота в телеграмме', 'voice message', 'iphone',)
    print(vk.write())
    telegram = bot('иди нахуй', 'voice message', 'samsung',)
    print(telegram.stop())
