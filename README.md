# Geno.me-Challenge-DevOps

System Administration and DevOps code challenge.

## Pre-requisites

1. [Virtualbox](https://www.virtualbox.org/wiki/Downloads) must be installed in your host machine.
2. [Vagrant](https://www.vagrantup.com/downloads) must be installed on your host machine. 
3. [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) must be installed on your host machine. 
4. sshpass must be installed: Ex. for Ubuntu use ```sudo apt install sshpass```
5. Visual Studio Code or any Code Editor.

# How to run
- ```vagrant up```

# Research (Interesting links)

1. [vagrant@127.0.0.1: Permission denied](https://github.com/hashicorp/vagrant/issues/9831)
2. [How do I destroy a VM when I deleted the .vagrant file?](https://stackoverflow.com/questions/15408969/how-do-i-destroy-a-vm-when-i-deleted-the-vagrant-file)

## Useful commands
- ```ansible-galaxy init dbserver```
- ```vagrant ssh -- -vvv```
