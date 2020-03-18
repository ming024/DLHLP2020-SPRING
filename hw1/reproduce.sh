python3 gdrive_downloader.py 1RJ00Y8fB0lWFHG7h_HdCtplI1AMQY2r5 best_ppx.pth
python3 gdrive_downloader.py 1L5VR-Bsu4BCRTsXyhrjUE7ni1WJWvnr- best_att.pth
sed -i "s@data_dir@$1@g" config/dlhlp/asr.yaml 
sed -i "s@data_dir@$1@g" config/dlhlp/lm.yaml 
python3 main.py --config config/dlhlp/decode.yaml --test --njobs 3
python3 format.py result/decode_test_output.csv result/kaggle.csv
mv result/kaggle.csv $2
