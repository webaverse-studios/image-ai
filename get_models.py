import os
import wget
import json

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
INVOKEAI_LOCAL_PATH = os.path.join(ROOT_DIR, 'InvokeAI')
INVOKEAI_MODELS_PATH = os.path.join(INVOKEAI_LOCAL_PATH, 'models', 'ldm', 'stable-diffusion-v1')

# Get model list from models.json
with open(os.path.join(ROOT_DIR, 'models.json')) as f:
    models = json.load(f)


# Create stable-diffusion-v1 directory
if not os.path.exists(INVOKEAI_MODELS_PATH):
    os.makedirs(INVOKEAI_MODELS_PATH)

# Get models from S3
for model in models["model_list"]:

    model_path = os.path.join(INVOKEAI_MODELS_PATH, model["filename"])

    if not os.path.exists(model_path):
        print("")
        print(f'Downloading {model["filename"]}...')
        wget.download(models["s3_url"] + model["filename"], out=model_path)
        print("")
        print(f'Download finished: {model_path}')
        print("")

        # Add model to InvokeAI config
        model_config_text = f"{model['name']}:\n" + \
                            f"   config:  configs/stable-diffusion/v1-inference.yaml\n" + \
                            f"   weights: models/ldm/stable-diffusion-v1/{model['filename']}\n" + \
                            f"   description: no desc\n" + \
                            f"   width: 512\n" + \
                            f"   height: 512\n"

        # Append to config file (InvokeAI/configs/models.yaml)
        with open(os.path.join(INVOKEAI_LOCAL_PATH, 'configs', 'models.yaml'), 'a') as f:
            f.write(model_config_text)
    else:
        print(f'Found existing checkpoint. Skipping: {model["filename"]}')