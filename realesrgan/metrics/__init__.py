import importlib
from basicsr.utils import scandir
from os import path as osp

# automatically scan and import model modules for registry
# scan all the files that end with '_model.py' under the model folder
metric_folder = osp.dirname(osp.abspath(__file__))
metric_filenames = [osp.splitext(osp.basename(v))[0] for v in scandir(metric_folder) if v.endswith('_metric.py')]
# import all the model modules
_model_modules = [importlib.import_module(f'realesrgan.metrics.{file_name}') for file_name in metric_filenames]
