# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = '''
---
module: haproxy_backend
version_added: "1.0.0"
short_description: Manage Backends
description:
  - Used to Manage HA Proxy Backend
  - Create and Delete HA Proxy Bacnekends
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
    default: 'v2'
    type: str
  name:
    description:
      - The HA Proxy Backend Name
    required: true
    type: str
  mode:
    description:
      - The HA Proxy Backend Mode
    required: false
    choices: ['HTTP', 'TCP']
    default: 'HTTP'
    type: str
  transaction_id:
    description:
      - The Transaction ID (If need to execute action as part of API Transaction)
    required: false
    type: str
  state:
    description:
      - The Transaction State
    required: false
    choices: ['present', 'absent']
    default: 'present'
    type: str
'''

EXAMPLES = r'''
- name: "Create HA Proxy Backend"
  kube_cloud.haproxy.haproxy_backend:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    name: "jira-backend-service"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'present'

- name: "Create HA Proxy Backend"
  kube_cloud.haproxy.haproxy_backend:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    name: "jira-backend-service"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'absent'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kube_cloud.haproxy.plugins.module_utils.haproxy import haproxy_client


# Instantiate Ansible Module
def build_ansible_module():

    # Build Module Arguments Specification
    module_specification = dict(
        base_url=dict(type='str', required=True),
        username=dict(type='str', required=True, no_log=True),
        password=dict(type='str', required=True, no_log=True),
        api_version=dict(type='str', required=False, default='v2'),
        name=dict(type='str', required=True),
        mode=dict(type='str', required=False, default='HTTP', choices=['HTTP', 'TCP']),
        transaction_id=dict(type='str', required=False, default=''),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    # Build ansible Module
    return AnsibleModule(
        argument_spec=module_specification,
        supports_check_mode=True
    )


# Porcess Module Execution
def run_module(module, client):

    # Extract Module Parameters
    base_url = module.params['base_url']
    username = module.params['username']
    password = module.params['password']
    api_version = module.params['api_version']
    transaction_id = module.params['transaction_id']
    state = module.params['state']


# Entrypoint Function
def main():

    # Build Module
    module = build_ansible_module()

    # Build OVH Client from Module
    client = haproxy_client(module)

    # Execute Module
    run_module(module, client)


# If file is executed directly (pythos ovh_dns_record.py [not imported])
if __name__ == '__main__':

    # Launch Entrypoint
    main()
