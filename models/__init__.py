# ----------------------------------------------------------------------------------------------
# CoFormer Official Code
# Copyright (c) Junhyeong Cho. All Rights Reserved 
# Licensed under the Apache License 2.0 [see LICENSE for details]
# ----------------------------------------------------------------------------------------------
# Modified from DETR (https://github.com/facebookresearch/detr)
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved [see LICENSE for details]
# ----------------------------------------------------------------------------------------------

from .gsrformer import build_encoder_transformer
from .gsrformer import build_decoder_transformer

def build_encoder_model(args):
    return build_encoder_transformer(args)
def build_decoder_model(args):
    return build_decoder_transformer(args)