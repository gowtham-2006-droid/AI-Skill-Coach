from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

try:
	import orjson  # type: ignore
except Exception:  # pragma: no cover
	orjson = None  # fallback to stdlib json


_DEFAULT_DATA: Dict[str, Any] = {
	"user": {
		"name": "Explorer",
	},
	"mood": "focused",
	"skills": {
		"Python": {"level": 20, "energy": 30},
		"Public Speaking": {"level": 10, "energy": 20},
	},
	"engagements": [],
}


class UserDataStore:
	def __init__(self, path: Path) -> None:
		self.path = Path(path)
		self.path.parent.mkdir(parents=True, exist_ok=True)
		if not self.path.exists():
			self.write(_DEFAULT_DATA)

	def read(self) -> Dict[str, Any]:
		data_bytes = self.path.read_bytes()
		if orjson:
			return orjson.loads(data_bytes)
		return json.loads(data_bytes.decode("utf-8"))

	def write(self, data: Dict[str, Any]) -> None:
		if orjson:
			self.path.write_bytes(orjson.dumps(data, option=orjson.OPT_INDENT_2))
		else:
			self.path.write_text(json.dumps(data, indent=2))

	def upsert_skill(self, name: str, level: int, energy: int) -> None:
		data = self.read()
		skills = data.setdefault("skills", {})
		skills[name] = {"level": max(0, min(100, level)), "energy": max(0, min(100, energy))}
		self.write(data)

	def add_energy_all(self, delta: int) -> None:
		data = self.read()
		for meta in data.get("skills", {}).values():
			meta["energy"] = max(0, min(100, int(meta.get("energy", 0)) + int(delta)))
		self.log_event("challenge_completed", delta=delta, persist=False, base=data)
		self.write(data)

	def log_event(self, event: str, delta: int = 0, persist: bool = True, base: Dict[str, Any] | None = None) -> None:
		data = base if base is not None else self.read()
		from datetime import datetime
		data.setdefault("engagements", []).append(
			{"time": datetime.now().strftime("%Y-%m-%d %H:%M"), "event": event, "delta": delta}
		)
		if persist and base is None:
			self.write(data)
