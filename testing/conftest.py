from typing import List

import pytest
import sys
import yaml

# sys.path.append('..')


def get_datas(name, type='int'):
    with open(r'D:\PyCharmWork\MyHomeWork\testing\data\cal_add.yml', encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas, ids)


@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_add_int_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('add', 'minus')[0], ids=get_datas('add', 'minus')[1])
def get_add_minus_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_normal')[0], ids=get_datas('div', 'int_normal')[1])
def get_div_int_normal_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_error')[0], ids=get_datas('div', 'int_error')[1])
def get_div_int_error_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'minus')[0], ids=get_datas('div', 'minus')[1])
def get_dive_minus_with_fixture(request):
    return request.param


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')  #测试用例路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape') #测试用例名字

        if 'add' in item._nodeid:
            item.add_marker(pytest.mark.add)

    items.reverse() #反转顺序
