# ⚡ Início Rápido - LiveKit Agent V3

**5 passos para começar em menos de 5 minutos!**

---

## 📦 Passo 1: Criar Ambiente Virtual

```bash
python -m venv venv
```

---

## 🔑 Passo 2: Ativar Ambiente

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

---

## 📥 Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

⏱️ _Aguarde ~1-2 minutos para instalar tudo_

---

## ⚙️ Passo 4: Configurar API Keys

### 1. Copie o template:
```bash
copy .env.example .env
```

### 2. Edite `.env` com suas chaves:

```ini
# LiveKit (obtenha em: https://cloud.livekit.io/)
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=sua_key_aqui
LIVEKIT_API_SECRET=sua_secret_aqui

# OpenAI (obtenha em: https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-...

# Deepgram (obtenha em: https://console.deepgram.com/)
DEEPGRAM_API_KEY=...
```

**💡 Dica:** Você precisa criar contas nesses serviços:
- [LiveKit Cloud](https://cloud.livekit.io/) (Plano gratuito disponível)
- [OpenAI](https://platform.openai.com/) (Requer cartêo, mas custa centavos)
- [Deepgram](https://console.deepgram.com/) (Plano gratuito disponível)

---

## 🚀 Passo 5: Iniciar Agente

```bash
start.bat
```

Ou:
```bash
python agent.py dev
```

---

## ✅ Verificaçêo

Se tudo deu certo, você verá:

```
========================================
  LiveKit Agent V3
  Agente de Voz em Portugues
========================================

[INFO] Ativando ambiente virtual...
[INFO] Iniciando agente v3...

🚀 Conectando à sala: ...
✅ Agente v3 iniciado com sucesso!
```

---

## 🎤 Testando

1. **Conecte-se ao LiveKit** usando um client (ex: web app, mobile app)
2. **Fale com o agente:**
   - _"Oi!"_
   - _"Que horas sêo?"_
   - _"Como está o tempo em Sêo Paulo?"_

---

## 🐛 Problemas Comuns

### "ModuleNotFoundError"
```bash
# Certifique-se de estar no venv:
venv\Scripts\activate

# Reinstale:
pip install -r requirements.txt
```

### "Invalid API key"
- Verifique se `.env` está configurado corretamente
- Confirme que copiou as chaves completas (sem espaços)

### "Connection refused"
- Verifique se o LiveKit server está rodando
- Se local: use `ws://localhost:7880`
- Se cloud: use o URL fornecido pelo LiveKit Cloud

---

## 📚 Próximos Passos

✅ Agente funcionando? Agora você pode:

1. **Ler o README.md** - Documentaçêo completa
2. **Personalizar o agente** - Edite `agent.py`
3. **Adicionar ferramentas** - Veja exemplos no código
4. **Migrar para V4** - Se precisar de recursos avançados

---

**🎉 Pronto! Seu agente de voz está funcionando!**
