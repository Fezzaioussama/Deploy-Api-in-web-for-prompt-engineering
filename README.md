# Unified Categories Generator

> Merges several retail product taxonomies into one coherent hierarchy using an LLM — a Flask API with a Streamlit front end.

A retailer running seasonal catalogues ends up with three overlapping category
trees: *Été*, *Enfants*, *Noël*. Each nests differently, and "Robes" appears in
all three at different depths. Reconciling them by hand is tedious and
inconsistent.

This sends all three to an LLM and asks for a single unified *référentiel*.
Flask does the model call, Streamlit provides the interface.

> ### ⚠️ Security notice
>
> **`app.py` contains a hardcoded OpenAI API key.** It has been in this public
> repository's history since January 2024 and must be treated as compromised.
>
> **Revoke it** at <https://platform.openai.com/api-keys>, then switch to the
> environment variable — the correct line is already in the file, commented out
> one line above:
>
> ```python
> client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
> ```
>
> Deleting the key from `app.py` is not enough on its own; it remains in the git
> history until the history is rewritten.

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."      # after fixing app.py as above
```

`requirements.txt` lists `request`, which is a typo for `requests` — install
that instead, or `pip install flask openai streamlit requests` directly.

## Run

Two processes. Backend first:

```bash
flask --app app run        # http://127.0.0.1:5000
```

Then the front end:

```bash
streamlit run client.py
```

Paste the three catalogues into the text areas and click **Generate Unified
Categories**.

## How it works

```mermaid
flowchart LR
    S["Streamlit UI<br/>client.py"] -->|"POST JSON"| F["Flask API<br/>app.py"]
    F -->|"chat.completions"| O["OpenAI"]
    O --> F --> S
```

`client.py` POSTs `{catalogue_ete, catalogue_enfants, catalogue_noel}` to the
Flask root route. `generate_unified_categories()` interpolates all three into a
French prompt, sends it to `gpt-3.5-turbo` with the system message *"Unified
référentiel."*, and returns `{"unified_categories": ...}`.

`GET /` returns `{"error": "Not allowed"}` — the route is POST-only in practice.

## Sample data

Three real catalogue trees are included to test with:

| File | Catalogue |
|---|---|
| `Referentiel1.txt` | Enfants — Vêtements → Filles/Garçons → Robes, Tops, … |
| `Referentiel2.txt` | Noël — Cadeaux → Pour Elle/Lui → Bijoux, Beauté, … |
| `Referentiel3.txt` | Été — Prêt-à-porter → Femmes/Hommes → Robes, … |

Each is a numbered hierarchy (`1.1.1.1`) four levels deep. Paste their contents
into the matching Streamlit fields.

## Known issues

Beyond the API key above:

- **`requirements.txt` has `request`** instead of `requests`.
- **The model is pinned to `gpt-3.5-turbo`**, long superseded. Newer models will
  produce noticeably better taxonomy merges for this task.
- **No error handling on the LLM call** — a rate limit or timeout surfaces as a
  raw exception.
- **The prompt and system message are minimal.** "Unified référentiel." gives the
  model little to work with; specifying the desired output format and numbering
  scheme would make results far more consistent.
- The API key would also need to be revoked before this could be deployed
  anywhere.
