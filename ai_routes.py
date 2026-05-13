# Register in app.py: from ai_routes import assistant_bp, then app.register_blueprint(assistant_bp, url_prefix='/api/v1')

import os
import json
from flask import Blueprint, request, jsonify
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

assistant_bp = Blueprint('assistant', __name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

context_path = os.path.join(os.path.dirname(__file__), 'ai_context.txt')
with open(context_path, "r", encoding="utf-8") as f:
    SITE_KNOWLEDGE = f.read()

SYSTEM_PROMPT = f"""Ти — AI-помічник сайту LevelUP. Відповідай виключно на основі контенту сайту.

КОНТЕНТ САЙТУ:
{SITE_KNOWLEDGE}

ПРАВИЛА:
1. Відповідай ТІЛЬКИ на основі контенту сайту
2. Якщо запитання виходить за межі тематики — поясни що ти спеціалізований помічник
3. Якщо інформації недостатньо — скажи звернутись до консультанта за контактами з сайту
4. НЕ вигадуй інформацію якої немає на сайті
5. Пропонуй 2-3 suggested_questions коли це доречно
6. Мова відповіді: українська

Відповідай ТІЛЬКИ у JSON форматі без жодного додаткового тексту:
{{"reply": "...", "suggested_questions": ["...", "..."]}}
Якщо suggested_questions недоречні — повертай []."""

@assistant_bp.route("/assistant", methods=["POST"])
def assistant():
    try:
        data = request.get_json()
        message = data.get("message", "")
        history = data.get("history", [])

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for msg in history[-6:]:
            role = "user" if msg.get("role") == "user" else "assistant"
            messages.append({"role": role, "content": msg.get("content", "")})

        messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
            temperature=0.3,
            response_format={"type": "json_object"}
        )

        raw = response.choices[0].message.content.strip()
        parsed = json.loads(raw)
        return jsonify(parsed)

    except json.JSONDecodeError:
        return jsonify({
            "reply": response.choices[0].message.content,
            "suggested_questions": []
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500