import os
from flask import Flask, request, jsonify
from openai import OpenAI

#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(api_key="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")
app = Flask(__name__)
# TODO add swagger


def generate_unified_categories(catalogue_ete, catalogue_enfants, catalogue_noel):
    """add doc string"""
    prompt = f"Unifiez les catalogues suivants :\n\nCatalogue Été:\n{catalogue_ete}\n\nCatalogue Enfants:\n{catalogue_enfants}\n\nCatalogue Noël:\n{catalogue_noel}\n\nNouveau référentiel unifié :"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Unified référentiel."},
            {"role": "user", "content": prompt},
        ],
    )
    unified_categories = completion.choices[0].message.content
    return unified_categories


@app.route("/", methods=["POST", "GET"])
def unify_categories():
    if request.method == "GET":
        return jsonify({"error": "Not allowed"})
    try:
        catalogue_ete = request.json.get("catalogue_ete")
        catalogue_enfants = request.json.get("catalogue_enfants")
        catalogue_noel = request.json.get("catalogue_noel")

        referentiel_unifie = generate_unified_categories(
            catalogue_ete, catalogue_enfants, catalogue_noel
        )

        return jsonify({"unified_categories": referentiel_unifie})

    except Exception as e:
        return f"Error in OpenAI API: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
