# Usage

## Prepare Vocab-Count File
```bash
python3 util/generate_vocab_file.py --input_file data/text-data.txt --mode character --output_file data/vocab.txt
```

## Train ASR
```bash
python3 main.py --config config/dlhlp/asr.yaml
```

## Train LM
```bash
python3 main.py --config config/dlhlp/lm.yaml --lm
```

## Tensorboard
```bash
tensorboard --logdir log/
```

## Decode
```bash
python3 main.py --config config/dlhlp/decode.yaml --test --njobs 8
```

## Post-Process CTC Outputs
```bash
TODO
```

## Evaluate
```bash
python3 eval.py --file result/decode_dev_output.csv
```

## Post-Process into Kaggle Format
```bash
python3 format.py result/decode_test_output.csv kaggle.csv
```

# Useful Parameters

## config/dlhlp/asr.yaml: 
max\_step: can be larger than 12001. I guess 20001 whould be proper.

ctc\_weight: maybe 0.5?

## config/dlhlp/decode.yaml
beam\_size: greater better

lm\_weight: not sure?

ctc\_weight: can only be 0. or 1.

# Experiments
lm\_weight | loss ctc\_weight | decode ctc\_weight | beam\_size | asr\_steps **|** **Dev. Char Error Rate(\%)** | **Dev. Word Error Rate(\%)** | **Kaggle Score**
:---------:|:----------------:|:------------------:|:----------:|:------------:|:------------------------------:|:---------------------------:|:----------------:
0.3        |0.                |0.                  |5           |12001         |2.9526                          |9.2290                        |
