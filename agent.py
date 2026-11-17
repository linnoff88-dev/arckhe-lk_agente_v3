"""
Agente de Voz LiveKit - API v1.0 - VERSÃO 3
============================================
Melhorias:
- STT em português (pt-BR)
- TTS com OpenAI (voz mais natural)
- Instruções otimizadas
- Ferramentas aprimoradas
"""

import logging
import random
from datetime import datetime
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import Agent, AgentSession, RunContext
from livekit.agents.llm import function_tool
from livekit.plugins import openai, deepgram

# Carrega variáveis de ambiente
load_dotenv()

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Assistant(Agent):
    """Assistente de voz em português com ferramentas aprimoradas."""

    def __init__(self):
        super().__init__(
            instructions="""Você é um assistente de voz brasileiro chamado LiveKit Assistant.

Características:
- Fale SEMPRE em português brasileiro natural
- Seja simpático, educado e prestativo
- Use linguagem coloquial mas profissional
- Respostas curtas e diretas (máximo 2-3 frases)
- Quando usar ferramentas, explique o que está fazendo

Suas capacidades:
- Informar hora e data atual (qualquer localização)
- Consultar previsão do tempo (simulado)
- Conversar naturalmente sobre diversos assuntos"""
        )

    @function_tool
    async def get_current_time(self, context: RunContext, location: str = None) -> str:
        """Obtém a hora e data atual.

        Args:
            location: Localização opcional (ex: "São Paulo", "Nova York")
        """
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%d de %B de %Y")
        day_of_week = datetime.now().strftime("%A")

        # Tradução simples dos dias da semana
        days_pt = {
            "Monday": "segunda-feira",
            "Tuesday": "terça-feira",
            "Wednesday": "quarta-feira",
            "Thursday": "quinta-feira",
            "Friday": "sexta-feira",
            "Saturday": "sábado",
            "Sunday": "domingo"
        }
        day_pt = days_pt.get(day_of_week, day_of_week)

        if location:
            return f"Em {location}, agora são {current_time}. Hoje é {day_pt}, {current_date}."

        return f"Agora são {current_time}. Hoje é {day_pt}, {current_date}."

    @function_tool
    async def get_weather(self, context: RunContext, city: str) -> str:
        """Consulta a previsão do tempo para uma cidade.

        Args:
            city: Nome da cidade (ex: "São Paulo", "Rio de Janeiro")
        """
        # Simulação realista de dados de clima
        weather_conditions = {
            "ensolarado": "☀️",
            "parcialmente nublado": "⛅",
            "nublado": "☁️",
            "chuvoso": "🌧️",
            "tempestuoso": "⛈️"
        }

        condition_name = random.choice(list(weather_conditions.keys()))
        condition_emoji = weather_conditions[condition_name]
        temperature = random.randint(18, 35)
        humidity = random.randint(40, 85)
        wind = random.randint(5, 25)

        # Sensação térmica baseada na temperatura
        feels_like = temperature + random.randint(-3, 3)

        result = f"{condition_emoji} Previsão para {city}:\n"
        result += f"• Condição: {condition_name}\n"
        result += f"• Temperatura: {temperature}°C (sensação de {feels_like}°C)\n"
        result += f"• Umidade: {humidity}%\n"
        result += f"• Vento: {wind} km/h"

        return result


async def entrypoint(ctx: agents.JobContext):
    """Ponto de entrada do agente."""

    logger.info(f"🚀 Conectando à sala: {ctx.room.name}")

    # Configura a sessão do agente com componentes em português
    session = AgentSession(
        # STT em português brasileiro
        stt=deepgram.STT(
            model="nova-2",
            language="pt-BR"  # ← PORTUGUÊS!
        ),

        # LLM OpenAI
        llm=openai.LLM(model="gpt-4o-mini"),

        # TTS OpenAI (vozes mais naturais que Cartesia)
        tts=openai.TTS(
            voice="alloy"  # Opções: alloy, echo, fable, onyx, nova, shimmer
        ),
    )

    # Inicia a sessão com o agente
    await session.start(
        room=ctx.room,
        agent=Assistant()
    )

    logger.info("✅ Agente v3 iniciado com sucesso!")

    # Saudação inicial em português
    await session.generate_reply(
        instructions="""Cumprimente o usuário de forma calorosa e natural em português brasileiro.
        Diga seu nome (LiveKit Assistant) e pergunte como pode ajudar.
        Seja breve e amigável."""
    )


if __name__ == "__main__":
    # Executa o agente
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
