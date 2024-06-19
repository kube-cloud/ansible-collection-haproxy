# (c) 2024, Jean-Jacques ETUNE NGI <jetune@kube-cloud.com>
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = '''
---
module: server
version_added: "1.0.0"
short_description: Manage Servers
description:
    - Used to Manage HA Proxy Servers
    - Create, Update and Delete HA Proxy Servers
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
    transaction_id:
        description:
        - The Transaction ID
        required: false
        default: ""
        type: str
    force_reload:
        description:
        - Force reload HA Proxy Configuration
        required: false
        default: true
        type: bool
    parent_name:
        description:
        - The Server Parent Name
        required: true
        type: str
    parent_type:
        description:
        - The Server Parent Type
        required: true
        type: str
        choices: ['backend', 'frontend']
    name:
        description:
        - The Server Name
        required: true
        type: str
    address:
        description:
        - The Server Address
        required: true
        type: str
    port:
        description:
        - The Server Port
        required: true
        type: int
    verify:
        description:
            - The HA Proxy Server Configuration verify
        required: false
        type: str
        choices: ['NONE', 'REQUIRED', 'OPTIONAL']
    verifyhost:
        description:
            - The HA Proxy Server Configuration verifyhost
        required: false
        type: str
    weight:
        description:
            - The HA Proxy Server Configuration weight
        required: false
        type: int
    track:
        description:
            - The HA Proxy Server Configuration track
        required: false
        type: str
    ws:
        description:
            - The HA Proxy Server Configuration ws
        required: false
        type: str
        choices: ['AUTO', 'H1', 'H2']
    check:
        description:
            - The HA Proxy Server Configuration check
        required: false
        type: str
        choices: ['NONE', 'REQUIRED', 'OPTIONAL']
    health_check_address:
        description:
            - The HA Proxy Server Configuration health_check_address
        required: false
        type: str
    health_check_port:
        description:
            - The HA Proxy Server Configuration health_check_port
        required: false
        type: int
    max_reuse:
        description:
            - The HA Proxy Server Configuration max_reuse
        required: false
        type: int
    maxconn:
        description:
            - The HA Proxy Server Configuration maxconn
        required: false
        type: int
    maxqueue:
        description:
            - The HA Proxy Server Configuration maxqueue
        required: false
        type: int
    minconn:
        description:
            - The HA Proxy Server Configuration minconn
        required: false
        type: int
    state:
        description:
            - The Transaction State
        required: false
        choices: ['present', 'absent']
        default: 'present'
        type: str
'''

