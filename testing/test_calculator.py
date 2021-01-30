import sys
import pytest
import yaml

sys.path.append('..')

from pythoncode.Calculator import Calculator


def get_datas_add():
    with open('./data/cal_add.yml') as f:
        datas = yaml.safe_load(f)
    return datas['add']['datas'], datas['add']['ids'], datas['div']['datas'], datas['div']['ids']


class TestCal:
    datas: list = get_datas_add()

    def setup_class(self):
        print('start calculating')
        self.cal = Calculator()

    def teardown_class(self):
        print('calculating finished')

    @pytest.mark.parametrize("a,b,result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        print(f'a={a},b={b},result={result}')
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize("a,b,result", datas[2], ids=datas[3])
    def test_div(self,a,b,result):
        if b == 0:
            try:
                self.cal.div(a, b)
            except  ZeroDivisionError as e:
                print('dividend can not be zero')
                pytest.xfail(reason='dividend illeagle') #将这次结果设为xfail
        else:
            print(f'a={a},b={b},result={result}')
            assert result == self.cal.div(a,b)

# if __name__ == '__main__':
#     datas = get_datas_add()
#     print(datas[0],datas[1],datas[2],datas[3])
if __name__ == '__main__':
    pytest.main(["-s"])
