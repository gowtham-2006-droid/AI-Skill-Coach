import os
from typing import Dict, Iterable, List, Optional

import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# Load .env from project root or nearest parent
_env_path = find_dotenv(usecwd=True)
if _env_path:
	load_dotenv(_env_path)
else:
	load_dotenv()


def _configure_api() -> None:
	api_key = os.getenv("GEMINI_API_KEY")
	if not api_key:
		raise RuntimeError("GEMINI_API_KEY is not set. Create a .env file with your key.")
	genai.configure(api_key=api_key)


class GeminiCoach:
	"""Thin wrapper around Gemini for coaching patterns."""

	def __init__(self, model_name: str = "gemini-2.0-flash") -> None:
		_configure_api()
		self.model = genai.GenerativeModel(model_name)

	@staticmethod
	def _system_preamble(mood: str, tone: str) -> str:
		return (
			"You are NeuroSkill Coach 2030, a futuristic, neuroscience-informed mentor. "
			f"User mood: {mood}. Prefer tone: {tone}. "
			"Be empathetic, concise, and specific. Use small emoji tastefully. "
			"When technical, include minimal code snippets."
		)

	def generate_text(self, prompt: str, user_snapshot: Optional[Dict] = None, tone: str = "motivational") -> str:
		mood = user_snapshot.get("mood", "focused") if user_snapshot else "focused"
		preamble = self._system_preamble(mood=mood, tone=tone)
		full = f"{preamble}\n\nUser context: {user_snapshot}\n\nTask: {prompt}"
		resp = self.model.generate_content(full)
		return resp.text or ""

	def stream_chat(
		self,
		messages: List[Dict[str, str]],
		mood: str,
		tone: str,
		user_snapshot: Optional[Dict] = None,
	) -> Iterable[str]:
		preamble = self._system_preamble(mood=mood, tone=tone)

		# Convert messages to a single prompt with role tags for simplicity
		history = []
		for m in messages:
			role = m.get("role", "user")
			content = m.get("content", "")
			history.append(f"[{role}] {content}")
		joined = "\n".join(history)

		full = (
			f"{preamble}\nUser snapshot: {user_snapshot}\n\n"
			"Continue the conversation helpfully and concretely."
			f"\n\n{joined}"
		)
		stream = self.model.generate_content(full, stream=True)
		for event in stream:
			if hasattr(event, "text") and event.text:
				yield event.text

	def generate_simulation(self, topic: str, mode: str = "quiz") -> str:
		prompt = (
			f"Create a {mode} style mini learning simulation for: {topic}. "
			"Keep it to ~6-10 lines, include numbered steps or questions, and an answer key at the end. "
			"Encourage reflection and one concrete next action."
		)
		resp = self.model.generate_content(prompt)
		return resp.text or ""

	def generate_vision(self, snapshot: Dict) -> str:
		prompt = (
			"Imagine the user's skills 6 months from now. Write a vivid, optimistic narrative "
			"of 6-8 sentences with 3 milestones (bulleted) and a rallying call."
		)
		resp = self.model.generate_content(f"User snapshot: {snapshot}\n\n{prompt}")
		return resp.text or ""
