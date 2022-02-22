import os

#lendo o arquivo de pontuação
with open('punctuation.txt', 'r') as f:
    punctuation = f.read()
punctuation = punctuation.split() #separando todas as pontuações e colocando em lista
#lendo o arquivo de stopwords
with open('stopwords_ptbr.txt', 'r', encoding="utf8") as f: 
    stopwords = f.read()
stopwords = stopwords.split("\n") #separando todas as stopwords e colocando em lista

path = "collection_docs"
docs = {}

for filename in os.listdir(path): #lendo os arquivos dentro do diretorio de caminho PATH
    with open(os.path.join(path, filename), 'r', encoding="utf8") as f: #abrindo arquivo com encoding utf8 para receber acentos adequadamente  
        docs[filename] = f.readlines() #salvando conteudo dos arquivos no dicionario de documentos

#dicionario de termos
dict_terms = {}

def prepare_doc(file): #file = filename
    document = str(docs.get(file)) #passando o conteudo para uma lista de string
    document = document.lower().replace("\\n", "") #convertendo tudo para minusculo  e retirando o \n
    for p in punctuation: #percorrendo o vetor de pontuação 
        document = document.replace(p, "") #retirando a pontuação da string
    document = document.split() #separando no espaço todas as palavras e inserindo em uma lista 
    document = [d for d in document if not d in stopwords] #inserindo na lista somente as palavras que NAO constam na lista de stopwords
    return document

def main():
    #tokenizando os documentos retirando pontuações e stopwords
    document01 = prepare_doc('doc1_patinho_feio.txt')
    document02 = prepare_doc('doc2_joao_maria.txt')
    document03 = prepare_doc('doc3_pinoquio.txt')
    document04 = prepare_doc('doc4_branca_neve.txt')
    document05 = prepare_doc('doc5_cinderela.txt')

    #ordenando os documentos por ordem alfabetica
    document01.sort()
    document02.sort()
    document03.sort()
    document04.sort()
    document05.sort()

    #criando indice invertido de cada um dos documentos e salvando no dicionario global dict_terms
    criar_indice_invertido(document01, '1')
    criar_indice_invertido(document02, '2')
    criar_indice_invertido(document03, '3')
    criar_indice_invertido(document04, '4')
    criar_indice_invertido(document05, '5')

    pesquisa = str(input("Entre com os termos da pesquisa:"))
    pesquisa = pesquisa.lower().split() #convertendo para minusculo e separando os termos

    docs_pesquisa = []

    for p in pesquisa: #percorrendo os termos de pesquisa fornecidos pelo usuário
        if dict_terms.get(p) is not None: #se o termo existir
            print(p+ " : " +dict_terms.get(p))
            aux = dict_terms.get(p) 
            aux = aux.split() 
            docs_pesquisa.append(aux) #inserindo o numero dos documentos de cada termo na lista
    
    if len(docs_pesquisa) == 0: #caso nenhum termo for encontrado, encerra
        print("Nenhum termo de pesquisa valido foi encontrado")
        exit()

    result_pesquisa = set(docs_pesquisa[0]) #convertendo a primeira posição para set
    for dc in range(len(docs_pesquisa)): #percorrendo o tamanho da lista
        docs_pesquisa[dc] = set(docs_pesquisa[dc]) #convertendo a lista em set
        result_pesquisa =  result_pesquisa.intersection(docs_pesquisa[dc]) #função de intersecção

    print("A pesquisa retornou termos em comum nos seguintes documentos: ",result_pesquisa)

def criar_indice_invertido(document, num): #criando indice invertido
    for d in document: #percorrendo o documento
        if d not in dict_terms:
            dict_terms[d] = num
        if d in dict_terms and num not in dict_terms[d]: #se o termo não esta no dict e não é um termo repetido
            x = str(dict_terms[d])+" "        
            dict_terms.update({d : x+num}) #atualiza a lista de documentos do termo

main()