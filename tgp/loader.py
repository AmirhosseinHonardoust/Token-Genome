import os

def load_sources(path):
    out = {}
    if os.path.isfile(path) and path.endswith(".sol"):
        with open(path,"r",encoding="utf-8") as f:
            out[os.path.basename(path)] = f.read()
        return out
    if os.path.isdir(path):
        for root,dirs,files in os.walk(path):
            for n in files:
                if n.endswith(".sol"):
                    p = os.path.join(root,n)
                    with open(p,"r",encoding="utf-8") as f:
                        out[n] = f.read()
    return out

def ensure_genomes():
    g = os.path.join(os.getcwd(),"genomes")
    os.makedirs(g,exist_ok=True)
    return g
