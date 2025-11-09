"""Módulo principal para o gerenciamento de tarefas CRUD, incluindo priorização por Criticidade."""
import json
import os

DATA_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        # Garante que o arquivo não está vazio antes de tentar carregar JSON
        content = f.read()
        if not content:
            return []
        f.seek(0) # Volta ao início do arquivo se precisar ler novamente
        return json.loads(content)


def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def create_task(title, description, criticidade="Baixa"): # Adiciona valor default
    tasks = load_tasks()

    # Validação simples da criticidade
    valid_criticities = ["Baixa", "Média", "Alta"]
    if criticidade not in valid_criticities:
        print(f"Erro: Criticidade inválida '{criticidade}'. Usando 'Baixa'.")
        criticidade = "Baixa"

    new_id = max([t['id'] for t in tasks], default=0) + 1
    new_task = {
        'id': new_id,
        'title': title,
        'description': description,
        'status': 'A Fazer',
        'criticidade': criticidade # NOVO CAMPO
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa '{title}' criada com sucesso com Criticidade: {criticidade}!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for task in tasks:
        criticidade = task.get('criticidade', 'N/A') # Pega o novo campo
        print(f"ID: {task['id']} | Título: {task['title']} | Status: {task['status']} | Criticidade: {criticidade}")
    print("----------------------")

# Demonstração de uso
if __name__ == "__main__":
    print("--- Sistema Básico de Gerenciamento de Tarefas ---")

    # 1. Cria uma tarefa inicial com ALTA criticidade
    create_task("Configurar ambiente de produção", "Instalar dependências no servidor.", "Alta")

    # 2. Cria outra tarefa (usará criticidade default "Baixa")
    create_task("Revisar interface de usuário", "Ajustar cores e fontes do dashboard.")

    # 3. Lista todas as tarefas
    list_tasks()
    # ... (deixe os outros testes de update/delete comentados para manter a saída limpa)