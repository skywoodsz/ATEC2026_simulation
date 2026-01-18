"""Example: consume obs from play_atec in-process."""

from play_atec import run_play, get_latest_obs


def on_obs(obs):
	# Example: access groups in TensorDict
	# print available groups once in a while or inspect specific group

	print("obs keys:", list(obs.keys()))
	for name, value in obs.items():
		shape = tuple(getattr(value, "shape", ()))
		print(f"  - {name}: type={type(value)}, shape={shape}")


def main() -> None:
	run_play(obs_callback=on_obs)


if __name__ == "__main__":
	main()
