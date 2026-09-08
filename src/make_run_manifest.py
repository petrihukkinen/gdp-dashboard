"""Write results/run_manifest.json: environment, versions, seeds, file hashes of src/ results/ sources/ reports/."""
import json, hashlib, os, platform, subprocess, sys, datetime
root = os.path.join(os.path.dirname(__file__), "..")
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
files = {}
for d in ("src", "results", "sources", "reports", "claims", "tests"):
    for f in sorted(os.listdir(os.path.join(root, d))):
        p = os.path.join(root, d, f)
        if os.path.isfile(p) and f != "run_manifest.json": files[f"{d}/{f}"] = dict(sha256=sha(p), bytes=os.path.getsize(p))
import numpy, scipy, sympy, pandas, matplotlib
man = dict(run_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), python=sys.version.split()[0], platform=platform.platform(),
           versions=dict(numpy=numpy.__version__, scipy=scipy.__version__, sympy=sympy.__version__, pandas=pandas.__version__, matplotlib=matplotlib.__version__),
           seeds=dict(pantheon_fit=20260908, local_expansion=20260908, bilfinger=20260908),
           git_commit=subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=root).stdout.strip(),
           blocked_hosts=["www.frontiersin.org", "doi.org", "arxiv.org", "export.arxiv.org", "ar5iv.labs.arxiv.org", "physicsfoundations.org", "archive.org", "web.archive.org", "ui.adsabs.harvard.edu", "iopscience.iop.org", "academic.oup.com"],
           reachable_hosts=["raw.githubusercontent.com", "pypi.org"], files=files)
json.dump(man, open(os.path.join(root, "results", "run_manifest.json"), "w"), indent=2)
print(f"run_manifest.json: {len(files)} files hashed")
