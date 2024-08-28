import os

# Kaggle API commands
commands = [
    "kaggle competitions download -c image-matching-challenge-2024",
    "kaggle datasets download -d maxchen303/hardnet8v2",
    "kaggle datasets download -d oldufo/imc2024-packages-lightglue-rerun-kornia",
    "kaggle datasets download -d oldufo/kornia-local-feature-weights",
    "kaggle datasets download -d losveria/super-glue-pretrained-network",
    # "kaggle models download -m oldufo/aliked/PyTorch/aliked-n16/1",
    # "kaggle models download -m timm/tf-efficientnet/PyTorch/tf-efficientnet-b7/1",
    # "kaggle models download -m timm/tf-efficientnet/PyTorch/tf-efficientnet-b6/1",
    # "kaggle kernels output motono0223/pytorch-lightglue-models -p ./",
    # "kaggle kernels output motono0223/dkm-dependencies -p ./",
    # "kaggle kernels output motono0223/dependencies-imc -p ./",
]

# Execute the Kaggle API commands
for command in commands:
    os.system(command)

print("All datasets and models have been downloaded.")