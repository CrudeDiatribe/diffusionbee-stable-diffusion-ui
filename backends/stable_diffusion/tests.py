

import os 
import sys
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path , "../model_converter"))
model_interface_path = os.environ.get('MODEL_INTERFACE_PATH')  or "../stable_diffusion_tf_models" 
sys.path.append( os.path.join(dir_path , model_interface_path) )

from interface import ModelInterface
from stable_diffusion import StableDiffusion

p_14 = "/Users/divamgupta/.diffusionbee/downloads/sd-v1-4_fp16.tdict"

sd = StableDiffusion( ModelInterface , p_14 , model_name="sd_1x", callback=None)

inp = "./test_assets/scribble_turtle.png"


img = sd.generate(
        prompt="a tortoise" , 
        img_height=512, 
        img_width=512, 
        seed=678, 
        tdict_path=None,
        second_tdict_path="/Users/divamgupta/Downloads/just_control_sd15_scribble_fp16.tdict",
        batch_size=1,
        dtype=ModelInterface.default_float_type,
        scheduler='ddim',
        num_steps=25,
        input_image=inp,
        mode="controlnet" )


Image.fromarray(img[0]).show()




img = sd.generate(
        prompt="a tortoise" , 
        img_height=512, 
        img_width=512, 
        seed=678, 
        tdict_path=None,
        batch_size=1,
        dtype=ModelInterface.default_float_type,
        scheduler='ddim',
        input_image=inp,
        mode="txt2img" )


Image.fromarray(img[0]).show()





exit()


inp = "./test_assets/mmm.png"
mas = "./test_assets/ddd.png"




for cur_run_id in range(2):
    img = sd.generate(
        prompt="a haloween bedroom" , 
        img_height=512+64, 
        img_width=512-64, 
        seed=678, 
        tdict_path=None,
        batch_size=1,
        dtype=ModelInterface.default_float_type,
        scheduler='ddim',
        input_image_strength=0.4,
        input_image="bedroom2.jpg",
        mode="img2img" )
    Image.fromarray(img[0]).show()

for cur_run_id in range(2):
    img = sd.generate(
        prompt="modern disney a blue colored baby lion with lots of fur" , 
        img_height=512-64, 
        img_width=512, 
        seed=34, 
        num_steps=25,
        batch_size=1,
        tdict_path="/Users/divamgupta/.diffusionbee/custom_models/moDi-v1-pruned.tdict",
        dtype=ModelInterface.default_float_type,
        scheduler='ddim',
        mode="txt2img" )
    Image.fromarray(img[0]).show()

img = sd.generate(
    prompt="modern disney a blue colored baby lion with lots of fur" , 
    img_height=512, 
    img_width=512, 
    seed=34, 
    tdict_path=None,
    mode="txt2img" )
Image.fromarray(img[0]).show()


img = sd.generate(
    prompt="Face of red cat, high resolution, sitting on a park bench" , 
    img_height=512, 
    img_width=512, 
    seed=443136, 
    input_image=inp, 
    mask_image=mas,  
    tdict_path="/Users/divamgupta/Downloads/sd-v1-5-inpainting.tdict",
    mode="inpaint_15" )
Image.fromarray(img[0]).show()



