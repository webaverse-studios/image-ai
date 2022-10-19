<h1>Webaverse ImageAI</h1>

<h3>GET Request:</h3>
<code>http://&lthostname&gt;/image?prompt=&lt;YOUR_PROMPT&gt;&model=&lt;YOUR_MODEL&gt;</code>

<h3>Needs to be re-implemented in FastAPI code: POST Request (full SD parameters):</h3> 
<code>http://&lthostname&gt;/api</code>
<ul>
  <li>
    model <code>default: stable-diffusion_1-4</code>
  </li>
  <li>
    prompt <code>default: "an astronaut riding a horse"</code>
  </li>
  <li>
    iterations <code>default: 50</code>
  </li>
  <li>
    steps <code>default: 1</code>
  </li>
  <li>
    seed <code>default: random()</code>
  </li>
  <li>
    cfg_scale <code>default: 7.5</code>
  </li>
  <li>
    seamless <code>makes output tileable. default: False</code>
  </li>
  <li>
    init_img  <code>for img2img.</code>
  </li>
  <li>
    init_mask <code>for inpainting</code>
  </li>
  <li>
    strength <code>default: 0.75</code>
  </li>
</ul>

<h3>Adding a model</h3>
<ol>
<li>Update configs/models.yaml:<br>
<pre>
models.json example
{
    "name": "waifu_diffusion_1-3",
    "filename": "wd-v1-3-float16.ckpt"
}
Name: the name that will be used to refer to the models in the request and within InvokeAI.
Filename: the filename of the model in S3. Keep the default Hugging Face filename.
</li>
<li>
<p>Run get_models.py to get the checkpoints from S3 and add them to InvokeAI's builtin configs.</p>
</li>
</ol>