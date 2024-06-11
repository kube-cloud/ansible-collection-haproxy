| Type	   | Status			|
|:---          |     :---:      |
| Sanity Checks | [![Sanity Checks](https://github.com/kube-cloud/ansible-collection-haproxy/actions/workflows/sanity-checks.yml/badge.svg)](https://github.com/kube-cloud/ansible-collection-haproxy/actions/workflows/sanity-checks.yml)     |
| Collection Publish | [![Collection Publish](https://github.com/kube-cloud/ansible-collection-haproxy/actions/workflows/sanity-checks.yml/badge.svg)](https://github.com/kube-cloud/ansible-collection-haproxy/actions/workflows/sanity-checks.yml)        |

# Ansible Collection : HA Proxy (kube_cloud.haproxy)

An Ansible Collection of modules and plugins that target HA Proxy Installation and Configuration on Linux Based Operating Systems.

## Included content

### Modules
Name | Description
--- | ---
[kube_cloud.haproxy.backend](https://github.com/kube-cloud/ansible-collection-haproxy/blob/main/docs/kube_cloud.haproxy.backend_module.rst)| Install and Configure HA Proxy.

## Installing this collection

### Python Requirements

- requests

### Ansible Dependencies

- community.general (>=4.0.0)

### Command

You can install the ``kube_cloud.haproxy`` collection with the Ansible Galaxy CLI:

```bash
ansible-galaxy collection install kube_cloud.haproxy
```

You can also include it in a `requirements.yml` file using the format:

```yaml
---
collections:
  - name: kube_cloud.haproxy
```

and install it with command :

```bash
ansible-galaxy collection install -r requirements.yml
```
