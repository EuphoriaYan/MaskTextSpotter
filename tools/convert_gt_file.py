
import os
import sys

import json
import argparse
from tqdm import tqdm


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_gt', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    with open(args.input_gt, 'r', encoding='utf-8') as fp:
        for line in tqdm(fp):
            image_name, image_json = line.strip().split('\t')
            image_json = json.loads(image_json)
            text_list = image_json['text_list']
            text_bbox_list = image_json['text_bbox_list']
            with open(os.path.join(args.output_path, image_name+'.txt'), 'w', encoding='utf-8') as output_fp:
                for bbox, text in zip(text_bbox_list, text_list):
                    left, top, right, bottom = map(str, bbox)
                    line_list = [left, top, right, top, right, bottom, left, bottom, ''.join(text)]
                    output_fp.write(','.join(line_list)+'\n')