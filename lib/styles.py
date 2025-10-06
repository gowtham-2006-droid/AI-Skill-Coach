import streamlit as st


def inject_global_styles() -> None:
	st.markdown(
		"""
		<style>
		:root{
			--glass-bg: rgba(255,255,255,0.08);
			--glass-br: 16px;
			--glass-blur: saturate(180%) blur(12px);
			--grad-1: linear-gradient(135deg, #8e2de2 0%, #4a00e0 100%);
			--grad-2: radial-gradient(1000px 600px at 10% 10%, rgba(0,255,255,0.18), transparent 60%),
					 radial-gradient(800px 500px at 90% 20%, rgba(255,0,200,0.16), transparent 60%);
		}
		body { background: #0b1020; color: #e8e8ef; }
		section.main > div { padding-top: 10px; }
		.block-container{ padding-top: 1rem; }
		
		/* Glass cards */
		.stContainer, .stMarkdown, .stChatMessage, .stTabs, .stExpander{
			background: var(--glass-bg);
			border-radius: var(--glass-br);
			backdrop-filter: var(--glass-blur);
			border: 1px solid rgba(255,255,255,0.06);
		}
		
		/* Accent gradient halo */
		header { background: var(--grad-2); }
		
		/* Progress ring container */
		.mind-ring{ display: grid; place-items: center; margin: 12px 0; }
		.mind-ring .label{ margin-top: 8px; font-weight: 600; letter-spacing: 0.4px; }
		.mind-ring .sub{ opacity: 0.8; font-size: 12px; }
		
		</style>
		""",
		unsafe_allow_html=True,
	)


def ring_svg(label: str, percent: int, subtext: str = "") -> str:
	percent = max(0, min(100, percent))
	# SVG ring with animated stroke
	size = 140
	radius = 60
	circumference = 2 * 3.14159 * radius
	dash = circumference * (percent / 100)
	gap = circumference - dash
	return f"""
	<div class='mind-ring'>
	<svg width='{size}' height='{size}' viewBox='0 0 {size} {size}'>
		<defs>
			<linearGradient id='grad' x1='0%' y1='0%' x2='100%' y2='100%'>
				<stop offset='0%' stop-color='#00e5ff'/>
				<stop offset='100%' stop-color='#ff00c3'/>
			</linearGradient>
		</defs>
		<circle cx='{size/2}' cy='{size/2}' r='{radius}' stroke='rgba(255,255,255,0.08)' stroke-width='12' fill='none'/>
		<circle cx='{size/2}' cy='{size/2}' r='{radius}' stroke='url(#grad)' stroke-width='12' fill='none'
			stroke-linecap='round' stroke-dasharray='{dash} {gap}'>
			<animate attributeName='stroke-dasharray' from='0 {circumference}' to='{dash} {gap}' dur='0.8s' fill='freeze' />
		</circle>
	</svg>
	<div class='label'>{label} — {percent}%</div>
	<div class='sub'>{subtext}</div>
	</div>
	"""
