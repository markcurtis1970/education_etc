### CFG - migrating config into Opscenter LCM json

This is a WIP something being done as a little side project

The Datastax OpsCenter API can be user to POST / GET (via curl) to pull a given config profile.
Generating a LCM config from a flat yaml file (i.e. `cassandra.yaml`) would be useful.

1. Install OpsCenter:

https://docs.datastax.com/en/install/6.7/install/opscInstallOpsc.html

2. Spin up some nodes (i.e. VMs)

3. Use LCM to install and setup the cluster:

https://docs.datastax.com/en/opscenter/6.7/opsc/LCM/opscLCMInstallDSE.html

4. Use the OpsCenter machien API to pull back a confgi profile

https://docs.datastax.com/en/opscenter/6.7/api/docs/lcm_walkthru.html#lcm-walkthru

eg: `curl 'http://localhost:8888/api/v2/lcm/config_profiles/' -s | json_pp`

Have a look at these examples

https://github.com/justinbreese/dse-opscenter-api-examples

5. See if theres a way to take a normal `cassandra.yaml` file and turn it into a `json` type format used for config profiles.
