import kagglehub

# Download latest version
path1 = kagglehub.model_download("timm/tf-efficientnet/pyTorch/tf-efficientnet-b6")
path2 = kagglehub.model_download("timm/tf-efficientnet/pyTorch/tf-efficientnet-b6")

print("Path to model files:", path1)
print("Path to model files:", path2)