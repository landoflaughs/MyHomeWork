import sys

import allure
import pytest
import yaml

from pythoncode.Calculator import Calculator


# def get_datas(name, type='int'):
#     with open('./data/cal_add.yml', encoding='utf-8') as f:
#         all_datas = yaml.safe_load(f)
#     datas = all_datas[name][type]['datas']
#     ids = all_datas[name][type]['ids']
#     return (datas,ids)

@pytest.fixture()
def get_instance():
    print('start calculating')
    calc: Calculator = Calculator()
    yield calc
    print('finish calculating')


class TestCal:
    # datas_add_int = get_datas('add','int')
    # datas_add_minus = get_datas('add', 'minus')
    # datas_div_int_normal = get_datas('div', 'int_normal')
    # datas_div_int_error = get_datas('div', 'int_error')
    # datas_div_minus = get_datas('div', 'minus')

    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])

    # pytest [test file] -s -q --alluredir=./testing/result/
    # allure serve ./testing/result/
    @allure.title("add_{get_add_int_with_fixture[0]}_{get_add_int_with_fixture[1]}")
    @allure.story("Add Integer Function")
    def test_add_int(self, get_instance, get_add_int_with_fixture):
        target = get_add_int_with_fixture
        assert target[2] == get_instance.add(target[0], target[1])

    # @pytest.mark.parametrize('a,b,result', datas_add_int[0], ids=datas_add_int[1])
    def test_add_minus(self, get_instance, get_add_minus_with_fixture):
        target = get_add_minus_with_fixture
        assert target[2] == get_instance.add(target[0], target[1])

    #
    # @pytest.mark.parametrize('a,b,result', datas_add_minus[0], ids=datas_add_minus[1])
    def test_div_int_normal(self, get_instance, get_div_int_normal_with_fixture):
        target = get_div_int_normal_with_fixture
        assert target[2] == get_instance.div(target[0], target[1])
        print(target[0], '/', target[1], '=', get_instance.div(target[0], target[1]))

    # @pytest.mark.parametrize('a,b,result', datas_div_int_normal[0], ids=datas_div_int_normal[1])
    # def test_div_int_normal(self,get_instance,a,b,result):
    #     assert result == get_instance.div(a,b)
    #     print(a, '/', b, '=', get_instance.div(a, b))

    # @pytest.mark.parametrize('a,b,result', datas_div_int_error[0], ids=datas_div_int_error[1])
    def test_div_int_error(self, get_instance, get_div_int_error_with_fixture):
        target = get_div_int_error_with_fixture
        with pytest.raises(ZeroDivisionError):
            get_instance.div(target[0], target[1])

    # @pytest.mark.parametrize('a,b,result', datas_div_minus[0], ids=datas_div_minus[1])
    def test_div_minus(self, get_instance, get_dive_minus_with_fixture):
        target = get_dive_minus_with_fixture
        assert target[2] == round(get_instance.div(target[0], target[1]), 2)
        # assert result == get_instance.div(a, b)
        print(target[0], '/', target[1], '=', get_instance.div(target[0], target[1]))

    # @pytest.mark.parametrize("a,b,result", datas[0], ids=datas[1])
    # def test_add(self, a, b, result):
    #     print(f'a={a},b={b},result={result}')
    #     assert result == self.cal.add(a, b)
    #
    # @pytest.mark.parametrize("a,b,result", datas[2], ids=datas[3])
    # def test_div(self,a,b,result):
    #     if b == 0:
    #         try:
    #             self.cal.div(a, b)
    #         except  ZeroDivisionError as e:
    #             print('dividend can not be zero')
    #             pytest.xfail(reason='dividend illeagle') #将这次结果设为xfail
    #     else:
    #         print(f'a={a},b={b},result={result}')
    #         assert result == self.cal.div(a,b)


# if __name__ == '__main__':
#     datas = get_datas_add()
#     print(datas[0],datas[1],datas[2],datas[3])
#
if __name__ == '__main__':
    pytest.main(["-s"])
