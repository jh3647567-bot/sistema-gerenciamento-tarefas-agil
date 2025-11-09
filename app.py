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

def create_task(title, description):
    tasks = load_tasks()
    # Garante que o novo ID seja único e sequencial
    new_id = max([t['id'] for t in tasks], default=0) + 1
    new_task = {
        'id': new_id,
        'title': title,
        'description': description,
        'status': 'A Fazer'
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarefa '{title}' criada com sucesso!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for task in tasks:
        print(f"ID: {task['id']} | Título: {task['title']} | Status: {task['status']}")
    print("----------------------")

# Demonstração de uso
if __name__ == "__main__":
    print("--- Sistema Básico de Gerenciamento de Tarefas ---")

    # 1. Cria uma tarefa inicial
    create_task("Configurar ambiente de produção", "Instalar dependências no servidor.")

    # 2. Cria outra tarefa
    create_task("Revisar interface de usuário", "Ajustar cores e fontes do dashboard.")

    # 3. Lista todas as tarefas
    list_tasks() 
