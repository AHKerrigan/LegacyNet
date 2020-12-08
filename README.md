# LegacyNet Model

We set up a separate conda training environment using the tutorial found here: 
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html#tf-install



## Training Setup

After following the tutorial to set up the environment, it is time to set up the actual model data.
[ ] need to be changed to what they are in your setup.

```
conda activate [TF ENV NAME]

cd [LEGACYNET FOLDER LOCATION]

python scripts/preprocessing/partition_dataset.py -i [TRAINING DATA LOCATION] -o ./ -x

python scripts/preprocessing/yolo_csv.py -i ./train/ -l annotations/label_map.pbtxt -c annotations/train_annotations.csv -t ./train.record

python scripts/preprocessing/yolo_csv.py -i ./test/ -l annotations/label_map.pbtxt -c annotations/test_annotations.csv -t ./test.record
```
Under `models/ssd_mobilenet/pipeline.config` make sure the input_path on `line 175` is correctly set to the path
to `train.record` and the `input_path` on `line 187` to the path to `test.record`. 

## Start Training

Begin training by running

```
python scripts/training/model_main_tf2.py --model_dir=models/ssd_mobilenet --pipeline_config_path=models/ssd_mobilenet/pipeline.config
```

You can monitor the job by opening a new terminal and running `tensorboard --logdir=models/ssd_mobilenet`

## Exporting the Model

To export the model, run the following command (changing the [ ] to whatever you want the folder to be called):

```
python .\exporter_main_v2.py --input_type image_tensor --pipeline_config_path .\models\ssd_mobilenet\pipeline.config --trained_checkpoint_dir .\models\ssd_mobilenet\ --output_directory .\exported_models\[NAME OF EXPORTED RUN]
```
