# UHVPN from command line

Scripting UH VPN access from command line when authentication via web browser is required.

To run:

`python connect_UHVPN.py`

Advanced usage:

`python connect_UHVPN.py -u ab12ced@herts.ac.uk -p supersecurepassword123`

## Requirements
### Webdriver-manager & selenium
[Selenium](https://www.selenium.dev/documentation/) is for browser automation. It requires a browser driver. Follow the [instructions on the selenium site](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) depending on your OS to install one. Or get it all via the wonderful conda/mamba:

`mamba create -n selenium_env selenium webdriver-manager`

### Openconnect
Get openconnect via your favourite package manager (recommended) or from the [openconnect website](https://www.infradead.org/openconnect/).

## Compatibility
Tested under MacOS. Should run under Linux. Will most likely not run under Windows since it uses "sudo" to launch openconnect. 

NO WARRANTY. USE AT OWN RISK. 
