from itertools import count
from operator import truediv
from models.LinkedList import LinkedList
def main():  #Função para a leitura dos valores introduzidos pelo utilizador
    lista_On = LinkedList()  #Defenição da lista como Lista Linkada
    while True:
        try:
            comandos = input().split()
        except EOFError:
            return
        if comandos[0] == "RPI":
            RPI(comandos[1], lista_On)
        elif comandos[0] == "RPF":
            RPF(comandos[1], lista_On)
        elif comandos[0] == "RPDE":
            RPDE(comandos[2], comandos[1], lista_On)
        elif comandos[0] == "RPAE":
            RPAE(comandos[2], comandos[1], lista_On)
        elif comandos[0] == "RPII":
            RPII(comandos[1], int(comandos[2]), lista_On)
        elif comandos[0] == "VNE":
            VNE(lista_On)
        elif comandos[0] == "VP":
            VP(comandos[1], lista_On)
        elif comandos[0] == "EPE":
            EPE(lista_On)
        elif comandos[0] == "EUE":
            EUE(lista_On)
        elif comandos[0] == "EP":
            EP(comandos[1], lista_On)


def RPI(pais, lista_On):
    lista_On.insert_at_start(pais)
    lista_On.traverse_list()
        
def RPF(pais, lista_On):
    lista_On.insert_at_end(pais)
    lista_On.traverse_list()

def RPDE(pais_existente, pais_novo, lista_On):
    lista_On.insert_after_item(pais_existente, pais_novo)
    lista_On.traverse_list()

def RPAE(pais_novo, pais_existeste, lista_On):
    lista_On.insert_before_item(pais_novo, pais_existeste)
    lista_On.traverse_list()

def RPII(pais, index,lista_On):
    lista_On.insert_at_index(pais, index)
    lista_On.traverse_list()

def VNE(pais, lista_On):
    conta_pais = lista_On.get_count(pais)
    print(f"O número de elementos são {conta_pais}")

def VP(pais, lista_On):
    if lista_On.search_item(pais) == True: 
        print(f"O país {pais} encontra-se na lista")
    else:
        print(f"O pais {pais} não se encontra na lista")

def EPE(lista_On):
    pais = lista_On.start_node.item
    lista_On.delete_at_start()
    print(f"O país {pais} foi eliminado da lista")

def EUE(lista_On):
    pais = lista_On.get_last_node
    lista_On.delete_at_end()
    print(f"O país {pais} foi eliminado da lista")

def EP(pais,lista_On):
    if lista_On.search_item(pais) == True:   
        lista_On.delete_element_by_value(pais)
        print(f"O país {pais} foi eliminado da lista")
    else:       
        print(f"O pais {pais} nao se encontra na lista")
    