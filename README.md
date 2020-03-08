# Ansible Role: `aisbergg.sysctl`

This Ansible role configures the Linux kernel parameters.

## Requirements

Requires Python package `jmespath` to be installed on the host running the Ansible playbook.

## Role Variables

| Variable | Default | Comments |
|----------|---------|----------|
| `sysctl_conf` | `{}` | Dictionary of kernel parameters (key-value pairs) to save into `/etc/sysctl.conf` |
| `sysctl_clear_configurations` | `false` | Remove any left over configuration files (`/etc/sysctl.d/*.conf`) |
| `sysctl_d` | `[]` | List of kernel configuration files (`/etc/sysctl.d/*.conf`) |
| `sysctl_d.file` |  | File name (without extension) |
| `sysctl_d.order` | `00` | File order as a two-digit number |
| `sysctl_d.variables` | `{}` | Dictionary of kernel parameters (key-value pairs) |

## Example Playbook

```yaml
- hosts: all
  vars:
    sysctl_clear_configurations: true
    sysctl_conf:
      vm.dirty_ratio: 20
      vm.dirty_background_ratio: 15
    sysctl_d:
      - file: networking
        order: 10
        variables:
          net.ipv4.tcp_syncookies: true
          net.ipv4.ip_forward: false
      - file: security
        order: 20
        variables:
          kernel.dmesg_restrict: true
  roles:
    - role: sysctl
```

## License

MIT

## Author Information

Andre Lehmann (aisberg@posteo.de)
