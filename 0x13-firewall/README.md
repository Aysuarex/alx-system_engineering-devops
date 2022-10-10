# Firewall

In this project, I used `ufw` to configure firewalls on my issued web servers.

## Tasks :page_with_curl:

* **0. Firewall ABC**
  * [0-firewall_ABC](./0-firewall_ABC): Text file containing answers to the the
  following multiple-choice questions, one per line:
  * What is a firewall?
	  * A hardware security system.
	  * A hardware or software security system.
	  * A software security system.
	* What are the 2 types of firewall?
	  * Soft and hard firewall
	  * Incoming and outgoing firewall.
	  * Network and host-based firewall.
	* What is the main function of a firewall?
	  * To filter incoming and outgoing network traffic.
	  * To filter incoming and outgoing TCP traffic.
	  * To filter outgoing traffic.

* **1. Block all incoming traffic but**
  * [1-block_all_incoming_traffic_but](./1-block_all_incoming_traffic_but): Bash
  script that installs a `ufw` firewall to block all incoming traffic except for
  ports `22`, `443` and `80` on a web server.

* **2. Port forwarding**
  * [100-port_forwarding](./100-port_forwarding): `ufw` configuration file that
  configures a firewall to redirect port `8080/TCP` to port `80/TCP`.
