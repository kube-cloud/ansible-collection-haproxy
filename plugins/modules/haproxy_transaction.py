#!/usr/bin/python
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = '''
module: haproxy_transaction
version_added: "1.0.0"
short_description: Manage Transactions
description:
    - Used to Manage HA Proxy Transactions
    - Create, Validate and Delete HA Proxy Transactions
requirements: []
author: Jean-Jacques ETUNE NGI (@jetune) <jetune@kube-cloud.com>
options:
    base_url:
        description:
            - The HA Proxy Dataplane API Base URL
        required: true
        type: str
    username:
        description:
            - The HA Proxy Dataplane API Admin Username
        required: true
        type: str
    password:
        description:
            - The HA Proxy Dataplane API Password
        required: true
        type: str
    api_version:
        description:
            - The HA Proxy Dataplane API Version
        required: false
        type: str
    transaction_id:
      description:
            - The Transaction ID (only if state is 'validated' or 'absent')
        required: false
        type: str
    state:
        description:
            - The Transaction State
        required: false
        choices: ['present', 'validated', 'absent']
        default: 'present'
        type: str
    target:
        description:
            - The value of the record
            - It can be an IP, a FQDN, a text...
        required: true
        type: str
'''


EXAMPLES = r'''
- name: "Create HA Proxy Transaction"
  kube_cloud.haproxy.haproxy_transaction:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    state: 'present'
  register: haproxy_tx_result

  - name: "Validate HA Proxy Transaction"
  kube_cloud.haproxy.haproxy_transaction:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'validate'
  register: haproxy_tx_result

  - name: "Delete HA Proxy Transaction"
  kube_cloud.haproxy.haproxy_transaction:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'absent'
  register: haproxy_tx_result
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kube_cloud.haproxy.plugins.module_utils.haproxy import Client
