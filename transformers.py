import re


def replace_meta_value(state, id_attrib, id_value, new_value):
    state["html"] = re.sub(f'<meta {id_attrib}=["\']*{id_value}["\']*[^>]+>', f'<meta {id_attrib}="{id_value}" content="{new_value}">', state["html"])


def inject_meta_field(state, field):
    state["html"] = re.sub('<head>', f'<head>{field}', state["html"])


def replace_tag(state, tag, replacment):
    # This regex covers only basic tags with no attributes (e.g. <title>Title</title>)
    state["html"] = re.sub(f"<{tag}>[^<]*</{tag}>", replacment, state["html"])
