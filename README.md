# UHVPN from command line

scripting UH VPN access even after UH required authentication via web browser.

To run:

`python connect_UHVPN.py`

## Requirements
### Webdriver-manager & selenium
[Selenium](https://www.selenium.dev/documentation/) is for browser automation. It requires a browser driver. Follow the instructions [here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) depending on your OS to install one. Or get it all via the wonderful conda/mamba:

`mamba create -n selenium_env selenium webdriver-manager`

### Openconnect
Get openconnect via your favourite package manager (recommended) or from the [website](https://www.infradead.org/openconnect/).

## Compatibility
Tested under MacOS. Should run under Linux. Will most likely not run under Windows since it uses "sudo" to launch openconnect. 
