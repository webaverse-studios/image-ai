from typing import Union, Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ldm.generate import Generate
from omegaconf import OmegaConf
import random


class Generation(BaseModel):
    model: Optional[str] = "stable-diffusion_1-4"
    prompt: Optional[str] = "An astronaut riding a horse."
    iterations: Optional[int] = 1
    steps: Optional[int] = 50
    seed: Optional[int] = random.randint(1, 99999)
    cfg_scale: Optional[float] = 7.5
    seamless: Optional[bool] = False
    init_img: Optional[str] = None
    init_mask: Optional[str] = None
    strength: Optional[float] = 0.75


app = FastAPI()

@app.get("/")
async def root(generation: Generation = None):

    if not generation:
        generation = Generation()

    # Get models and configs
    model = generation.model
    models = OmegaConf.load("configs/models.yaml")
    width = models[model].width
    height = models[model].height
    config = models[model].config
    weights = models[model].weights

    arg_dict = {
        "prompt": generation.prompt,
        "iterations": generation.iterations,
        "steps": generation.steps,
        "seed": generation.seed,
        "cfg_scale": generation.cfg_scale,
        "width": width,
        "height": height,
        "seamless": generation.seamless,
        "init_img": generation.init_img, # For img2img
        "init_mask": generation.init_mask, # For inpainting
        "strength": generation.strength
    }

    generation = Generate(weights=weights, config=config)
    output = generation.prompt2png(**arg_dict, outdir="outputs/web_out")

    #return send_file(output[0][0], mimetype="image/png")
    #return "something"
    return FileResponse(output[0][0])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="216.153.51.112", port=8001, log_level="debug")