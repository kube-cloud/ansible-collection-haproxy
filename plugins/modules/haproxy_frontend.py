#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = '''
'''


EXAMPLES = r'''
- name: "Create HA Proxy Frontend"
  kube_cloud.haproxy.haproxy_frontend:
    endpoint: "ovh-eu"
    application_key: "2566789999999999"
    application_secret: "me4567009132467nhst5"
    consumer_key: "po230O851Ujjhr3"
    domain: "kube-cloud.com"
    record_name: "demo.test"
    record_type: "TXT"
    target: "VALUE TO SET"
    state: 'present'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kube_cloud.haproxy.plugins.module_utils.haproxy import Client

