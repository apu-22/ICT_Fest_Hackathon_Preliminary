"""Human-facing booking reference codes.

Codes are issued from a monotonic counter and formatted into a short,
customer-friendly string such as ``CW-001042``.
"""

#bug-9->fixed
import threading
import time

_counter = {"value": 1000}
_lock = threading.Lock()

def _format_pause() -> None:
    time.sleep(0.12)

def next_reference_code() -> str:
    with _lock:
        current = _counter["value"]
        _format_pause()
        _counter["value"] = current + 1
        return f"CW-{current:06d}"