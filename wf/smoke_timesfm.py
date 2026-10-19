"""Smoke test: load TimesFM 2.5 200M on CPU, run one forecast, report time/memory."""
import os
import time

os.environ.setdefault("HF_HOME", r"D:\Openwork_Projects\trading-bot\.hf_cache")

import numpy as np

def rss_mb() -> float:
    import psutil

    return psutil.Process().memory_info().rss / 1e6

print(f"RSS before load: {rss_mb():.0f} MB", flush=True)
t0 = time.time()
import timesfm

model = timesfm.TimesFM_2p5_200M_torch.from_pretrained(
    "google/timesfm-2.5-200m-pytorch", torch_compile=False
)
print(f"Model downloaded+loaded in {time.time() - t0:.1f}s, RSS={rss_mb():.0f} MB", flush=True)

model.compile(
    timesfm.ForecastConfig(
        max_context=512,
        max_horizon=16,
        per_core_batch_size=1,
        normalize_inputs=True,
    )
)
print("Compiled (no torch.compile).", flush=True)

rng = np.random.default_rng(42)
# synthetic random-walk, 512 points
series = np.cumsum(rng.normal(0, 1, 512)) + 100.0
t1 = time.time()
point, quantiles = model.forecast(horizon=16, inputs=[series])
dt = time.time() - t1
print(f"One forecast: {dt:.2f}s, RSS={rss_mb():.0f} MB", flush=True)
print(f"point shape={point.shape}, last known={series[-1]:.2f}, "
      f"fwd mean={point[0].mean():.2f}", flush=True)
print("SMOKE OK", flush=True)
