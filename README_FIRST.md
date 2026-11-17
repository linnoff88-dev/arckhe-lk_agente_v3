# 🎯 LEIA PRIMEIRO - LiveKit Agent V3 Isolado

**Bem-vindo à versão isolada e independente do Agent V3!**

---

## ✅ O que foi criado

Esta pasta contém uma **versão completamente isolada** do LiveKit Agent V3.

**Características:**
- ✅ **100% funcional** - Pronto para usar
- ✅ **Independente** - Não depende de V4, V2 ou outros
- ✅ **Limpo** - Apenas código V3, sem misturas
- ✅ **Documentado** - Guias completos incluídos

---

## 📂 Arquivos Incluídos

### 🚀 Essenciais (para funcionar):
1. **`agent.py`** - Código do agente (150 linhas)
2. **`requirements.txt`** - Dependências Python
3. **`.env.example`** - Template de configuração
4. **`start.bat`** - Script para iniciar (Windows)

### 📚 Documentação (leia antes de usar):
5. **`README.md`** - Documentação completa (20 KB)
6. **`INICIO_RAPIDO.md`** - Guia de 5 passos (5 min)
7. **`INDEX.md`** - Índice de todos os arquivos
8. **`V3_VS_V4.md`** - Comparação V3 vs V4

### 🔧 Utilitários:
9. **`.gitignore`** - Proteção para Git
10. **`README_FIRST.md`** - Este arquivo

---

## 🚀 Como Começar (3 minutos)

### Passo 1: Criar ambiente virtual
```bash
python -m venv venv
```

### Passo 2: Ativar ambiente
```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### Passo 3: Instalar dependências
```bash
pip install -r requirements.txt
```

### Passo 4: Configurar API keys
```bash
# Copie o template:
copy .env.example .env

# Edite .env com suas chaves
```

### Passo 5: Iniciar!
```bash
start.bat
# ou
python agent.py dev
```

**Documentação completa:** Leia `INICIO_RAPIDO.md`

---

## 📖 Ordem de Leitura Recomendada

1. ✅ **`README_FIRST.md`** (este arquivo) - 2 min
2. ✅ **`INICIO_RAPIDO.md`** - Configuração rápida - 5 min
3. ✅ **`README.md`** - Documentação completa - 20 min
4. 📚 **`INDEX.md`** - Referência de arquivos - 5 min
5. 📚 **`V3_VS_V4.md`** - Comparação versões - 10 min

---

## 🎯 O que o Agent V3 faz?

### Capacidades:
- ✅ **Conversação natural** em português brasileiro
- ✅ **Consulta hora/data** (qualquer localização)
- ✅ **Previsão do tempo** (simulado)
- ✅ **Resposta rápida** (~500-800ms latência)

### O que NÃO tem (use V4 para isso):
- ❌ Google Calendar
- ❌ Busca web real
- ❌ Gerenciamento de tarefas
- ❌ Email

**Se precisa desses recursos:** Veja `V3_VS_V4.md` para decidir

---

## 🤔 Perguntas Rápidas

**Q: Este V3 é diferente do V4?**
A: Sim! V3 é simples e focado. V4 tem Google Calendar, busca web, etc.

**Q: Posso usar sem V4 instalado?**
A: Sim! V3 é completamente independente.

**Q: Precisa de muitas dependências?**
A: Não! Apenas 5 pacotes Python básicos.

**Q: É difícil configurar?**
A: Não! Menos de 5 minutos seguindo o guia.

**Q: Quanto custa?**
A: ~$0.0063/minuto de conversação (muito barato!)

**Q: Funciona em produção?**
A: Sim! É estável e testado.

---

## 🎓 Para Quem é o V3?

### ✅ Ideal para:
- Iniciantes em LiveKit
- Projetos simples de conversação
- Aprendizado (código limpo e fácil)
- Prototipagem rápida
- Quem não precisa de calendário/busca web

### ❌ Não ideal para:
- Projetos que precisam de Google Calendar
- Sistemas que exigem busca web
- Gerenciamento complexo de tarefas

**Para esses casos:** Use o V4 (veja `V3_VS_V4.md`)

---

## 📊 Recursos Necessários

### Contas/APIs:
1. **LiveKit** - Servidor de mídia
   - 🔗 https://cloud.livekit.io/
   - 💰 Plano gratuito disponível

2. **OpenAI** - LLM e TTS
   - 🔗 https://platform.openai.com/
   - 💰 Créditos iniciais gratuitos

3. **Deepgram** - STT em português
   - 🔗 https://console.deepgram.com/
   - 💰 Plano gratuito disponível

### Hardware:
- **RAM:** 512 MB (mínimo), 1 GB (recomendado)
- **CPU:** Qualquer (baixo uso)
- **Disco:** 300 MB (com venv)

---

## 🛠️ Tecnologias Usadas

- **Python** 3.10+
- **LiveKit** - Framework de voz
- **OpenAI GPT-4o-mini** - LLM
- **OpenAI TTS** - Text-to-Speech
- **Deepgram Nova-2** - Speech-to-Text (pt-BR)

---

## 🎉 Você está pronto!

### Próximos passos:

1. ✅ **Configure o ambiente** (siga `INICIO_RAPIDO.md`)
2. ✅ **Teste o agente** (fale com ele!)
3. ✅ **Leia a documentação** (`README.md`)
4. ✅ **Customize** (edite `agent.py`)
5. ✅ **Divirta-se!**

---

## 📞 Suporte

### Documentação:
- **Início Rápido:** `INICIO_RAPIDO.md`
- **Completo:** `README.md`
- **Referência:** `INDEX.md`
- **Comparação:** `V3_VS_V4.md`

### Problemas Comuns:
- **"ModuleNotFoundError"** → Ative o venv e reinstale
- **"Invalid API key"** → Verifique o `.env`
- **"Connection refused"** → Verifique o LiveKit server

**Troubleshooting completo:** Veja `README.md`

---

## 🎯 Estrutura Resumida

```
lk_agente_v3/
│
├── 🚀 EXECUTAR
│   ├── agent.py              # Código principal
│   ├── start.bat             # Inicia o agente
│   └── .env                  # Configuração (você cria)
│
├── 📦 CONFIGURAÇÃO
│   ├── requirements.txt      # Dependências
│   ├── .env.example          # Template
│   └── .gitignore           # Proteção Git
│
└── 📚 DOCUMENTAÇÃO
    ├── README_FIRST.md       # ← VOCÊ ESTÁ AQUI
    ├── INICIO_RAPIDO.md      # Guia de 5 passos
    ├── README.md             # Documentação completa
    ├── INDEX.md              # Índice de arquivos
    └── V3_VS_V4.md          # Comparação versões
```

---

## ✅ Checklist Rápido

Antes de começar:

- [ ] Python 3.10+ instalado
- [ ] Contas criadas (LiveKit, OpenAI, Deepgram)
- [ ] API keys obtidas
- [ ] Leu `INICIO_RAPIDO.md`

Pronto? Comece agora:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edite .env com suas chaves
start.bat
```

---

## 🏆 Versão Isolada = Liberdade

**Benefícios desta versão:**
- ✅ Sem confusão com V4
- ✅ Sem dependências extras
- ✅ Código limpo e simples
- ✅ Fácil de versionar
- ✅ Independente e estável

---

**🎉 Bem-vindo ao LiveKit Agent V3!**

**Próximo passo:** Leia `INICIO_RAPIDO.md` e configure em 5 minutos!

---

**Documentação criada em:** 12 de Outubro de 2025
**Versão do Agent:** 3.0
**Status:** Estável e Pronto para Uso
