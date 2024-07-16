import torch
import subprocess

def check_cuda():
    cuda_available = torch.cuda.is_available()
    cuda_version = torch.version.cuda if cuda_available else None

    print(f"CUDA Available: {cuda_available}")
    if cuda_available:
        print(f"CUDA Version: {cuda_version}")

def check_pytorch_version():
    pytorch_version = torch.__version__
    print(f"PyTorch Version: {pytorch_version}")

def check_nvcc_version():
    try:
        result = subprocess.run(['nvcc', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("nvcc Version:")
            print(result.stdout)
        else:
            print("Failed to get nvcc version")
            print(result.stderr)
    except FileNotFoundError:
        print("nvcc not found. Please ensure CUDA is installed and nvcc is in your PATH.")

if __name__ == "__main__":
    check_pytorch_version()
    check_cuda()
    check_nvcc_version()
