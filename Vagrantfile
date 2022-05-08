# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "bento/ubuntu-20.04"
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.define "database" do |db|
    db.vm.hostname = "dbsrv"
    db.vm.network "private_network", ip: "192.168.56.57"
    db.vm.network "forwarded_port", guest: 3306, host: 3306

    db.vm.provision "ansible_local" do |a|
      a.verbose = true
      a.become = true
      a.limit = "database"
      a.playbook = "./provisioning/site.yaml"
      a.inventory_path = "./provisioning/hosts"
    end
    db.vm.post_up_message = "Successfully started database (DB) server box."
  end
  
  config.vm.define "devel" do |devel|
    devel.vm.hostname = "develsrv"
    devel.vm.network "private_network", ip: "192.168.56.56"
    devel.vm.network "forwarded_port", guest: 80, host: 8080
    devel.vm.synced_folder ".", "/vagrant"

    devel.vm.provision "ansible_local" do |a|
      a.verbose = true
      a.become = true
      a.limit = "devel"
      a.playbook = "./provisioning/site.yaml"
      a.inventory_path = "./provisioning/hosts"
    end
    devel.vm.post_up_message = "Successfully started developer (DEVEL) server box."
  end

end
