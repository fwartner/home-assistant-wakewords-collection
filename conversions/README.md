
# Manual Instructions: Convert TFLite to ONNX

Converts TensorFlow Lite wakeword models to ONNX format (both are supported by OpenWakeWord, with ONNX-only on Windows)

## How to use

### Quick test (1 file)
```bash
cd conversions
docker build -t wakeword-converter .
docker run --rm -v $(pwd)/..:/workspace -w /workspace wakeword-converter --sample
```

### Convert all files
```bash
cd conversions
docker build -t wakeword-converter .
docker run --rm -v $(pwd)/..:/workspace -w /workspace wakeword-converter
```

### Build and run in one command
```bash
cd conversions
docker build -t wakeword-converter . && docker run --rm -v $(pwd)/..:/workspace -w /workspace wakeword-converter --sample
```

Converted ONNX files will appear next to the original TFLite files.
