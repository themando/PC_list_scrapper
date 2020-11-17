import requests
import unidecode
import re
from lxml import html


def content_graber(conf):
    if conf == "imc":
        url = 'https://conferences.sigcomm.org/imc/2020/committees/'
    if conf == "pam":
        url = 'https://www.p am2021.b-tu.de/committees/'

    page = requests.get(url)
    tree = html.fromstring(page.content)

    gen_chair = tree.xpath('/html/body/main/ul[1]/li[1]/ul[1]/*/text()')

    if conf == "imc":
        pc_chair = tree.xpath('/html/body/main/ul[3]/*/text()')
    if conf == "pam":
        pc_chair = tree.xpath('/html/body/main/ul[2]/*/text()')

    if conf == "imc":
        pc = tree.xpath('/html/body/main/ul[4]/*/text()')
    if conf == "pam":
        pc = tree.xpath('/html/body/main/ul[3]/*/text()')

    return clean_list(gen_chair) + clean_list(pc_chair) + clean_list(pc)


def clean_list(pc_list):
    pc_list = [re.sub("[\(\[].*?[\)\]]", "", x) for x in pc_list]
    pc_list = [unidecode.unidecode(x) for x in pc_list]
    pc_list = [x.replace('\t', '').replace('\n', '').replace('(', '').replace(')', '').strip() for x in pc_list]
    pc_list = list(filter(None, pc_list))

    return pc_list

imc = content_graber("imc")
pam = content_graber("pam")

print(list(set(imc) & set(pam)))

