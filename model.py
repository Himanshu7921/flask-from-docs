import torch.nn as nn
import torch


class LinearLayer(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        super().__init__()
        self.weight = nn.Parameter(torch.rand(in_features, out_features))
        self.bias = nn.Parameter(torch.rand(out_features))

    def forward(self, x: torch.Tensor):
        return x @ self.weight + self.bias

class SoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x: torch.Tensor):
        exp_x = torch.exp(x)
        probs = exp_x / torch.sum(exp_x, dim = -1, keepdim=True)
        return probs
    
class Model(nn.Module):
    def __init__(self, x_dim: int, n_classes: int):
        super().__init__()
        self.linear_layer_1 = LinearLayer(x_dim, n_classes)
        self.softmax = SoftMax()

    def forward(self, x: torch.Tensor):
        logits = self.linear_layer_1(x)
        return self.softmax(logits)