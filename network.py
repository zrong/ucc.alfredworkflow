#!/usr/bin/python
# encoding: utf-8

import sys
from workflow import Workflow, ICON_SWITCH, ICON_INFO

log = None
airport = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -z'

def main(wf):
    wf.add_item(u'Toggle Wi-Fi', u'打开或关闭Wi-Fi', arg='wifi', valid=True, icon=ICON_SWITCH)
    wf.add_item(u'Wi-Fi信息', u'查看网络信息', arg='info', valid=True, icon=ICON_INFO)
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
