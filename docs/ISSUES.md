# Issues do Projeto

## [Melhoria] Implementar a biblioteca logging e tratamento de dados vazios

**Descrição:**
Substituir os comandos `print()` do arquivo `main.py` e dos módulos do diretório `pipeline/` por um sistema de logging estruturado utilizando a biblioteca padrão `logging`.

**Objetivos:**
- Criar uma configuração centralizada de logging.
- Substituir todos os `print()` por `logger.info()`, `logger.warning()` ou `logger.error()`.
- Implementar um comportamento controlado (alerta) caso o DataFrame retornado na extração seja nulo ou vazio.

**Critérios de Aceite:**
- O pipeline não deve utilizar `print()`.
- Se os dados estiverem vazios, um log de aviso deve ser emitido e o pipeline deve ser encerrado graciosamente.
- Logs devem seguir um formato padronizado (Data/Hora - Nível - Mensagem).
