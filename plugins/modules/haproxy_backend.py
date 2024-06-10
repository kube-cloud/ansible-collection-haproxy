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
requirements:
  - requests
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
  balance:
    description:
      - The HA Proxy Backend Load Balancing
    required: false
    default: {}
    type: dict
  httpchk:
    description:
      - The HA Proxy Backend Default HealthCheck Configuration
    required: false
    default: {}
    type: dict
  httpchk_params:
    description:
      - The HA Proxy Backend Secrver HealthCheck Configuration
    required: false
    default: {}
    type: dict
  transaction_id:
    description:
      - The Transaction ID (If need to execute action as part of API Transaction)
    required: false
    type: str
  force_reload:
    description:
      - Force reload HA Proxy Configuration
    required: false
    default: true
    type: bool
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
    mode: 'HTTP'
    balance:
      algorithm: roundrobin
      hdr_use_domain_only: false
      uri_path_only: false
      uri_whole: true
    httpchk_params:
      method: GET
      uri: "/login"
      version: "HTTP/1.1"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'present'

- name: "Create HA Proxy Backend"
  kube_cloud.haproxy.haproxy_backend:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    name: "jira-backend-service"
    mode: 'HTTP'
    balance:
      algorithm: roundrobin
      hdr_use_domain_only: false
      uri_path_only: false
      uri_whole: true
    httpchk_params:
      method: GET
      uri: "/login"
      version: "HTTP/1.1"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    state: 'absent'
'''

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.kube_cloud.haproxy.plugins.module_utils.haproxy import haproxy_client, ProxyProtocol, Balance, HttpHealthCheck, HttpCheckParams, Backend, Client

try:
    from requests import HTTPError  # type: ignore
    IMPORTS_OK = True
except ImportError:
    IMPORTS_OK = False


# Find and Return Backend
def get_backend(module: AnsibleModule, client: Client, name: str):

    try:

        # Call Client
        return client.get_backend(name=name)

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Find Backend] - Failed Get HA Proxy Backend (Name : {0}): {1}".format(
                name,
                api_error
            )
        )


# Update Backend
def update_backend(module: AnsibleModule, client: Client, transaction_id: str, name: str, backend: Backend, force_reload: bool):

    try:

        # Call Client
        return client.update_backend(
            name=name,
            backend=backend,
            transaction_id=transaction_id,
            force_reload=force_reload
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Update Backend] - Failed Update HA Proxy Backend (Name : {0} : [{1}]): {2}".format(
                name,
                backend,
                api_error
            )
        )


# Create Backend
def create_backend(module: AnsibleModule, client: Client, transaction_id: str, backend: Backend, force_reload: bool):

    try:

        # Call Client
        return client.create_backend(
            backend=backend,
            transaction_id=transaction_id,
            force_reload=force_reload
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Create Backend] - Failed Create HA Proxy Backend (Name : {0} : [{1}]): {2}".format(
                backend.name,
                backend,
                api_error
            )
        )


# Delete Backend
def delete_backend(module: AnsibleModule, client: Client, transaction_id: str, name: str, force_reload: bool):

    try:

        # Call Client
        return client.delete_backend(
            name=name,
            transaction_id=transaction_id,
            force_reload=force_reload
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Delete Backend] - Failed Delete HA Proxy Backend (Name : {0}): {1}".format(
                name,
                api_error
            )
        )


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
        balance=dict(type=dict, required=False, default={}),
        httpchk=dict(type=dict, required=False, default={}),
        httpchk_params=dict(type=dict, required=False, default={}),
        transaction_id=dict(type='str', required=False, default=''),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    # Build ansible Module
    return AnsibleModule(
        argument_spec=module_specification,
        supports_check_mode=True
    )


# Porcess Module Execution
def run_module(module: AnsibleModule, client: Client):

    # Extract Trasaction ID
    transaction_id = module.params['transaction_id']

    # Extract State
    state = module.params['state']

    # Extract Force Reload
    force_reload = module.params['force_reload']

    # Build Requested Instance
    backend = Backend(
        name=module.params['name'],
        mode=ProxyProtocol(module.params['mode']),
        balance=Balance(module.params['balance']),
        httpchk=HttpHealthCheck(module.params['httpchk']),
        httpchk_params=HttpCheckParams(module.params['httpchk_params'])
    )

    # Find Existing Instance
    existing_backend = get_backend(
        module=module,
        client=client,
        name=backend.name
    )

    # If Requested State is 'present' and Instance Already exists
    if existing_backend and state == 'present':

        # If Existing Instance match requested Instance
        if existing_backend == backend:

            # Initialize response (No Change)
            module.exit_json(
                msg="Backend [{0} - {1}] Not Changed".format(backend.name, backend.mode),
                changed=False
            )

            # Update Existing Instance
            update_backend(
                module=module,
                client=client,
                transaction_id=transaction_id,
                name=backend.name,
                backend=backend,
                force_reload=force_reload
            )

            # Module Response : Changed
            module.exit_json(
                changed=True,
                msg="Backend [{0} - {1}] Has Been Updated".format(backend.name, backend.mode)
            )

            # Initialize Module Response : Changed
            module.exit_json(
                changed=True,
                msg="[{0} - {1}] Has been Updated".format(backend.name, backend.mode)
            )

    # If Requested State is 'present' and Instance don't exists
    if not existing_backend and state == 'present':

        # Create Instance
        create_backend(
            module=module,
            client=client,
            transaction_id=transaction_id,
            backend=backend,
            force_reload=force_reload
        )

        # Initialize Module Response : Changed
        module.exit_json(
            changed=True,
            msg="[{0} - {1}] Has been Created".format(backend.name, backend.mode)
        )

    # If Requested State is 'absent' and Instance exists
    if existing_backend and state == 'absent':

        # Delete Instance
        delete_backend(
            module=module,
            client=client,
            transaction_id=transaction_id,
            name=backend.name,
            force_reload=force_reload
        )

        # Exit Module
        module.exit_json(
            msg="[{0} - {1}] Has been Deleted".format(backend.name, backend.mode),
            changed=True
        )

    # If Requested State is 'absent' and Instance don't exists
    else:

        # Initialize Response : No Change
        module.exit_json(
            msg="[{0} - {1}] Not Found".format(backend.name, backend.mode),
            changed=False
        )


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
