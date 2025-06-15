FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

RUN uv pip install --system --no-cache \
    "tensorflow>=2.15.0,<2.16.0" \
    "tf2onnx>=1.16.1" \
    "numpy<2.0" \
    "onnxruntime>=1.16.0"

WORKDIR /workspace

COPY convert.py /workspace/conversions/

ENTRYPOINT ["python", "conversions/convert.py"]
