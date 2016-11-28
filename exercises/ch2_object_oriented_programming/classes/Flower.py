class Flower:
    def __init__(self):
        """

        :param name: name of the flower
        :param petal: # of petals
        :param price: price of the flower
        :return:
        """
        self._name = 'default flower name'
        self._petal = 0
        self._price = 0.0

    def set_name(self,name):
        """
        set the name of the flower
        :param name: name of the flower
        :return:
        """
        if not isinstance(name,(str)):
            raise TypeError('name must be string')
        else:
            self._name = name

    def set_petal(self,petal):
        """
        set the number of petals
        :param petal: number of petals
        :return:
        """
        if not isinstance(petal,(int)):
            raise TypeError('petal must be int')
        else:
            self._petal = petal

    def set_price(self, price):
        """
        set the price
        :param price: the price of the flower
        :return:
        """
        if not isinstance(price, (float)):
            raise TypeError('price must be float')
        else:
            self._price = price

    def get_name(self):
        """

        :return: the name of the flower
        """
        return self._name

    def get_petal(self):
        """

        :return: the number of the petal
        """
        return self._petal

    def get_price(self):
        """

        :return: the price of the price
        """
        return self._price