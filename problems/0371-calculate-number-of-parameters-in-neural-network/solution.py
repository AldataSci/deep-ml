# Cell 1
def calculate_parameters(layers):
    total_params = 0

    for layer in layers:
        layer_type = layer['type']
        has_bias = layer.get('bias', True)  # Defaults to True when 'bias' is omitted

        if layer_type == 'dense':
            weights = layer['input_size'] * layer['output_size']
            bias = layer['output_size'] if has_bias else 0

        elif layer_type == 'conv2d':
            weights = layer['in_channels'] * layer['out_channels'] * layer['kernel_size'] * layer['kernel_size']
            bias = layer['out_channels'] if has_bias else 0

        else:
            raise ValueError(f"Unsupported layer type: {layer_type}")

        total_params += weights + bias

    return total_params