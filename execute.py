#!/usr/bin/python
# encoding: utf-8

import sys
import subprocess
from workflow import Workflow, notify

log = None

def main(wf):
    qs = wf.args[0] if len(wf.args) else None
    if qs == 'wifi':
        networkset = ['networksetup', '-setairportpower', 'en0']
        networkget = ['networksetup', '-getairportpower', 'en0']
        status = subprocess.check_output(networkget).strip()
        log.debug(status)
        if status.endswith('Off'):
            networkset.append('on')
            subprocess.call(networkset)
            notify.notify(u'打开Wi-Fi', u'已开启')
        elif status.endswith('On'):
            networkset.append('off')
            subprocess.call(networkset)
            notify.notify(u'关闭Wi-Fi', u'已关闭')
    else:
        status = subprocess.check_output(
                ['networksetup', 
                '-getinfo', 
                'Wi-Fi'])
        log.debug(status)
        notify.notify(u'Wi-Fi信息', status)

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
