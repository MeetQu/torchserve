cd /root/vbr || exit
source /root/anaconda3/bin/activate torchserve

torchserve --stop

torch-model-archiver --model-name vbr --version 1.0 --serialized-file best_model.pt --export-path model_store --extra-files ./index_to_name.json --handler handler --force

rm -r logs
torchserve --start --ncs --model-store model_store --models vbr.mar --ts-config config.properties
