<div align="right">
<a href="./README.md">Read in English</a>
</div>

# VaVargas PyBackup - Gerenciador Simples de Backup

Uma aplicação de desktop simples construída com Python e Tkinter para gerenciar e executar tarefas de backup/sincronização de arquivos.

![VaVar PyBackup](https://raw.githubusercontent.com/vavargasdev/va_pybackup/refs/heads/main/VaVarBackupScreen.jpg)

## Funcionalidades

-   **Grupos de Configuração**: Salve e carregue diferentes configurações de backup (ex: "Trabalho Diário", "Backup Completo do Drive").
-   **Sincronização Flexível**: Escolha diretórios de origem e destino.
-   **Regras de Exclusão**: Especifique diretórios e arquivos a serem ignorados durante o backup (ex: `node_modules`, arquivos `.tmp`).
-   **Controle de Atualização**: Opção para atualizar apenas arquivos que são mais recentes no diretório de origem.
-   **Interface Simples**: Interface gráfica fácil de usar, construída com Tkinter.

## Tecnologias Utilizadas

-   Python 3
-   Tkinter (para a GUI)

## Como Usar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/vavargasdev/va_pybackup.git
    cd va_backup
    ```

2.  **Execute a aplicação:**
    ```bash
    python main.py
    ```

3.  **Configuração:**
    -   A aplicação usa um arquivo `backup_config.json` para armazenar os grupos de backup.
    -   Preencha os campos na interface para criar um novo grupo de configuração.
    -   Digite um nome para o grupo e clique em "Salvar Configuração".
    -   Para executar um backup, selecione um grupo no menu suspenso e clique em "Iniciar Backup".

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para mais detalhes.