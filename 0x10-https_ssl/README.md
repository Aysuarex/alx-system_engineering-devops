# HTTPS SSL

In this project, I learned about the importance of HTTPS and how it works. I
configured my HolbertonBnB web servers with `certbot` certificate and HAproxy
SSL termination.

## Tasks :page_with_curl:

* **0. HTTPS ABC**
  * [0-https_abc](./0-https_abc): Text file containing answers to the
  following questions, one answer per line:
  * What is HTTPS?
    * A secure version of HTTP.
    * A faster version of HTTP.
    * A superior version of HTTP.
  * Why do you need HTTPS?
    * To encrypt credit card and social security number information going
    between the client and the website servers.
    * To encrypt all communication between the client and the website
    servers.
    * To accelerate the communication between the client and the website
    servers.
    * In a secure location where nobody can access it.
    * You can host it anywhere but you have to share the link to it on your
    website.
    * On your website web server(s).

* **1. World wide web**
  * [1-world_wide_web](./1-world_wide_web): Bash script that displays
  information about subdomains on my configured servers.
  * Usage: `./1-world_wide_web <domain> <subdomain>`
  * Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and
  points to [DESTINATION]`
  * If no `subdomain` parameter is passed, displays information about the
  subdomains `www`, `lb-01`, `web-01` and `web-02`, in that order.

* **2. HAproxy SSL termination**
  * [2-haproxy_ssl_termination](./2-haproxy_ssl_termination): HAproxy
  configuration file that accepts encrypted SSL traffic for the subdomain
  `www.` on TCP port 443.

* **3. No loophole in your website traffic**
  * [100-redirect_http_to_https](./100-redirect_http_to_https): HAproxy
  configuration file that automatically redirects HTTP traffic to HTTPS.
