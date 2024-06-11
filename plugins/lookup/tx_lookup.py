# (c) 2024, Jean-Jacques ETUNE NGI <jetune@kube-cloud.com>
# -*- coding: utf-8 -*-
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = '''
---
name: tx_lookup
version_added: "1.0.0"
short_description: Create and Return HA Proxy Dataplane API Transaction
description:
  - Used to Create and Return HA Proxy Dataplane API Transaction
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
'''

EXAMPLES = r'''
- name: "Create HA Proxy Dataplane API Transaction"
  ansible.builtin.debug: msg="{{item}}"
  transaction: "{{ lookup('kube_cloud.haproxy.tx_lookup', base_url='http://localhost:5555', username: 'admin', password: 'admin', api_version='v2') }}"
'''

RETURN = '''
_raw:
  description: HA Proxy Dataplane API Transaction Details
  type: dict
'''


from ansible.plugins.lookup import LookupBase
from ansible_collections.kube_cloud.haproxy.plugins.module_utils.haproxy import haproxy_client

try:
    from requests import HTTPError  # type: ignore
    IMPORTS_OK = True
except ImportError:
    IMPORTS_OK = False


class LookupModule(LookupBase):

    # Execute Plugin
    def run(self, terms, variables, **kwargs):

        # Build Client
        client = haproxy_client(variables)

        try:

            # Create and return Transaction
            return client.create_transaction()

        except HTTPError as api_error:

            # Rethrow
            raise HTTPError(msg="[Create Transaction] - Failed Create New Transaction ({0})".format(
                api_error
            ))
