#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StringCalculator:
    """
    Give sum of str arguments
    """

    def __init__(self):
        pass

    count_add = 0

    def add(self, str_chain):
        """
        add method : give sum for every string entrance
        :param str_chain: string of integers separated
        :return: sum(str_chain)
        """
        self.count_add += 1
        prefix_str = str_chain.split('\n', 1)
        stop_point = False

        try:
            delimiter = prefix_str[0].split('//', 1)[1]
            str_chain = prefix_str[1]
            if not delimiter.find("["):
                delimiter_count = delimiter.count('[')
                for i in range(delimiter_count):
                    new_delimiter = delimiter[delimiter.find("[") + 1:delimiter.find("]")]
                    str_chain = str_chain.replace(new_delimiter, ',')
                    delimiter = delimiter.replace('[{}]'.format(new_delimiter), '')
                delimiter = ','
        except IndexError:
            delimiter = ','
            str_chain = str_chain.replace('\n', delimiter)

        if not str_chain:
            return 0

        sum_list = [int(_) for _ in str_chain.split(delimiter)]

        for e in sum_list:
            if e < 0:
                stop_point = True
                print 'negative number : ' + str(e)
            if e > 1000:
                sum_list[sum_list.index(e)] = 0

        if stop_point:
            raise ValueError('negatives not allowed')

        return sum(sum_list)

    def GetCalledCount(self):
        return self.count_add


if __name__ == '__main__':
    a = StringCalculator()
    a.add('1')
    a.add('1\n2,3')
    a.add('//;\n2;3')
    a.add('//;\n2;3;1001')
    a.add('//***\n2***3***1001')
    a.add('//[***]\n2***3***1001')
    a.add('//[%%]\n2%%3%%1')
    a.add('//[%%][*]\n2%%3*1')
