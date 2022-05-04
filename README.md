# Geno.me-Challenge-DevOps

System Administration and DevOps code challenge.

## Pre-requisites

1. [Virtualbox](https://www.virtualbox.org/wiki/Downloads) must be installed in your host machine.
2. [Vagrant](https://www.vagrantup.com/downloads) must be installed on your host machine. 
3. Optional: [Visual Studio Code](https://code.visualstudio.com/) or any Code Editor.

# How to run

- ```vagrant up```

# How to test

- ```curl -v http://localhost:5000/api/greeting```

# Research (Interesting links)

1. [vagrant@127.0.0.1: Permission denied](https://github.com/hashicorp/vagrant/issues/9831)
2. [How do I destroy a VM when I deleted the .vagrant file?](https://stackoverflow.com/questions/15408969/how-do-i-destroy-a-vm-when-i-deleted-the-vagrant-file)
3. [Host-Only Networking](https://www.virtualbox.org/manual/ch06.html#network_hostonly)
4. [How To Reset Your MySQL or MariaDB Root Password on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-reset-your-mysql-or-mariadb-root-password-on-ubuntu-20-04)
5. [Unable to change password for root account ansible](https://stackoverflow.com/questions/38433295/unable-to-change-password-for-root-account-ansible)
6. [Configuring MariaDB for Remote Client Access](https://mariadb.com/kb/en/configuring-mariadb-for-remote-client-access/)
7. [Virtualbox Networking](https://www.youtube.com/watch?v=VvNPUooobyE)
8. [Problem copying a file to remote host with Ansible](https://access.redhat.com/discussions/3916281)
9. [Status Code](https://stackoverflow.com/questions/42143115/which-status-code-is-correct-404-or-400-and-when-to-use-either-of-these)
10. [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) must be installed on your host machine.
11. sshpass must be installed: Ex. for Ubuntu use ```sudo apt install sshpass```

## Useful commands

- ```ansible-galaxy init dbserver```
- ```vagrant ssh -- -vvv```
