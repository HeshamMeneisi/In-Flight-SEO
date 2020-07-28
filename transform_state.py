import transformers
import _transformers


def transform_state(state, rule):
    for t in rule["transformations"]:
        apply_trans(t, state)


def apply_trans(t, state):
    t_func = None
    
    try:
        t_func = getattr(transformers, t["name"])
    except:
        try:
            t_func = getattr(_transformers, t["name"])
        except:
            pass
        
    if t_func is None:
        print(f"Unknown transformer {t['name']}")
    else:
        t_func(state, **t["params"])
