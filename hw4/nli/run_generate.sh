CUDA_VISIBLE_DEVICES=0 python3 generate-similarity-data.py --data_dir ../dataset \
    --model_type bert \
    --model_name_or_path ../output/try/checkpoint-44100/\
    --config_name bert-base-chinese\
    --tokenizer_name bert-base-chinese\
    --output_dir ../output/similarity \
    --cache_dir ../dataset_cache \
    --do_eval \
    --evaluate_during_training \
    --do_lower_case \
    --warmup_steps 500 \
    --language zh \
    --per_gpu_train_batch_size 24 \
    --per_gpu_eval_batch_size 24 

