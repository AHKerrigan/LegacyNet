""" YOLO -> CSV and TFRecord converter, for use with LabelImg

usage: yolo_csv.py [-i INPUT_DIR] [-l LABELS_PATH] [-c CSV_PATH] [-t TFRECORD_PATH] 

optional arguments:
	-i INPUT_DIR, --input_path INPUT_DIR
			Path to DIRECTORY containing input images and their associated YOLO TXT files
	-l LABELS_PATH, --labels_path LABELS_PATH
			Path to .pbtxt file with classnames
	-c CSV_PATH, --csv_path CSV_PATH
			Path to .csv file to output annotations 
	-t TFRECORD_PATH, --tfrecord_path TFRECORD_PATH
			Path to a .record file for final output
"""

import io
import os
import csv
import glob
import argparse
from PIL import Image
from pathlib import Path
import tensorflow as tf
import pandas as pd
from object_detection.utils import dataset_util, label_map_util
from collections import namedtuple

def split(df, group):
  data = namedtuple('data', ['filename', 'object'])
  gb = df.groupby(group)
  return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def main():
  # Handle arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input_path', help='Path to folder containing images and matching YOLO .txt files', type=str)
  parser.add_argument('-l', '--labels_path', help='Path to .pbtxt file with classnames', type=str)
  parser.add_argument('-c', '--csv_path', help='Path to .csv file to output annotations', type=str)
  parser.add_argument('-t', '--tfrecord_path', help='Path to .record file to output', type=str)
  args = parser.parse_args()

  csv_data = []

  # Grab list of yolo .txt files
  file_list = glob.glob(args.input_path + "*.txt")
  for f in file_list:
    file = open(f, 'r')
    filename = Path(f).stem
    img_name = filename + '.jpg'
    print("Processing example: {}".format(img_name))
    try:
      img_file = Image.open(args.input_path + img_name)
    except IOError as e:
      print('File could not be opened, skipping: {}'.format(img_name))
      continue 
    
    width, height = img_file.size
    classname = 'headstone'
    for line in file:
      string_data = line.split(' ', 5)
      data = [float(s) for s in string_data]
      xmin = (data[1] - data[3] / 2) * width
      ymin = (data[2] - data[4] / 2) * height
      xmax = (data[1] + data[3] / 2) * width
      ymax = (data[2] + data[4] / 2) * height
      annotation = [
        img_name,
        width,
        height,
        classname,
        int(xmin),
        int(ymin),
        int(xmax),
        int(ymax)
      ]
      csv_data.append(annotation)
    file.close()

  # Write all data to .csv
  with open(args.csv_path, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
    writer.writerows(csv_data)

  # Convert .csv to Pandas dataframe
  df = pd.DataFrame(csv_data, columns=['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
  
  # Group annotations by file
  groups = split(df, 'filename')

  # Create TFRecord
  record_filename = args.tfrecord_path
  tf_writer = tf.io.TFRecordWriter(record_filename)
  for group in groups:
    img_name = group.filename
    with tf.io.gfile.GFile(os.path.join(args.input_path, '{}'.format(img_name)), 'rb') as fid:
      encoded_jpg = fid.read()
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
      xmins.append(row['xmin'] / width)
      xmaxs.append(row['xmax'] / width)
      ymins.append(row['ymin'] / height)
      ymaxs.append(row['ymax'] / height)
      classes_text.append(row['class'].encode('utf8'))
      classes.append(1) # We're only working with 1 class

    tf_example = tf.train.Example(features=tf.train.Features(feature={
      'image/height'            : dataset_util.int64_feature(height),
      'image/width'             : dataset_util.int64_feature(width),
      'image/filename'          : dataset_util.bytes_feature(img_name.encode('utf8')),
      'image/source_id'         : dataset_util.bytes_feature(img_name.encode('utf8')),
      'image/encoded'           : dataset_util.bytes_feature(encoded_jpg),
      'image/format'            : dataset_util.bytes_feature(b'jpg'),
      'image/object/bbox/xmin'  : dataset_util.float_list_feature(xmins),
      'image/object/bbox/xmax'  : dataset_util.float_list_feature(xmaxs),
      'image/object/bbox/ymin'  : dataset_util.float_list_feature(ymins),
      'image/object/bbox/ymax'  : dataset_util.float_list_feature(ymaxs),
      'image/object/class/text' : dataset_util.bytes_list_feature(classes_text),
      'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    tf_writer.write(tf_example.SerializeToString())

  tf_writer.close()

if __name__ == '__main__':
  main()