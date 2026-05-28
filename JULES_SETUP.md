# 🤖 Tutorial: Instalando e Configurando o Jules

Se você encontrou o erro `bash: npm: command not found`, isso significa que o **Node.js** (que inclui o `npm`) não está instalado no seu sistema ou não está configurado no seu PATH.

Siga os passos abaixo para resolver o problema e configurar o Jules neste projeto.

---

## 1. Instalando o Node.js e npm

O Jules é uma ferramenta baseada em Node.js. Para utilizá-lo, você precisa primeiro instalar o ambiente Node.js.

### No Windows:
1. Baixe o instalador oficial em [nodejs.org](https://nodejs.org/).
2. Recomendamos a versão **LTS**.
3. Durante a instalação, certifique-se de que a opção "Add to PATH" está marcada.
4. Reinicie seu terminal/PowerShell após a instalação.

### No Linux (Ubuntu/Debian):
Execute os seguintes comandos no terminal:
```bash
sudo apt update
sudo apt install nodejs npm
```

### No macOS:
Se você usa [Homebrew](https://brew.sh/):
```bash
brew install node
```

---

## 2. Instalando o Jules CLI

Com o `npm` funcionando, agora você pode instalar o Jules globalmente:

```bash
npm install -g @google/jules
```

> **Dica:** Se estiver no Linux ou macOS e receber um erro de permissão (EACCES), você pode precisar usar `sudo npm install -g @google/jules` ou configurar um gerenciador de versões como o `nvm`.

---

## 3. Autenticação

Antes de começar a usar, você precisa se conectar à sua conta Google:

```bash
jules login
```
Isso abrirá uma janela no seu navegador para realizar o login.

---

## 4. Usando o Jules no Projeto

Agora que o Jules está instalado, você pode interagir com ele. Por exemplo, para listar sessões remotas:

```bash
jules remote list --session
```

Para obter ajuda geral:
```bash
jules help
```

---

## 🛠 Solução de Problemas Comuns

### "bash: npm: command not found" dentro do (venv)
O fato de você estar em um Ambiente Virtual Python (`venv`) não impede o uso do `npm`, mas o `npm` deve estar instalado no seu sistema operacional "global". O `venv` gerencia apenas pacotes Python. Se você instalou o Node.js recentemente, tente fechar e abrir o terminal novamente para que as alterações no PATH sejam aplicadas.
