import os
from os import listdir
from os.path import isfile, join

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_alice_added(host):
    assert host.user('alice')

    home = host.user('alice').home
    ssh_dir = os.path.join(home, '.ssh/')
    onlyfiles = [f for f in listdir(ssh_dir) if isfile(join(ssh_dir, f))]
    print(onlyfiles)
    assert False
