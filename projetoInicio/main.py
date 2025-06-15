#PEP8 são as boas práticas para codar em python
#Local onde será armazenado as tarefas
bancoDeDados = []

def adicionarTarefas(nomeDaTarefaParametro: str, 
                     descricaoTarefaParametro: str, 
                     prioridadeTarefaParametro: str,
                     categoriaTarefaParametro: str):
    
    """
    esta função tem como seu proposito armazenar tarefas
    """

    tarefa = {
        'nomeDaTarefa': nomeDaTarefaParametro,
        'descricaoDaTarefa': descricaoTarefaParametro,
        'prioridadeDaTarefa': prioridadeTarefaParametro,
        'categoriaDaTarefa': categoriaTarefaParametro
    }

    bancoDeDados.append(tarefa)
    return bancoDeDados


def listarTarefas():
    """
    Esta função tem como proposito listar todas as tarefas armazenadas
    """

    if len(bancoDeDados) == 0:
        return'Banco esta vazio!'
    else:
        return bancoDeDados
    
def marcarTarefaComoConcluida(nomeDaTarefa:str):
    """
    Esta funçao tem como proposito marcar a tarefa como concluida e remove-la do banco de dados
    """

    for tarefa in bancoDeDados:
       if nomeDaTarefa == tarefa['nomeDaTarefa']:
           posicao = bancoDeDados.index(tarefa)
           bancoDeDados.pop(posicao)

           return'tarefa marcada como concluida'
       
    return'tarefa inexistente'



def filtrarTarefasPorPrioridade(prioridade):
    listaFiltrada = []

    bancoDeDadosTupla = tuple(bancoDeDados) 

    for tarefa in bancoDeDadosTupla:
        if prioridade == tarefa ['prioridadeDaTarefa']:
            listaFiltrada.append(tarefa)

    return listaFiltrada



#adicionarTarefas(nomeDaTarefaParametro='Arrumar o quarto',descricaoTarefaParametro='no domingo eu preciso fazer uma faxina geral em meu quarto', prioridadeTarefaParametro='ALTA',categoriaTarefaParametro='LIMPEZA')

print('LISTA DE TAREFAS')
print('Escolha uma das opções abaixo para começar:')
print('1 - Adicionar Tarefa')
print('2 - Visualizar tarefas')
print('3 - Excluir tarefas')
print('4 - Sair')

escolhaDoUsuario = int(input('Digite a sua escolha: '))

match escolhaDoUsuario:
    case 1:
        nome_tarefa = input('Digite a tarefa que deseja adicionar: ')
        descricao_tarefa = input('Digite a descrição da tarefa que deseja adicionar: ')
        prioridade_tarefa = input('Digite a prioridade da tarefa que deseja adicionar(BAIXA, MEDIA ou ALTA): ')
        categoria_tarefa = input('Digite a categoria da tarefa que deseja adicionar: ')

        adicionarTarefas(nome_tarefa, descricao_tarefa, prioridade_tarefa, categoria_tarefa)
        print(bancoDeDados)

    case 2:
        print(bancoDeDados)
    case 3:
        print("Opção inválida")