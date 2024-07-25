args = {
        # 'MODEL_NAME': 'weight/RWKV-x060-World-1B6-v2.1-20240328-ctx4096', #模型文件的名字，pth结尾的权重文件。
        'MODEL_NAME': r'C:\Users\17506\Desktop\RWKV_Pytorch\weight\rwkv-test-epoch-1.pth', #模型文件的名字，pth结尾的权重文件。
        
        'vocab_size': 1024, #词表大小
        'device': "cuda", # 运行设备，可选'cpu','cuda','musa','npu'
        'onnx_opset': '18', # 非必要不要使用 <18 的值，会引起数值不稳定
        "parrallel": "True", # 是否使用并行计算
    }