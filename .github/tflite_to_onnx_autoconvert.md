# TFLite to ONNX Conversion

Automatically converts `.tflite` files to `.onnx` format when pushed to the repository.

## Triggers
- Push with `.tflite` files
- Pull requests with `.tflite` files  
- Manual trigger (Actions tab)

## Process
1. Finds all `.tflite` files
2. Skips if `.onnx` already exists and is newer
3. Converts using `tf2onnx.convert`
4. Commits new `.onnx` files

## Dependencies
- TensorFlow 2.16.0-2.18.0
- tf2onnx 1.16.1+
- NumPy <2.0
- ONNX Opset 15

## Output
Creates `.onnx` files alongside `.tflite` files in same directories.
