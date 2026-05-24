# ReflexionTemporalMemorySuccessAgentRAG (RTMS-RAG)

Self-reflective Retrieval-Augmented Generation (RAG) architecture and code accompanying a Master's thesis on reducing hallucination propagation in agentic RAG systems. This repository contains the RTMS implementation, baseline variants, evaluation drivers, data-ingest utilities, and the LaTeX thesis sources (thesis sources are kept local by default).

## Quickstart

1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv rag-env
source rag-env/bin/activate
pip install -r requirements.txt
```

2. Set required environment variables (see next section) then run an evaluation example:

```bash
# Example: run the fixed-context evaluation used in the thesis
python evaluate_cross_repo_fixed_context.py

# Example: run the local legal benchmark
python evaluate_local_benchmark.py
```

## Environment variables

The code reads several credentials and configuration items from environment variables. Common ones:

- `PINECONE_API_KEY` — API key for Pinecone vector DB
- `PINECONE_INDEX_NAME` — (optional) name of index
- `YANDEX_API_KEY` or `YANDEX_IAM_TOKEN`, `YANDEX_FOLDER_ID` — for Yandex services used by embedding/vision clients
- `GEMINI_API_KEY` — for Google Gemini (if used)
- `OLLAMA_URL` / `OLLAMA_MODEL` — for a local Ollama provider (optional)

Set these safely in your shell or via a `.env` file (do not commit credentials). See [ReflexionTemporalMemorySuccessAgentRAG/.env.example](ReflexionTemporalMemorySuccessAgentRAG/.env.example) for a starting list.

## Reproducibility

- `requirements.txt` contains the minimal package list needed for experiments. After you verify the environment, capture exact package versions for reproducibility:

```bash
pip freeze > requirements-freeze.txt
```

- Large datasets and model checkpoints are intentionally excluded from the repository. Use the `data/` and `models/` folders as placeholders; provide download instructions or external links in `docs/` or the thesis appendix.

## Repository layout (top-level)

- Top-level compatibility shims (keep previous import paths working):
	- `rag.py`, `retrieve.py`, `ingest.py`, `load_data.py`, `pinecone_setup.py`, `yandex_embed.py` — small wrappers that re-export the real implementations from `ReflexionTemporalMemorySuccessAgentRAG/src/`.

- Implementation package (new):
	- `ReflexionTemporalMemorySuccessAgentRAG/src/` — core implementation moved into an importable `src` package. Key modules:
		- `src/rag.py`, `src/retrieve.py`, `src/ingest.py`, `src/load_data.py`, `src/pinecone_setup.py`, `src/yandex_embed.py`

- Evaluation & drivers:
	- `evaluate_cross_repo_fixed_context.py`, `evaluate_local_benchmark.py`, `evaluate_ragtruth_fixed_context.py` (top-level drivers used in experiments)

- Other folders: `docs/`, `data/` (placeholder), `models/` (placeholder), thesis sources (kept local)

> Note: By default `.gitignore` excludes `data/`, `models/`, virtual environments and editor caches.

## What will be pushed (recommended)

To make the repository push-ready while keeping large and local-only artifacts out of the remote, I recommend including:

- **Included:** Core code and metadata needed to reproduce experiments:
	- Root metadata: `README.md`, `requirements.txt`, `.gitignore`
	- Top-level wrappers (compatibility shims) and the `ReflexionTemporalMemorySuccessAgentRAG/src/` package with full implementations
	- Evaluation drivers and `docs/`

- **Excluded (recommended):** Large datasets, model weights, generated outputs, and local environments:
	- `memories/`, `eval_runs/`, `eval_clean_runs/`
	- Large files: `*.jsonl`, `*.json`, `*.npz`, `*.pt`, `*.bin`, model checkpoints
	- Local envs and caches: `rag-env/`, `venv/`, `__pycache__/`, `.pytest_cache/`

## Running experiments

1. Prepare environment and credentials.
2. Index the dataset (if not already indexed):

```bash
python ingest.py
```

3. Run a fixed-context evaluation or benchmark script (examples above). Saved evaluation outputs and logs are written alongside the respective evaluation scripts unless configured otherwise.

## Tests

Run unit tests (where available):

```bash
pytest -q
```

## Contributing

If you want to extend a baseline, add a new experiment, or help reproduce results, open an issue or submit a pull request. Keep changes focused and provide instructions to reproduce any new experiments.

## License & Citation

If you reuse code or results, please cite the associated thesis. Add a citation block here (or request one and I will generate BibTeX).

---

If you'd like I can commit these repository changes (I will show the exact files to be staged first). Tell me if you also want me to push to the remote after committing.# RTMS-RAG
