#!/bin/bash

python3 src/run_squad.py --predict_file $2 --model_type albert_zh --model_name_or_path albert_qa --output_dir albert_qa --do_eval --per_gpu_eval_batch_size 16
python3 src/json_to_csv.py albert_qa/predictions_.json $3
