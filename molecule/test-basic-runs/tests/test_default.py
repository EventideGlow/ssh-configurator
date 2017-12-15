import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.contains("alice")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_alice_added_with_ssh_key(host):
    assert host.user('alice')

    home = host.user('alice').home
    keysfile = host.file(os.path.join(home, '.ssh', 'authorized_keys'))

    assert keysfile.exists
    # Ensures Alice's key is the only one that's authorized for her user
    assert keysfile.content_string.strip() == "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDZ36QoIhiCE21EIidBkQX3MKqMP2n0XOK3CfXzguJcqW6wjAVi55I3h/cQjbSvSnfljr0kq/Ut/5kGMw3suO88yPwNe16l4ga8wfyZyhURNtJYUhRcvMWLnIN5Q+WvrDltxKICozvYz71gGkmBnM/j5qAhUYEnU42NXDCoCw3++fMj/8fU2tvUOaybe3lxTGsTikNREn3aIdXuIt2BCck9GFycbWvdGFS9fUaTkj57waXu9DMSqETbuKdaPyGdEEbgbP7+dQnaSi2C9FJd1OPasVU3FJCiP3AWblhJWpf0TZO86uCUfD3Y/6JsGilJIw2i1PQ+rjA3P2NdW+jUV8MZ"  # noqa: E127, E501


def test_eve_not_added(host):
    print(host.user('eve'))
    assert not host.user('eve').exists
