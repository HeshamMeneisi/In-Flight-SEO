# User-defined transformers


def replace_text(state, text, replacment):
    state["html"] = state["html"].replace(text, replacment)
