import logging
import json

import numpy as np
import torch
import torch.nn.functional as F
from ts.torch_handler.base_handler import BaseHandler
from ts.utils.util import map_class_to_label

logger = logging.getLogger(__name__)


class Classifier(BaseHandler):
    def preprocess(self, data):
        line = data[0]
        json_data = json.dumps(line)
        json_data = json.loads(json_data)['body']
        input_data, rows, cols = json_data['data'], json_data['rows'], json_data['cols']
        input_data = np.array(input_data, dtype=np.float32).reshape(-1, rows, cols)
        input_tensor = torch.as_tensor(input_data, device=self.device)
        return input_tensor, input_data

    def inference(self, data, *args, **kwargs):
        input_tensor, _ = data
        return super().inference(input_tensor)

    def postprocess(self, data):
        data = F.softmax(data, dim=1)
        data = data.tolist()
        return map_class_to_label(data, self.mapping)
