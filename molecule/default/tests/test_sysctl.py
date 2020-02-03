import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def assert_parameters(file_, parameters):
    for k, v in parameters.items():
        assert file_.contains("{} = {}".format(k, v))


def test_hosts_file(host):
    assert_parameters(
        host.file("/etc/sysctl.conf"),
        {
            "vm.dirty_ratio": 20,
            "vm.dirty_background_ratio": 15
        }
    )

    assert_parameters(
        host.file("/etc/sysctl.d/10-networking.conf"),
        {
            "net.ipv4.tcp_syncookies": 1,
            "net.ipv4.ip_forward": 0
        }
    )

    assert_parameters(
        host.file("/etc/sysctl.d/20-security.conf"),
        {
            "kernel.dmesg_restrict": 1
        }
    )
