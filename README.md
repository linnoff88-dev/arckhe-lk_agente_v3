# ðŸŽ™ï¸ LiveKit Agent V3 - VersÃ£o Isolada

**VersÃ£o:** 3.0
**Data:** Outubro 2025
**Status:** EstÃ¡vel e Funcional

---

## ðŸ“‹ Sobre

Agente de voz simples em portuguÃªs brasileiro para LiveKit.

### âœ¨ CaracterÃ­sticas:
- âœ… **STT:** Deepgram Nova-2 (portuguÃªs brasileiro)
- âœ… **LLM:** OpenAI GPT-4o-mini
- âœ… **TTS:** OpenAI TTS (voz "alloy")
- âœ… **Idioma:** PortuguÃªs brasileiro natural

### ðŸ› ï¸ Ferramentas DisponÃ­veis:

1. **`get_current_time()`** - Consulta hora e data
   - Exemplo: _"Que horas sÃ£o?"_
   - Exemplo: _"Que dia Ã© hoje?"_

2. **`get_weather(city)`** - Clima simulado
   - Exemplo: _"Como estÃ¡ o tempo em SÃ£o Paulo?"_
   - Exemplo: _"Qual a temperatura no Rio?"_

---

## ðŸš€ InstalaÃ§Ã£o

### 1. **Requisitos:**
- Python 3.10+
- Conta LiveKit
- API Keys: OpenAI, Deepgram

### 2. **Criar ambiente virtual:**
```bash
python -m venv venv
```

### 3. **Ativar ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. **Instalar dependÃªncias:**
```bash
pip install -r requirements.txt
```

### 5. **Configurar variÃ¡veis de ambiente:**

Copie `.env.example` para `.env`:
```bash
copy .env.example .env
```

Edite `.env` com suas chaves:
```ini
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=sua_key
LIVEKIT_API_SECRET=sua_secret
OPENAI_API_KEY=sk-...
DEEPGRAM_API_KEY=...
```

---

## ðŸŽ¬ Como Usar

### **OpÃ§Ã£o 1: Script de inicializaÃ§Ã£o (Windows)**
```bash
start.bat
```

### **OpÃ§Ã£o 2: Comando direto**
```bash
python agent.py dev
```

### **OpÃ§Ã£o 3: Em produÃ§Ã£o**
```bash
python agent.py start
```

---

## ðŸ’¬ Exemplos de Uso

ApÃ³s iniciar o agente, conecte-se via LiveKit client e teste:

### Consultar Hora:
```
ðŸ‘¤ "Que horas sÃ£o?"
ðŸ¤– "Agora sÃ£o 14:35. Hoje Ã© sexta-feira, 12 de outubro de 2025."

ðŸ‘¤ "Que horas sÃ£o em Nova York?"
ðŸ¤– "Em Nova York, agora sÃ£o 07:35. Hoje Ã© sexta-feira, 12 de outubro de 2025."
```

### Consultar Clima:
```
ðŸ‘¤ "Como estÃ¡ o tempo em SÃ£o Paulo?"
ðŸ¤– "â˜€ï¸ PrevisÃ£o para SÃ£o Paulo:
     â€¢ CondiÃ§Ã£o: ensolarado
     â€¢ Temperatura: 28Â°C (sensaÃ§Ã£o de 30Â°C)
     â€¢ Umidade: 65%
     â€¢ Vento: 15 km/h"

ðŸ‘¤ "Qual a temperatura no Rio?"
ðŸ¤– "ðŸŒ§ï¸ PrevisÃ£o para Rio de Janeiro:
     â€¢ CondiÃ§Ã£o: chuvoso
     â€¢ Temperatura: 22Â°C (sensaÃ§Ã£o de 20Â°C)
     â€¢ Umidade: 85%
     â€¢ Vento: 20 km/h"
```

### ConversaÃ§Ã£o Geral:
```
ðŸ‘¤ "Oi, tudo bem?"
ðŸ¤– "OlÃ¡! Tudo Ã³timo, obrigado! Como posso te ajudar hoje?"

ðŸ‘¤ "Me conte uma piada"
ðŸ¤– "Por que o livro de matemÃ¡tica se suicidou? Porque tinha muitos problemas!"
```

---

## ðŸ“ Estrutura de Arquivos

```
lk_agente_v3/
â”œâ”€â”€ agent.py            # CÃ³digo principal do agente
â”œâ”€â”€ requirements.txt    # DependÃªncias Python
â”œâ”€â”€ .env.example       # Template de configuraÃ§Ã£o
â”œâ”€â”€ .env               # ConfiguraÃ§Ã£o (nÃ£o versionado)
â”œâ”€â”€ start.bat          # Script de inicializaÃ§Ã£o (Windows)
â”œâ”€â”€ README.md          # Esta documentaÃ§Ã£o
â””â”€â”€ venv/              # Ambiente virtual (criado apÃ³s instalaÃ§Ã£o)
```

---

## ðŸ”§ ConfiguraÃ§Ã£o AvanÃ§ada

### Mudar Voz do TTS:

Edite `agent.py` na linha 127:
```python
tts=openai.TTS(
    voice="alloy"  # OpÃ§Ãµes: alloy, echo, fable, onyx, nova, shimmer
)
```

**Vozes disponÃ­veis:**
- `alloy` - Voz neutra (padrÃ£o)
- `echo` - Voz masculina
- `fable` - Voz britÃ¢nica
- `onyx` - Voz profunda
- `nova` - Voz feminina
- `shimmer` - Voz suave

### Mudar Modelo LLM:

Edite `agent.py` na linha 124:
```python
llm=openai.LLM(model="gpt-4o-mini")  # Pode usar: gpt-4, gpt-3.5-turbo, etc
```

