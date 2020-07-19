import transformers

def transform_state(state, route):
    for t in route["transformations"]:
        apply_trans(t, state)
    
def apply_trans(t, state):
    t_func = getattr(transformers, t["name"])
    t_func(state, **t["params"])
