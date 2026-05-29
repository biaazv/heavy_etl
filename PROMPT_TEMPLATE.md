# 📝 Modelo de Prompt para o Jules

Use este template para solicitar novas tarefas. Copie e cole o conteúdo abaixo no início da sua conversa com o Jules.

---

```markdown
# 🚀 NOVA TAREFA

# 1. CONTEXTO
Estamos trabalhando no repositório Hevy ETL.
- Leia o arquivo `AGENTS.md` para diretrizes de desenvolvimento.
- Leia o arquivo `STATE.md` para entender o progresso atual.

# 2. OBJETIVO DA ATIVIDADE
[Descreva aqui o que você quer que seja feito em detalhes]
Ex: "Implementar uma validação na transformação que ignore linhas onde a coluna 'weight' é igual a zero."

# 3. ARQUIVOS RELEVANTES
- [Liste os arquivos que o agente deve focar]
Ex: `pipeline/transformation.py` e `tests/test_transformation.py`.

# 4. REGRAS / RESTRIÇÕES
- [Regras específicas para esta tarefa]
Ex: "Não mude os nomes das colunas atuais."

# 5. DEFINIÇÃO DE PRONTO (DoD)
- [ ] Código implementado.
- [ ] Testes rodando e passando.
- [ ] O arquivo `STATE.md` foi atualizado com o progresso.
```