### Desabilitar Logging:

Edite `agent.py` na linha 24:
```python
logging.basicConfig(level=logging.WARNING)  # Menos verboso
```

---

## ðŸ› Troubleshooting

### Problema: "ModuleNotFoundError: No module named 'livekit'"

**SoluÃ§Ã£o:**
```bash
# Certifique-se de estar no ambiente virtual
venv\Scripts\activate

# Reinstale as dependÃªncias
pip install -r requirements.txt
```

### Problema: "Invalid API key"

**SoluÃ§Ã£o:**
- Verifique se `.env` existe e estÃ¡ configurado corretamente
- Confirme que as chaves API estÃ£o vÃ¡lidas
- Certifique-se de nÃ£o ter espaÃ§os extras no `.env`

### Problema: Agente nÃ£o responde em portuguÃªs

**SoluÃ§Ã£o:**
- Verifique se o STT estÃ¡ configurado como `pt-BR` (linha 118-120)
- Confirme que as instruÃ§Ãµes do agente estÃ£o em portuguÃªs (linha 33-45)

### Problema: "Connection refused"

**SoluÃ§Ã£o:**
- Certifique-se de que o LiveKit server estÃ¡ rodando
- Verifique o `LIVEKIT_URL` no `.env`
- Se local, use: `ws://localhost:7880`

---

## ðŸ“Š EspecificaÃ§Ãµes TÃ©cnicas

### Performance:
- **LatÃªncia mÃ©dia:** ~500-800ms
- **Uso de memÃ³ria:** ~200-300MB
- **CPU:** Baixo (maior uso no STT/TTS)

### Limites:
- **HistÃ³rico de conversaÃ§Ã£o:** Gerenciado pelo LiveKit
- **DuraÃ§Ã£o mÃ¡xima de Ã¡udio:** Sem limite (streaming)
- **ConexÃµes simultÃ¢neas:** Depende do plano LiveKit

### Modelos Usados:
- **STT:** Deepgram Nova-2 (pt-BR)
- **LLM:** OpenAI GPT-4o-mini
- **TTS:** OpenAI TTS

---

## ðŸ”’ SeguranÃ§a

### Boas PrÃ¡ticas:

1. **NUNCA** commite `.env` para git
2. **SEMPRE** use `.env.example` como template
3. **ROTACIONE** suas API keys regularmente
4. **MONITORE** uso de API para evitar custos inesperados

### Arquivo `.gitignore`:
```
.env
venv/
__pycache__/
*.pyc
*.log
```

---

## ðŸ“ˆ DiferenÃ§as entre VersÃµes

### V3 vs V4:
| Recurso | V3 | V4 |
|---------|----|----|
| STT PortuguÃªs | âœ… | âœ… |
| TTS OpenAI | âœ… | âœ… |
| Hora/Data | âœ… | âœ… |
| Clima | âœ… Simulado | âœ… Simulado |
| Google Calendar | âŒ | âœ… |
| Busca Web | âŒ | âœ… |
| Tarefas | âŒ | âœ… |
| Email | âŒ | âœ… Simulado |
| Router Cognitivo | âŒ | âœ… |
| Contexto | âŒ | âœ… |

**V3 Ã© ideal se vocÃª quer:**
- âœ… SoluÃ§Ã£o simples e rÃ¡pida
- âœ… Menos dependÃªncias
- âœ… FÃ¡cil de entender e modificar
- âœ… Apenas conversaÃ§Ã£o + hora/clima

**V4 Ã© ideal se vocÃª precisa:**
- âœ… IntegraÃ§Ã£o com Google Calendar
- âœ… Busca web em tempo real
- âœ… Gerenciamento de tarefas
- âœ… Arquitetura modular avanÃ§ada

---

## ðŸ†˜ Suporte

### DocumentaÃ§Ã£o Oficial:
- [LiveKit Docs](https://docs.livekit.io/)
- [LiveKit Agents](https://docs.livekit.io/agents/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Deepgram API](https://developers.deepgram.com/)

### Issues Comuns:
- [LiveKit Community](https://github.com/livekit/livekit/discussions)
- [OpenAI Community](https://community.openai.com/)

---

## ðŸ“ Changelog

### V3.0 (Outubro 2025)
- âœ… VersÃ£o isolada criada
- âœ… STT em portuguÃªs (Deepgram)
- âœ… TTS OpenAI com voz natural
- âœ… Ferramentas: hora/data, clima
- âœ… InstruÃ§Ãµes otimizadas em portuguÃªs
- âœ… DocumentaÃ§Ã£o completa

---

## ðŸ“œ LicenÃ§a

Este Ã© um projeto educacional. Use por sua conta e risco.

**Custos de API:**
- OpenAI: ~$0.002 por minuto de conversaÃ§Ã£o
- Deepgram: ~$0.0043 por minuto de Ã¡udio
- LiveKit: Plano gratuito disponÃ­vel

---

## ðŸŽ¯ PrÃ³ximos Passos

Depois de testar o V3, vocÃª pode:

1. **Adicionar ferramentas customizadas** no `agent.py`
2. **Integrar APIs reais** (clima, notÃ­cias, etc.)
3. **Personalizar instruÃ§Ãµes** para seu caso de uso
4. **Migrar para V4** se precisar de recursos avanÃ§ados

---

**ðŸŽ‰ Divirta-se com seu agente de voz em portuguÃªs!**

Para dÃºvidas ou sugestÃµes, consulte a documentaÃ§Ã£o do LiveKit.

---

Projeto adaptado da comunidade INEMA TDS - Marca Arckhe