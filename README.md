# Conference PC Scraper #

This script is useful in scrapping PC list (or any other committee list) from specified conferences and comparing them for overlapping PC members.

### Usage ###

In the example script, ``` IMC_PAM.py ``` I compare common PC members from [IMC 2020](https://conferences.sigcomm.org/imc/2020/committees/) and [PAM 2021](https://www.pam2021.b-tu.de/committees/). To use this script for the venues of your choice, replace the ```url``` variable with that of the desired conferences. Ensure that the **xpath** is correctly set for each ```<div>``` element that you are scraping (usually within a ```<ul>...</ul>```) -- then configure the ```tree.xpath(<your xpath>)``` in the script.
