import os
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv, find_dotenv

# Load environment variables first, before any other imports
_env_path = find_dotenv(usecwd=True)
if _env_path:
    load_dotenv(_env_path)
    print(f"Loaded .env from: {_env_path}")
else:
    load_dotenv()
    print("Loaded .env from default location")

# Debug: Check if API key is loaded
api_key = os.getenv("GEMINI_API_KEY")
print(f"API Key loaded: {bool(api_key)}")
if api_key:
    print(f"API Key starts with: {api_key[:10]}...")

from lib.data_store import UserDataStore
from lib.gemini_client import GeminiCoach
from lib.styles import inject_global_styles, ring_svg

APP_TITLE = "NeuroSkill Coach 2030"
DATA_PATH = Path("data/user_data.json")


def init_state():
	if "messages" not in st.session_state:
		st.session_state.messages = []
	if "mood" not in st.session_state:
		st.session_state.mood = "focused"
	if "tone" not in st.session_state:
		st.session_state.tone = "motivational"


def ai_summary(coach: GeminiCoach, user_snapshot: dict) -> str:
	prompt = (
		"You are a futuristic, neuroscience-informed AI mentor. Summarize the user's current "
		"learning momentum in 2-3 energetic sentences with one concrete suggestion. "
		"Reference skills with emojis and keep it warm and empowering."
	)
	return coach.generate_text(prompt, user_snapshot=user_snapshot, tone="motivational")


def sidebar_controls(store: UserDataStore):
	st.sidebar.header("Mentor Controls")
	st.sidebar.selectbox(
		"Mood", ["focused", "tired", "motivated", "stressed", "curious"],
		key="mood",
	)
	st.sidebar.selectbox(
		"Tone", ["motivational", "technical", "reflective"],
		key="tone",
	)

	with st.sidebar.expander("Add/Update Skill"):
		skill_name = st.text_input("Skill name", key="skill_input")
		col1, col2 = st.columns(2)
		with col1:
			level = st.number_input("Level", 0, 100, 0, 1, key="lvl_input")
		with col2:
			energy = st.number_input("Energy", 0, 100, 0, 1, key="eng_input")
		if st.button("Save Skill") and skill_name:
			store.upsert_skill(skill_name, int(level), int(energy))
			st.success(f"Saved {skill_name}")

	st.sidebar.markdown("---")
	st.sidebar.caption("Data saved locally to data/user_data.json")


def dashboard(store: UserDataStore, coach: GeminiCoach):
	st.subheader("Neural Dashboard")
	user = store.read()

	# Summary
	with st.container(border=True):
		st.markdown("### Daily Activation")
		summary = ai_summary(coach, user)
		st.write(summary)

	# Mind tree visualization with progress rings
	st.markdown("### Mind Tree")
	skills = user.get("skills", {})
	if not skills:
		st.info("Add your first skill in the sidebar.")
	else:
		cols = st.columns(3)
		for i, (skill, meta) in enumerate(skills.items()):
			with cols[i % 3]:
				level = int(meta.get("level", 0))
				energy = int(meta.get("energy", 0))
				st.markdown(
					ring_svg(
						label=skill,
						percent=level,
						subtext=f"⚡ {energy}%",
					),
					unsafe_allow_html=True,
				)


def chat(coach: GeminiCoach, store: UserDataStore):
	st.subheader("AI Mentor Chat")
	for msg in st.session_state.messages:
		with st.chat_message(msg["role"]):
			st.markdown(msg["content"])

	if prompt := st.chat_input("Ask your coach anything..."):
		st.session_state.messages.append({"role": "user", "content": prompt})
		with st.chat_message("assistant"):
			stream = coach.stream_chat(
				messages=st.session_state.messages,
				mood=st.session_state.mood,
				tone=st.session_state.tone,
				user_snapshot=store.read(),
			)
			response = st.write_stream(stream)
		st.session_state.messages.append({"role": "assistant", "content": response})


def simulation(coach: GeminiCoach, store: UserDataStore):
	st.subheader("Dynamic Skill Simulation")
	topic = st.text_input("Enter a topic (e.g., Python loops, stage confidence)")
	col1, col2 = st.columns(2)
	with col1:
		mode = st.selectbox("Simulation type", ["quiz", "scenario", "challenge"]) 
	with col2:
		boost = st.slider("Energy reward", 1, 15, 5)

	if st.button("Generate Simulation") and topic:
		with st.spinner("Synthesizing neural challenge..."):
			plan = coach.generate_simulation(topic=topic, mode=mode)
		st.markdown(plan)

	if st.button("I completed the challenge ✅"):
		store.add_energy_all(boost)
		st.success(f"Great job! Mind tree energy +{boost} to all skills.")


def growth_tracker(store: UserDataStore):
	st.subheader("Growth Tracker")
	user = store.read()
	engagements = user.get("engagements", [])
	st.caption("Recent engagement pulses")
	if not engagements:
		st.info("No activity yet. Complete a simulation or chat to add activity.")
	else:
		for pulse in engagements[-8:][::-1]:
			st.write(f"{pulse['time']} • {pulse['event']} • +{pulse['delta']} energy")

	if st.button("Log Focus Session (25m)"):
		store.log_event("focus_session", delta=3)
		st.success("Logged +3 energy across skills.")


def vision_mode(coach: GeminiCoach, store: UserDataStore):
	st.subheader("Vision Mode 🚀")
	if st.button("Generate a 6-month future snapshot"):
		with st.spinner("Projecting timelines with creative synthesis..."):
			vision = coach.generate_vision(store.read())
		st.markdown(vision)


def main():
	st.set_page_config(page_title=APP_TITLE, page_icon="🧠", layout="wide")
	inject_global_styles()
	init_state()

	store = UserDataStore(DATA_PATH)
	coach = GeminiCoach()

	sidebar_controls(store)

	st.title(APP_TITLE)
	st.caption("An adaptive AI mentor blending neuroscience + AI skills")

	tab_dash, tab_chat, tab_sim, tab_growth, tab_vision = st.tabs(
		["Dashboard", "Mentor Chat", "Simulation", "Growth", "Vision"]
	)

	with tab_dash:
		dashboard(store, coach)
	with tab_chat:
		chat(coach, store)
	with tab_sim:
		simulation(coach, store)
	with tab_growth:
		growth_tracker(store)
	with tab_vision:
		vision_mode(coach, store)


if __name__ == "__main__":
	main()
