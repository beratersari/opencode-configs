---
name: machine-learning
description: ML / training skill. Load when the diff changes training scripts, *.ipynb model code, torch/tensorflow/sklearn imports, or model artifact loaders.
license: MIT
compatibility: opencode
---

# Machine learning

Project rules still win.

## Look for

- Train/test leakage (fit on full data, then split; target
  in features).
- Random seed not set when this change claims reproducibility.
- Metric that does not match the task (accuracy on a 1%
  positive class this change introduced).
- `eval()` / pickle load of an untrusted checkpoint.
- GPU tensor left on device when the rest of the batch
  is CPU (silent wrong result / OOM).
- Path that downloads weights on every request without
  the project's cache.

## Do not flag

- Framework wars (PyTorch vs TF).
- Suggesting a larger model as the fix.
