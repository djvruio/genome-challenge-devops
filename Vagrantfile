# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "bento/ubuntu-20.04"
  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.define "devel" do |devel|
    devel.vm.hostname = "develsrv"
    devel.vm.network "private_network", ip: "192.168.56.56"
    devel.vm.network "forwarded_port", guest: 3306, host: 3310
    devel.vm.network "forwarded_port", guest: 5000, host: 5010
    devel.vm.synced_folder "data", "/vagrant"
    devel.vm.synced_folder ".", "/vagrant"

    devel.vm.provision "ansible" do |a|
      a.limit = "all"
      a.playbook = "./provisioning/site.yaml"
      a.inventory_path = "./provisioning/hosts"
      a.verbose = "v"
    end
    devel.vm.post_up_message = "Successfully started developer (DEVEL) server box."
  end

end
