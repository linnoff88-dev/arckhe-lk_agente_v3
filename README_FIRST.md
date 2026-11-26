# 🎯 LEIA PRIMEIRO - LiveKit Agent V3 Isolado

**Bem-vindo à versêo isolada e independente do Agent V3!**

---

## ✅ O que foi criado

Esta pasta contém uma **versêo completamente isolada** do LiveKit Agent V3.

**Características:**
- ✅ **100% funcional** - Pronto para usar
- ✅ **Independente** - Nêo depende de V4, V2 ou outros
- ✅ **Limpo** - Apenas código V3, sem misturas
- ✅ **Documentado** - Guias completos incluídos

---

## 📂 Arquivos Incluídos

### 🚀 Essenciais (para funcionar):
1. **`agent.py`** - Código do agente (150 linhas)
2. **`requirements.txt`** - Dependências Python
3. **`.env.example`** - Template de configuraçêo
4. **`start.bat`** - Script para iniciar (Windows)

### 📚 Documentaçêo (leia antes de usar):
5. **`README.md`** - Documentaçêo completa (20 KB)
6. **`INICIO_RAPIDO.md`** - Guia de 5 passos (5 min)
7. **`INDEX.md`** - Índice de todos os arquivos
8. **`V3_VS_V4.md`** - Comparaçêo V3 vs V4

### 🔧 Utilitários:
9. **`.gitignore`** - Proteçêo para Git
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

**Documentaçêo completa:** Leia `INICIO_RAPIDO.md`

---

## 📖 Ordem de Leitura Recomendada

1. ✅ **`README_FIRST.md`** (este arquivo) - 2 min
2. ✅ **`INICIO_RAPIDO.md`** - Configuraçêo rápida - 5 min
3. ✅ **`README.md`** - Documentaçêo completa - 20 min
4. 📚 **`INDEX.md`** - Referência de arquivos - 5 min
5. 📚 **`V3_VS_V4.md`** - Comparaçêo versões - 10 min

---

## 🎯 O que o Agent V3 faz?

### Capacidades:
- ✅ **Conversaçêo natural** em português brasileiro
- ✅ **Consulta hora/data** (qualquer localizaçêo)
- ✅ **Previsêo do tempo** (simulado)
- ✅ **Resposta rápida** (~500-800ms latência)

### O que NêO tem (use V4 para isso):
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
A: Nêo! Apenas 5 pacotes Python básicos.

**Q: É difícil configurar?**
A: Nêo! Menos de 5 minutos seguindo o guia.

**Q: Quanto custa?**
A: ~$0.0063/minuto de conversaçêo (muito barato!)

**Q: Funciona em produçêo?**
A: Sim! É estável e testado.

---

## 🎓 Para Quem é o V3?

### ✅ Ideal para:
- Iniciantes em LiveKit
- Projetos simples de conversaçêo
- Aprendizado (código limpo e fácil)
- Prototipagem rápida
- Quem nêo precisa de calendário/busca web

### ❌ Nêo ideal para:
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
3. ✅ **Leia a documentaçêo** (`README.md`)
4. ✅ **Customize** (edite `agent.py`)
5. ✅ **Divirta-se!**

---

## 📞 Suporte

### Documentaçêo:
- **Início Rápido:** `INICIO_RAPIDO.md`
- **Completo:** `README.md`
- **Referência:** `INDEX.md`
- **Comparaçêo:** `V3_VS_V4.md`

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
│   └── .env                  # Configuraçêo (você cria)
│
├── 📦 CONFIGURAÇêO
│   ├── requirements.txt      # Dependências
│   ├── .env.example          # Template
│   └── .gitignore           # Proteçêo Git
│
└── 📚 DOCUMENTAÇêO
    ├── README_FIRST.md       # ← VOCÊ ESTÁ AQUI
    ├── INICIO_RAPIDO.md      # Guia de 5 passos
    ├── README.md             # Documentaçêo completa
    ├── INDEX.md              # Índice de arquivos
    └── V3_VS_V4.md          # Comparaçêo versões
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

## 🏆 Versêo Isolada = Liberdade

**Benefícios desta versêo:**
- ✅ Sem confusêo com V4
- ✅ Sem dependências extras
- ✅ Código limpo e simples
- ✅ Fácil de versionar
- ✅ Independente e estável

---

**🎉 Bem-vindo ao LiveKit Agent V3!**

**Próximo passo:** Leia `INICIO_RAPIDO.md` e configure em 5 minutos!

---

**Documentaçêo criada em:** 12 de Outubro de 2025
**Versêo do Agent:** 3.0
**Status:** Estável e Pronto para Uso
