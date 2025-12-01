import os
import glob
import json
import pandas as pd

from setting import setting

ANNOTATION_DIR = setting.DATASETS_PATH / "annotations"

CSV_COLUMNS = [
    'annotation_id', 'batch_id', 'annotator_id',
    'policy_id', 'segment_id', 'category',
    'attributes', 'url', 'date'
]

df = pd.read_csv(ANNOTATION_DIR / "105_amazon.com.csv", names=CSV_COLUMNS)