EXAMPLES = r'''
- name: "Create HA Proxy Server"
  kube_cloud.haproxy.server:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    force_reload: true
    parent_name: "test_frontend"
    parent_type: "frontend"
    name: "server1"
    address: "127.0.0.1"
    port: 8080
    state: 'present'

- name: "Cancel HA Proxy Dataplane API Transaction"
  kube_cloud.haproxy.server:
    base_url: "http://localhost:5555"
    username: "admin"
    password: "admin"
    api_version: "v2"
    transaction_id: "88a7601b-6960-4263-873f-b5e3040c80a2"
    force_reload: true
    name: "server1"
    parent_name: "test_frontend"
    parent_type: "frontend"
    state: 'absent'
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.client_servers import ServerClient
from ..module_utils.models import Server
from ..module_utils.haproxy import haproxy_client
from ..module_utils.enums import WebSocketProtocol, Requirement
from ..module_utils.commons import filter_none

try:
    from requests import HTTPError  # type: ignore
    IMPORTS_OK = True
except ImportError:
    IMPORTS_OK = False


# Find and Return Server
def get_server(client: ServerClient, name: str, parent_name: str, parent_type: str):

    try:

        # Call Client
        return client.get_server(
            name=name,
            parent_name=parent_name,
            parent_type=parent_type
        )

    except HTTPError:

        # Return None
        return None


# Update Server
def update_server(module: AnsibleModule, client: ServerClient, transaction_id: str,
                  name: str, parent_name: str, parent_type: str, server: Server, force_reload: bool):

    try:

        # Call Client
        return client.update_server(
            name=name,
            parent_name=parent_name,
            parent_type=parent_type,
            force_reload=force_reload,
            server=server,
            transaction_id=transaction_id
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Update Server] - Failed Update HA Proxy Server (Name :  {0}, Parent : {1}:{2}): {3}".format(
                name,
                parent_name,
                parent_type,
                api_error
            )
        )


# Create Server
def create_server(module: AnsibleModule, client: ServerClient, transaction_id: str,
                  parent_name: str, parent_type: str, server: Server, force_reload: bool):

    try:

        # Call Client
        return client.create_server(
            server=server,
            transaction_id=transaction_id,
            force_reload=force_reload,
            parent_name=parent_name,
            parent_type=parent_type
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Create Server] - Failed Update HA Proxy Server (Server : {0}, Parent : {1}:{2}): {3}".format(
                server.name,
                parent_name,
                parent_type,
                api_error
            )
        )


# Delete Backend
def delete_server(module: AnsibleModule, client: ServerClient, transaction_id: str,
                  name: str, parent_name: str, parent_type: str, force_reload: bool):

    try:

        # Call Client
        return client.delete_server(
            name=name,
            parent_name=parent_name,
            parent_type=parent_type,
            transaction_id=transaction_id,
            force_reload=force_reload
        )

    except HTTPError as api_error:

        # Set Module Error
        module.fail_json(
            msg="[Delete Server] - Failed Delete HA Proxy Server (Name :  {0}, Parent : {1}:{2}): {3}".format(
                name,
                parent_name,
                parent_type,
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
        transaction_id=dict(type='str', required=False, default=''),
        force_reload=dict(type='bool', required=False, default=True),
        parent_name=dict(type='str', required=True),
        parent_type=dict(type='str', required=True, choices=['frontend', 'backend']),
        name=dict(type='str', required=True),
        address=dict(type='str', required=True),
        port=dict(type='int', required=True),
        verify=dict(type='str', required=False, choices=Requirement.names()),
        verifyhost=dict(type='str', required=False),
        weight=dict(type='int', required=False),
        track=dict(type='str', required=False),
        ws=dict(type='str', required=False, choices=WebSocketProtocol.names()),
        check=dict(type='str', required=False, choices=Requirement.names()),
        health_check_address=dict(type='str', required=False),
        health_check_port=dict(type='int', required=False),
        max_reuse=dict(type='int', required=False),
        maxconn=dict(type='int', required=False),
        maxqueue=dict(type='int', required=False),
        minconn=dict(type='int', required=False),
        state=dict(type='str', required=False, default='present', choices=['present', 'absent'])
    )

    # Build ansible Module
    return AnsibleModule(
        argument_spec=module_specification,
        supports_check_mode=True
    )


# Instantiate Ansible Module
def build_client(module: AnsibleModule):

    try:

        # Build Client from Module
        return haproxy_client(module.params)

    except ValueError:

        # Set Module Error
        module.fail_json(
            msg="[Build Client] - Failed Build HA Proxy Dataplane API Client"
        )


# Build Requested Server from Configuration
def build_requested_server(params: dict) -> Server:

    # Base Parameters Name
    base_param_names = [
        "name", "address", "port",
        "verifyhost", "weight", "track", "health_check_address",
        "health_check_port", "max_reuse", "maxconn", "maxqueue",
        "minconn"
    ]

    # Build Requested Instance
    server = Server(
        **{k: v for k, v in params.items() if v is not None and k in base_param_names}
    )

    # Initialize Enums
    server.verify = Requirement.create(params.get('verify', None))
    server.ws = WebSocketProtocol.create(params.get('ws', None))
    server.check = Requirement.create(params.get('check', None))

    # Build Requested Instance
    return server


# Porcess Module Execution
def run_module(module: AnsibleModule, client: ServerClient):

    # Extract Trasaction ID
    transaction_id = module.params['transaction_id']

    # Extract State
    state = module.params['state']

    # Extract Force Reload
    force_reload = module.params['force_reload']

    # Server Name
    name = module.params['name']

    # Server Parent Name
    parent_name = module.params['parent_name']

    # Server Parent Type
    parent_type = module.params['parent_type']

    # Find Existing Instance
    existing_instance = get_server(
        client=client,
        name=name,
        parent_name=parent_name,
        parent_type=parent_type
    )

    # Build Requested Instance
    server = build_requested_server(module.params)

    # If Requested State is 'present' and Instance Already exists
    if existing_instance and state == 'present':

        # If Existing Instance match requested Instance
        if existing_instance == name:

            # Initialize response (No Change)
            module.exit_json(
                msg="Server [Parent : {0}/{1}, Name : {2}] Not Changed".format(
                    parent_name,
                    parent_type,
                    server.name
                ),
                changed=False
            )

        # Update Existing Instance
        update_server(
            module=module,
            client=client,
            transaction_id=transaction_id,
            server=server,
            name=name,
            parent_name=parent_name,
            parent_type=parent_type,
            force_reload=force_reload
        )

        # Module Response : Changed
        module.exit_json(
            changed=True,
            instance=filter_none(server),
            parent_name=parent_name,
            parent_type=parent_type,
            msg="Server [Parent : {0}/{1}, Name : {2}] Has Been Updated".format(
                parent_name,
                parent_type,
                server.name
            )
        )

    # If Requested State is 'present' and Instance don't exists
    if not existing_instance and state == 'present':

        # Create Instance
        create_server(
            module=module,
            client=client,
            transaction_id=transaction_id,
            force_reload=force_reload,
            parent_name=parent_name,
            parent_type=parent_type,
            server=server
        )

        # Initialize Module Response : Changed
        module.exit_json(
            changed=True,
            instance=filter_none(server),
            parent_name=parent_name,
            parent_type=parent_type,
            msg="Server [Parent : {0}/{1}, Name : {2}] Has Been Created".format(
                parent_name,
                parent_type,
                server.name
            )
        )

    # If Requested State is 'absent' and Instance exists
    if existing_instance and state == 'absent':

        # Delete Instance
        delete_server(
            module=module,
            client=client,
            transaction_id=transaction_id,
            force_reload=force_reload,
            name=server.name,
            parent_name=parent_name,
            parent_type=parent_type
        )

        # Exit Module
        module.exit_json(
            changed=True,
            instance=filter_none(server),
            parent_name=parent_name,
            parent_type=parent_type,
            msg="Server [Parent : {0}/{1}, Name : {2}] Has Been Deleted".format(
                parent_name,
                parent_type,
                server.name
            )
        )

    # If Requested State is 'absent' and Instance don't exists
    else:

        # Initialize Response : No Change
        module.exit_json(
            msg="Server Not Found [Parent : {0}/{1}, Name : {2}]".format(
                parent_name,
                parent_type,
                server.name
            ),
            changed=False
        )


# Entrypoint Function
def main():

    # Build Module
    module = build_ansible_module()

    # Build Client from Module
    client = build_client(module).server

    # Execute Module
    run_module(module, client)


# If file is executed directly (pythos ovh_dns_record.py [not imported])
if __name__ == '__main__':

    # Launch Entrypoint
    main()
