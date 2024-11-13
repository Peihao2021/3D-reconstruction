## Environment Setup

```
conda create --name myenv python=3.9

conda activate myenv

pip install altgraph==0.17.2 appnope==0.1.4 asttokens==2.4.1 beautifulsoup4==4.12.3 \
certifi==2024.6.2 charset-normalizer==3.3.2 comm==0.2.2 contourpy==1.2.1 cycler==0.12.1 \
debugpy==1.8.1 decorator==5.1.1 exceptiongroup==1.2.1 executing==2.0.1 fastprogress==1.0.3 \
filelock==3.14.0 fonttools==4.53.0 fsspec==2024.6.0 future==0.18.2 google==3.0.0 h5py==3.11.0 \
huggingface-hub==0.24.6 idna==3.7 importlib_metadata==7.1.0 importlib_resources==6.4.0 \
ipykernel==6.29.4 ipython==8.18.1 jedi==0.19.1 Jinja2==3.1.4 joblib==1.4.2 jupyter_client==8.6.2 \
jupyter_core==5.7.2 kiwisolver==1.4.5 kornia==0.7.3 kornia_rs==0.1.5 macholib==1.15.2 \
MarkupSafe==2.1.5 matplotlib==3.9.0 matplotlib-inline==0.1.7 mpmath==1.3.0 nest-asyncio==1.6.0 \
networkx==3.2.1 numpy==1.26.4 opencv-python==4.10.0.82 packaging==24.0 pandas==2.2.2 \
parso==0.8.4 pexpect==4.9.0 pillow==10.3.0 pip==24.2 platformdirs==4.2.2 \
prompt_toolkit==3.0.46 psutil==5.9.8 ptyprocess==0.7.0 pure-eval==0.2.2 py-cpuinfo==9.0.0 \
pycolmap==3.10.0 Pygments==2.18.0 pyparsing==3.1.2 python-dateutil==2.9.0.post0 \
pytz==2024.1 PyYAML==6.0.1 pyzmq==26.0.3 requests==2.32.3 safetensors==0.4.4 \
scikit-learn==1.5.1 scipy==1.13.1 seaborn==0.13.2 setuptools==58.0.4 six==1.15.0 \
soupsieve==2.5 stack-data==0.6.3 sympy==1.12.1 threadpoolctl==3.5.0 timm==1.0.9 \
torch==2.3.0 torchvision==0.18.0 tornado==6.4 tqdm==4.66.4 traitlets==5.14.3 \
typing_extensions==4.12.1 tzdata==2024.1 ultralytics==8.2.28 ultralytics-thop==0.2.7 \
urllib3==2.2.1 wcwidth==0.2.13 wheel==0.37.0 zipp==3.19.2
```

## Dependency Setup

```
pip install kaggle
```

Then create a Kaggle API (Please ask ChatGPT if you need help.).

```
python download_kaggle_data.py

python download.py
```

For the tree of the directory, please refer to detailed code in the .ipynb file. You may have to modify several relative paths.

## About The Comment
- I use zhr: to note where I have add or modifies.
- The src is about the path, you can modifies it to your local absolute path.
- The change of model is still under test since it locally run out of the Memory.
- The 3D-graph can already be genreated. 