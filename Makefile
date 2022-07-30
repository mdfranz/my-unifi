UDM_HOST := root@192.168.0.1
DATA_DIR := /mnt/data_ext
CONFIG_DIR := /config
SCRIPTS_DIR := $(CONFIG_DIR)/scripts
VECTOR_DIR := $(DATA_DIR)/vector

.PHONY: push shell ssh build-image create-container rm-container 
.PHONY: recreate-container start-container container-shell start
.PHONY: requirements

push:
	ssh -Tq $(UDM_HOST) "mkdir -pv $(VECTOR_DIR) && rm -vf $(VECTOR_DIR)/*.toml"
	ssh -Tq $(UDM_HOST) "mkdir -pv $(SCRIPTS_DIR)"
	scp -Tqrp ./files/scripts $(UDM_HOST):$(CONFIG_DIR)/
	scp -Tqrp ./files/vector  $(UDM_HOST):$(DATA_DIR)/
	ssh -Tq $(UDM_HOST) "chmod -c u+rwx,g-rwx,o-rwx $(VECTOR_DIR)/vector.sh $(VECTOR_DIR)/vector"
	ssh -Tq $(UDM_HOST) "$(VECTOR_DIR)/vector validate"

test: 
	vector test ./files/vector/vector.d/*.toml

validate: 
	@ssh $(UDM_HOST) "cd $(VECTOR_DIR) && ./vector validate"

start: validate
	@ssh $(UDM_HOST) "ash -euc $(VECTOR_DIR)/vector.sh" || true

shell ssh:
	ssh $(UDM_HOST) 

dhcp-leases hosts:
	ssh $(UDM_HOST) cat /config/dnsmasq.lease | cut -d\  -f2,3,4 | column -t

build-image: push-config
	ssh $(UDM_HOST) docker build -t my-unifi -f $(VECTOR_DIR)/Dockerfile $(VECTOR_DIR)

create-container: 
	ssh $(UDM_HOST) docker container create --name=my-unifi --network=host my-unifi
# --mount='type=bind,source=/mnt/data,destination=/mnt/data' 

rm-container: 
	ssh $(UDM_HOST) docker container rm my-unifi

recreate-container: rm-container create-container

start-container: 
	ssh $(UDM_HOST) docker container start my-unifi

container-shell:
	ssh $(UDM_HOST) -t docker run --rm --network=host -it --entrypoint=/bin/sh my-unifi

.venv:
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt
requirements: .venv
	./.venv/bin/pip install -r requirements.txt
lab: .venv
	./.venv/bin/jupyter-lab

