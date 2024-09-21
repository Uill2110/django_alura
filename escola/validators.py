
from validate_docbr import CPF
import re


def invalid_cpf(cpf_number):
    cpf = CPF()
    valid_cpf = cpf.validate(cpf_number)
    return not valid_cpf

def invalid_name(name):
    return not name.isalpha()

def invalid_mobile_number(mobile_number):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    find = re.findall(model, mobile_number)
    return not find
