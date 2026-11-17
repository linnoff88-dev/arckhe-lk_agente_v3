# 📂 LiveKit Agent V3 - Índice de Arquivos

**Estrutura completa do projeto isolado**

---

## 📄 Arquivos Principais

### `agent.py` ⭐
- **O que é:** Código principal do agente de voz
- **Função:** Define o agente, ferramentas e comportamento
- **Editar?** Sim - para customizar o agente
- **Tamanho:** ~150 linhas
- **Linguagem:** Python 3.10+

**Contém:**
- Classe `Assistant` (agente principal)
- Ferramentas: `get_current_time()`, `get_weather()`
- Configuração de STT/LLM/TTS
- Ponto de entrada `entrypoint()`

---

### `requirements.txt`
- **O que é:** Lista de dependências Python
- **Função:** Define pacotes necessários
- **Editar?** Raramente - apenas se adicionar novas bibliotecas
- **Tamanho:** ~15 linhas

**Dependências:**
- `livekit` - Core do LiveKit
- `livekit-agents[openai,deepgram]` - Plugins
- `openai` - LLM e TTS
- `deepgram-sdk` - STT em português
- `python-dotenv` - Carrega `.env`

---

### `start.bat` (Windows)
- **O que é:** Script de inicialização
- **Função:** Ativa venv e inicia o agente
- **Editar?** Não necessário
- **Alternativa Linux/Mac:** Use `python agent.py dev` diretamente

---

### `.env` (você cria)
- **O que é:** Arquivo de configuração com API keys
- **Função:** Armazena credenciais sensíveis
- **Editar?** Sim - OBRIGATÓRIO para funcionar
- **⚠️ IMPORTANTE:** NUNCA commite para git!

**Conteúdo necessário:**
```ini
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
OPENAI_API_KEY=sk-...
DEEPGRAM_API_KEY=...
```

---

### `.env.example`
- **O que é:** Template do `.env`
- **Função:** Mostra quais variáveis são necessárias
- **Editar?** Não - copie para `.env` e edite lá

---

### `.gitignore`
- **O que é:** Lista de arquivos ignorados pelo Git
- **Função:** Protege `.env` e `venv/` de serem commitados
- **Editar?** Raramente

---

## 📖 Documentação

### `README.md` ⭐⭐⭐
- **O que é:** Documentação completa do projeto
- **Conteúdo:**
  - Instalação detalhada
  - Configuração
  - Exemplos de uso
  - Troubleshooting
  - Especificações técnicas
  - Comparação V3 vs V4
- **Leia:** Primeira coisa a fazer!

---

### `INICIO_RAPIDO.md` ⭐
- **O que é:** Guia de 5 passos para começar
- **Conteúdo:**
  - Setup rápido (< 5 minutos)
  - Comandos essenciais
  - Verificação
  - Problemas comuns
- **Leia:** Se quer começar rapidamente

---

### `INDEX.md` (este arquivo)
- **O que é:** Índice de todos os arquivos
- **Conteúdo:** Descrição de cada arquivo do projeto
- **Leia:** Para entender a estrutura

---

## 📁 Diretórios

### `venv/` (criado após instalação)
- **O que é:** Ambiente virtual Python
- **Função:** Isola dependências do projeto
- **Tamanho:** ~200-300 MB
- **Git:** Ignorado (não versionar)
- **Como criar:** `python -m venv venv`
- **Como ativar:** `venv\Scripts\activate` (Windows)

---

## 🔒 Arquivos Sensíveis

### ⚠️ NUNCA COMMITE:
- `.env` - Contém API keys
- `venv/` - Ambiente virtual (grande e desnecessário)

### ✅ SEMPRE VERSIONE:
- `agent.py` - Código do agente
- `requirements.txt` - Dependências
- `.env.example` - Template
- `.gitignore` - Proteção
- Documentação (README, etc.)

---

## 🎯 Fluxo de Trabalho

### Primeira Vez:
1. Ler `INICIO_RAPIDO.md`
2. Criar `venv`
3. Instalar dependências
4. Copiar `.env.example` → `.env`
5. Configurar API keys
6. Executar `start.bat`

### Dia a Dia:
1. Ativar `venv`
2. Executar `python agent.py dev`
3. Conectar client e testar

### Customização:
1. Editar `agent.py`
2. Testar mudanças
3. Commitar (sem `.env` e `venv/`)

---

## 📊 Tamanho dos Arquivos

```
agent.py              ~15 KB
requirements.txt      ~500 bytes
.env.example          ~500 bytes
.gitignore           ~300 bytes
start.bat            ~800 bytes
README.md            ~20 KB
INICIO_RAPIDO.md     ~5 KB
INDEX.md             ~5 KB (este arquivo)

venv/                ~200-300 MB (após instalação)
.env                 ~500 bytes (você cria)
```

**Total (sem venv):** ~50 KB
**Total (com venv):** ~300 MB

---

## 🔧 Arquivos para Editar

### Você DEVE editar:
- ✅ `.env` - Obrigatório para funcionar

### Você PODE editar:
- ✅ `agent.py` - Para customizar o agente
- ✅ `README.md` - Para documentar suas mudanças
- ✅ `start.bat` - Para ajustar o script de inicialização

### Você NÃO DEVE editar:
- ❌ `venv/` - Gerado automaticamente
- ❌ `.env.example` - Template padrão
- ❌ `.gitignore` - A menos que saiba o que está fazendo

---

## 📦 Dependências Externas

### Serviços Necessários:
1. **LiveKit** - Servidor de mídia
   - URL: https://cloud.livekit.io/
   - Plano gratuito: Sim

2. **OpenAI** - LLM e TTS
   - URL: https://platform.openai.com/
   - Plano gratuito: Créditos iniciais

3. **Deepgram** - STT em português
   - URL: https://console.deepgram.com/
   - Plano gratuito: Sim

---

## 🎓 Ordem de Leitura Recomendada

1. **INICIO_RAPIDO.md** - Para começar rápido (5 min)
2. **README.md** - Para entender tudo (20 min)
3. **INDEX.md** - Para referência (5 min)
4. **agent.py** - Para customizar (quando necessário)

---

## ❓ FAQ Rápido

**Q: Qual arquivo devo rodar?**
A: `start.bat` (Windows) ou `python agent.py dev` (qualquer OS)

**Q: Onde coloco minhas API keys?**
A: No arquivo `.env` (copie de `.env.example`)

**Q: Como customizo o agente?**
A: Edite `agent.py`

**Q: Preciso do V4?**
A: Não, se apenas quer conversação simples. V3 é independente.

**Q: Posso deletar a documentação?**
A: Sim, mas não recomendado. Mantenha pelo menos o README.md

---

## 🚀 Próximos Passos

Agora que você conhece a estrutura:

1. ✅ **Instalação** - Siga o INICIO_RAPIDO.md
2. ✅ **Teste** - Execute e converse com o agente
3. ✅ **Customize** - Edite agent.py para suas necessidades
4. ✅ **Explore** - Leia o README.md completo
5. ✅ **Compartilhe** - Versione seu código (sem .env!)

---

**📚 Documentação Completa:**
- `README.md` - Tudo sobre o projeto
- `INICIO_RAPIDO.md` - Setup em 5 passos
- `INDEX.md` - Este arquivo

**🎯 Arquivos Essenciais:**
- `agent.py` - Código principal
- `requirements.txt` - Dependências
- `.env` - Configuração (você cria)

**🛠️ Utilities:**
- `start.bat` - Script de inicialização
- `.gitignore` - Proteção

---

**🎉 Agora você conhece todos os arquivos do projeto!**
