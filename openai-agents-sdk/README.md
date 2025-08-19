 Development Lifecycle (Step-By-Step)

| Step | Title                      | Description                                                                                                                                |
| ---- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | Initialize the Project     | `uv init` scaffolds a clean project structure and starter `pyproject.toml`, replacing manual folder setup and template copying.            |
| 2    | Pin the Python Version     | `uv python pin 3.12` ensures everyone uses the same interpreter version, downloading it if necessary and recording it for all devs and CI. |
| 3    | Create Environment         | `uv` creates a virtual environment automatically on first dependency action. `uv run` lets you execute code without manual activation.     |
| 4    | Add Runtime Dependencies   | `uv add pkg` updates your manifest, resolves, locks, and installs in one atomic step—keeping declared and installed packages in sync.      |
| 5    | Add Dev Tools              | `uv add --dev tool` cleanly separates dev dependencies (tests, lint, format) from runtime packages, all in the same lock file.             |
| 6    | Optional Feature Groups    | `uv add --group docs mkdocs` lets you define install-on-demand groups for optional features.                                               |
| 7    | Lock Dependencies          | `uv` automatically maintains `uv.lock` after changes for reproducible installs.                                                            |
| 8    | Sync Environment           | `uv sync` ensures the environment matches the lock file exactly; `uv sync --frozen` blocks changes unless the lock is updated.             |
| 9    | Run Code & Tools           | `uv run <cmd>` runs commands in the correct environment without needing to activate the venv.                                              |
| 10   | Lint / Format / Type Check | Running tools via `uv run` ensures they use the exact locked versions locally and in CI.                                                   |
| 11   | Test                       | `uv run pytest` guarantees tests run with the locked dependency set—no “works on my machine” surprises.                                    |
| 12   | Upgrade Dependencies       | `uv upgrade` re-resolves, locks, and installs updates in one controlled step.                                                              |
| 13   | Build Artifacts            | `uv build` quickly produces both wheel and sdist artifacts with minimal config.                                                            |
| 14   | Publish                    | `uv publish` builds (if needed) and uploads to PyPI or another index in one step.                                                          |
| 15   | Use Cache                  | Shared caching speeds up installs and can be inspected or pruned.                                                                          |
| 16   | Offline / Restricted       | Cache export/import plus `uv sync --frozen` allows full offline environment recreation.                                                    |
| 17   | CI Reproducibility         | `uv sync --frozen` in CI ensures lock and manifest match before install.                                                                   |
| 18   | Inspect Environment        | `uv run pip list` and similar commands always target the project’s environment, not the global Python.                                     |
| 19   | Clean & Prune              | `uv cache prune` or environment removal frees space; everything can be rebuilt from manifest + lock.                                       |
| 20   | Monorepo Management        | Each project in a monorepo can have its own `pyproject.toml` + `uv.lock` for independent syncing.                                          |
| 21   | Migrate (Optional)         | `uv` can import specs from legacy requirement files, resolve, and lock—simplifying to the two-file model.                                  |
