# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas HTTP, validando dados com modelos e retornando respostas apropriadas. Você vai implementar operações CRUD para gerenciar tarefas usando armazenamento em memória.

## 📝 Tasks

### 🛠️ Configure a API and List Tasks

#### Descrição
Instale FastAPI e Uvicorn e complete o código inicial para disponibilizar a rota de listagem de tarefas. A rota de verificação já está no código para ajudar a confirmar que a API está funcionando.

```bash
python -m pip install fastapi uvicorn
```

#### Requisitos
O programa concluído deve:

- Usar a aplicação FastAPI fornecida, com o título `Task API`.
- Executar `GET /health` e confirmar que retorna `{"status": "ok"}`.
- Implementar `GET /tasks`, retornando todas as tarefas armazenadas; inicialmente, a lista pode estar vazia.
- Iniciar a API com `python starter-code.py` e disponibilizar a documentação interativa em `/docs`.

### 🛠️ Retrieve a Task by ID

#### Descrição
Adicione uma rota para consultar uma tarefa específica pelo seu identificador e trate o caso em que ela não existe.

#### Requisitos
O programa concluído deve:

- Implementar `GET /tasks/{task_id}` com um identificador inteiro.
- Retornar a tarefa correspondente quando o identificador existir.
- Retornar o status HTTP `404` quando não houver uma tarefa com esse identificador.

### 🛠️ Create, Update, and Delete Tasks

#### Descrição
Complete as rotas que modificam a coleção de tarefas. Use o modelo de dados fornecido para validar o título, a descrição e o estado de conclusão.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com um identificador único e retornar o status HTTP `201`.
- Implementar `PUT /tasks/{task_id}` para substituir os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente.
- Retornar o status HTTP `404` ao tentar atualizar ou remover uma tarefa inexistente.
- Permitir testar todas as rotas pela documentação interativa em `/docs`.

Exemplo de corpo para criar ou atualizar uma tarefa:

```json
{
  "title": "Read about HTTP methods",
  "description": "Compare GET, POST, PUT, and DELETE",
  "completed": false
}
```
