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
**max\_step**: 12001 is enough when CTC loss is used.

**ctc\_weight**: maybe 0.5?

## config/dlhlp/decode.yaml
**beam\_size**: greater better

**lm\_weight**: not sure?

**ctc\_weight**: can only be 0. or 1.

# Experiments
lm\_weight | loss ctc\_weight | decode ctc\_weight | beam\_size | asr\_steps | **Dev. Char Error Rate(\%)** | **Dev. Word Error Rate(\%)** | **Kaggle Score**
:---------:|:----------------:|:------------------:|:----------:|:----------:|:----------------------------:|:---------------------------:|:----------------:
0.3|0.|0.|5|12001|2.9526|9.2290|1.754
0.2|0.2|0.|5|12001|1.9519|6.4261|
0.3|0.2|0.|5|12001|1.8465|6.0594|
0.4|0.2|0.|5|12001|1.8061|5.8850|1.128
0.5|0.2|0.|5|12001|2.0416|5.9126|
0.6|0.2|0.|5|12001|2.0308|5.8646|
0.7|0.2|0.|5|12001|2.1395|5.8917|
0.2|0.3|0.|5|12001|1.9557|6.4956|
0.3|0.3|0.|5|12001|1.8979|6.2687|
0.4|0.3|0.|5|12001|1.8434|6.0769|1.072
0.5|0.3|0.|5|12001|1.8143|5.9136|1.042
0.6|0.3|0.|5|12001|1.7649|5.7494|1.034
0.7|0.3|0.|5|12001|1.7956|5.7066|
0.2|0.4|0.|5|12001|2.0736|6.8996|
0.3|0.4|0.|5|12001|2.0127|6.6556|
0.4|0.4|0.|5|12001|1.9258|6.3759|
0.5|0.4|0.|5|12001|1.8962|6.2124|
0.6|0.4|0.|5|12001|1.8685|6.0905|
0.7|0.4|0.|5|12001|1.9346|6.0758|
0.2|0.5|0.|5|12001|1.9508|6.5784|
0.3|0.5|0.|5|12001|1.8733|6.3137|1.082
0.4|0.5|0.|5|12001|1.7965|6.0639|
0.5|0.5|0.|5|12001|1.7292|5.8467|1.038
0.6|0.5|0.|5|12001|1.6838|5.6423|1.004
0.7|0.5|0.|5|12001|1.6646|5.5716|1.218
0.2|0.6|0.|5|12001|2.0172|6.6447|
0.3|0.6|0.|5|12001|1.9312|6.3307|
0.4|0.6|0.|5|12001|1.8886|6.1447|
0.5|0.6|0.|5|12001|1.8311|5.9237|
0.6|0.6|0.|5|12001|1.8759|5.9268|
0.7|0.6|0.|5|12001|1.8606|5.8207|
0.2|0.7|0.|5|12001|1.9615|6.5334|
0.3|0.7|0.|5|12001|1.9122|6.3535|
0.4|0.7|0.|5|12001|1.8907|6.1789|
0.5|0.7|0.|5|12001|1.8232|5.9312|
0.6|0.7|0.|5|12001|1.8664|5.8569|
0.7|0.7|0.|5|12001|1.9448|5.9521|
