# (c) 2024, Jean-Jacques ETUNE NGI <jetune@kube-cloud.com>
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


DOCUMENTATION = '''
---
module: backend
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
    type: dict
  httpchk:
    description:
      - The HA Proxy Backend Default HealthCheck Configuration
    required: false
    type: dict
  httpchk_params:
    description:
      - The HA Proxy Backend Secrver HealthCheck Configuration
    required: false
    type: dict
  transaction_id:
    description:
      - The Transaction ID (If need to execute action as part of API Transaction)
    required: false
    default: ""
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
  kube_cloud.haproxy.backend:
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
  kube_cloud.haproxy.backend:
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
from ..module_utils.client_backends import BackendClient
from ..module_utils.haproxy import haproxy_client
from ..module_utils.models import Balance, Backend, HttpHealthCheck, HttpCheckParams
from ..module_utils.enums import ProxyProtocol, LoadBalancingAlgorithm, HealthCheckType
from ..module_utils.enums import MatchType, TimeoutStatus, ErrorStatus, OkStatus, HttpMethod

try:
    from requests import HTTPError  # type: ignore
    IMPORTS_OK = True
except ImportError:
    IMPORTS_OK = False


# Find and Return Backend
def get_backend(module: AnsibleModule, client: BackendClient, name: str):

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
def update_backend(module: AnsibleModule, client: BackendClient, transaction_id: str, name: str, backend: Backend, force_reload: bool):

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
def create_backend(module: AnsibleModule, client: BackendClient, transaction_id: str, backend: Backend, force_reload: bool):

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
def delete_backend(module: AnsibleModule, client: BackendClient, transaction_id: str, name: str, force_reload: bool):

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
        balance=dict(type='dict', required=False, default=None),
        httpchk=dict(type='dict', required=False, default=None),
        httpchk_params=dict(type='dict', required=False, default=None),
        transaction_id=dict(type='str', required=False, default=''),
        force_reload=dict(type='bool', required=False, default=True),
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


# Build Requested Backend from Configuration
def build_requested_backend(params: dict) -> Backend:

    # Base Parameters Name
    base_param_names = [
        "name"
    ]

    # Build Requested Instance
    backend = Backend(
        **{k: v for k, v in params.items() if v is not None and k in base_param_names}
    )

    # Optional Initialization : mode
    backend.mode = ProxyProtocol.create(params['mode'])

    # Optional Initialization : balance
    if params.get('balance', None) is not None:

        # Extract balance
        p_balance = params.get['balance']

        # Initialize Object
        backend.balance = Balance(
            algorithm=LoadBalancingAlgorithm(p_balance.get('algorithm', None)),
            header=p_balance.get('header', None),
            ifnone=p_balance.get('ifnone', None),
            hash_expression=p_balance.get('hash_expression', None),
            hdr_name=p_balance.get('hdr_name', None),
            hdr_use_domain_only=p_balance.get('hdr_use_domain_only', None),
            random_draws=p_balance.get('random_draws', None),
            rdp_cookie_name=p_balance.get('rdp_cookie_name', None),
            uri_depth=p_balance.get('uri_depth', None),
            uri_len=p_balance.get('uri_len', None),
            uri_path_only=p_balance.get('uri_path_only', None),
            uri_whole=p_balance.get('uri_whole', None),
            url_param=p_balance.get('url_param', None),
            url_param_check_post=p_balance.get('url_param_check_post', None),
            url_param_max_wait=p_balance.get('url_param_max_wait', None)
        )

    # Optional Initialization : httpchk
    if params.get('httpchk', None) is not None:

        # Extract httpchk
        p_httpchk = params.get['httpchk']

        # Initialize Object
        backend.httpchk = HttpHealthCheck(
            type=HealthCheckType(p_httpchk.get('type', None)),
            method=p_httpchk.get('method', None),
            uri=p_httpchk.get('uri', None),
            uri_log_format=p_httpchk.get('uri_log_format', None),
            var_expr=p_httpchk.get('var_expr', None),
            var_format=p_httpchk.get('var_format', None),
            var_name=p_httpchk.get('var_name', None),
            var_scope=p_httpchk.get('var_scope', None),
            version=p_httpchk.get('version', None),
            via_socks4=p_httpchk.get('via_socks4', None),
            port=p_httpchk.get('port', None),
            port_string=p_httpchk.get('port_string', None),
            proto=p_httpchk.get('proto', None),
            send_proxy=p_httpchk.get('send_proxy', None),
            sni=p_httpchk.get('sni', None),
            ssl=p_httpchk.get('ssl', None),
            status_code=p_httpchk.get('status_code', None),
            tout_status=TimeoutStatus.create(p_httpchk.get('tout_status', None)),
            match=MatchType.create(p_httpchk.get('match', None)),
            headers=p_httpchk.get('headers', None),
            body=p_httpchk.get('body', None),
            body_log_format=p_httpchk.get('body_log_format', None),
            check_comment=p_httpchk.get('check_comment', None),
            default=p_httpchk.get('default', None),
            error_status=ErrorStatus.create(p_httpchk.get('error_status', None)),
            ok_status=OkStatus.create(p_httpchk.get('ok_status', None))
        )

    # Optional Initialization : httpchk_params
    if params.get('httpchk_params', None) is not None:

        # Extract httpchk_params
        p_httpchk_params = params.get['httpchk_params']

        # Initialize Object
        backend.httpchk_params = HttpCheckParams(
            method=HttpMethod(p_httpchk_params.get('method', None)),
            uri=p_httpchk_params.get('uri', None),
            version=p_httpchk_params.get('version', None)
        )

    # Return Backend
    return backend


# Porcess Module Execution
def run_module(module: AnsibleModule, client: BackendClient):

    # Extract Trasaction ID
    transaction_id = module.params['transaction_id']

    # Extract State
    state = module.params['state']

    # Extract Force Reload
    force_reload = module.params['force_reload']

    # Build Requested Instance
    backend = build_requested_backend(module.params)

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

    # Build Client from Module
    client = build_client(module).backend

    # Execute Module
    run_module(module, client)


# If file is executed directly (pythos ovh_dns_record.py [not imported])
if __name__ == '__main__':

    # Launch Entrypoint
    main()
