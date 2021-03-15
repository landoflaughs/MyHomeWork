# -*- coding: gbk -*-
import os
import signal
import subprocess

import chardet
import pytest
from chardet import detect

from ui_framework.page.logger import log_init


@pytest.fixture(scope="module", autouse=True)
def record():
    log_init()
    # do sth before run
    # cmd is utf-8 encoded, so it must transcode to gbk,since windows cmd uses gbk codec
    # str can't be transcoded,so use list to do the job
    cmd = ["scrcpy -Nr tmp.mp4"]
    cmd1 = cmd[0].encode('gbk')
    cmd2 = str(cmd1, 'gbk')
    print(cmd2)
    p = subprocess.Popen(cmd2, shell=True)
    # ���������У���os.sys��ǿ��;�����Ҫ��������д����Ҫshell = true

    yield
    # do sth after test complete
    os.kill(p.pid, signal.CTRL_C_EVENT) # ȱ�� ctrl c��kill��pytest? ������windows���ٷ���bug�� linuxϵͳ����ֱ��kill����ok
