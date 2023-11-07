# Leap Services

This document outlines the parameters to pass into Leap Services in workflows.

## SDXL Parameters

- **`prompt`**: `str` or `List[str]`, optional - The prompt or prompts to guide the image generation.
- **`prompt_2`**: `str` or `List[str]`, optional - Secondary prompts for tokenizer_2 and text_encoder_2.
- **`height`**: `int`, optional - The height in pixels of the generated image, defaults to 1024.
- **`width`**: `int`, optional - The width in pixels of the generated image, defaults to 1024.
- **`num_inference_steps`**: `int`, optional - The number of denoising steps, defaults to 50.
- **`denoising_end`**: `float`, optional - Fraction of the denoising process to be completed, between 0.0 and 1.0.
- **`guidance_scale`**: `float`, optional - Classifier-Free Diffusion Guidance scale, defaults to 5.0. _Use with caution; high values can significantly affect image quality._
- **`negative_prompt`**: `str` or `List[str]`, optional - Prompts not to guide the image generation.
- **`negative_prompt_2`**: `str` or `List[str]`, optional - Secondary set of negative prompts.
- **`num_images_per_prompt`**: `int`, optional - The number of images to generate per prompt, defaults to 1.
- **`eta`**: `float`, optional - DDIM scheduler parameter, defaults to 0.0. _Adjust carefully as this may impact the generation process._
- **`latents`**: `torch.FloatTensor`, optional - Pre-generated noisy latents for image generation. _Using custom latents can yield unpredictable results._
- **`prompt_embeds`**: `torch.FloatTensor`, optional - Pre-generated text embeddings.
- **`negative_prompt_embeds`**: `torch.FloatTensor`, optional - Pre-generated negative text embeddings.
- **`pooled_prompt_embeds`**: `torch.FloatTensor`, optional - Pre-generated pooled text embeddings.
- **`negative_pooled_prompt_embeds`**: `torch.FloatTensor`, optional - Pre-generated negative pooled text embeddings.
- **`guidance_rescale`**: `float`, optional - Guidance rescale factor, defaults to 0.0. _Use with caution; may impact image fidelity._
- **`crops_coords_top_left`**: `Tuple[int]`, optional - Coordinates for cropping the image, defaults to (0, 0).
- **`target_size`**: `Tuple[int]`, optional - The target size of the generated image, defaults to (1024, 1024).
- **`negative_original_size`**: `Tuple[int]`, optional - Negative conditioning based on image resolution. _Use at your own risk; this can alter generation logic._
- **`negative_crops_coords_top_left`**: `Tuple[int]`, optional - Negative conditioning based on crop coordinates. _Use at your own risk; this can alter generation logic._
- **`negative_target_size`**: `Tuple[int]`, optional - Negative conditioning based on target image resolution. _Use at your own risk; this can alter generation logic._
- **`callback_on_step_end`**: `Callable`, optional - Function called at the end of each denoising step. _This is an advanced feature that may affect the generation process._
- **`callback_on_step_end_tensor_inputs`**: `List`, optional - Tensor inputs for the `callback_on_step_end` function. _This should be used with a thorough understanding of the tensors involved._

## Musicgen Parameters

- **`prompt`**: `str` - Text to guide the music generation.
- **`duration`**: `int`, optional - Duration of the generated music piece, defaults to 10 seconds. _This has a maximum of 60 seconds._
- **`format`**: `str`, optional - The format of the generated music, defaults to "wav".
- **`melody`**: `str`, optional - Melodic guide for the music generation.