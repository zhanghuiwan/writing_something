```
python main.py --mode variation --input_image path/to/image.jpg --prompt "A beautiful landscape" --image_count 4
```

```
2025-01-11 16:54:26,105 - INFO - Starting model loading...
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████| 2/2 [00:03<00:00,  1.77s/it]
You set `add_prefix_space`. The tokenizer needs to be converted from the slow tokenizers
D:\BaiduNetdiskDownload\qwen2vl-flux-main\flux\attention_processor.py:1645: FutureWarning: `FluxSingleAttnProcessor2_0` is deprecated and will be removed in version 0.32.0. `FluxSingleAttnProcessor2_0` is deprecated and will be removed in a future version. Please use `FluxAttnProcessor2_0` instead.
  deprecate("FluxSingleAttnProcessor2_0", "0.32.0", deprecation_message)
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████| 4/4 [03:48<00:00, 57.23s/it]
D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py:88: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  connector_state = torch.load(connector_path, map_location='cpu')
D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py:94: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  t5_embedder_state = torch.load(t5_embedder_path, map_location='cpu')
2025-01-11 16:59:49,515 - INFO - All models loaded successfully
INFO: Could not find files for the given pattern(s).
* Running on local URL:  http://127.0.0.1:7860
2025-01-11 16:59:50,997 - INFO - HTTP Request: GET http://127.0.0.1:7860/gradio_api/startup-events "HTTP/1.1 200 OK"
2025-01-11 16:59:51,019 - INFO - HTTP Request: HEAD http://127.0.0.1:7860/ "HTTP/1.1 200 OK"

To create a public link, set `share=True` in `launch()`.
2025-01-11 16:59:51,597 - INFO - HTTP Request: GET https://api.gradio.app/pkg-version "HTTP/1.1 200 OK"
2025-01-11 17:00:36,544 - INFO - Starting generation with prompt:  "A realistic  floor with one or two areas of water, "
            "water naturally spreading out and forming irregular shapes, "
2025-01-11 17:00:36,599 - INFO - Set random seed to: 0
2025-01-11 17:00:36,599 - INFO - Processing input image with Qwen2VL...
2025-01-11 17:00:36,600 - INFO - Moving Qwen2VL models to GPU...
2025-01-11 17:01:17,984 - INFO - Image processing completed
2025-01-11 17:01:17,986 - INFO - Computing text embeddings...
2025-01-11 17:01:20,532 - INFO - Text embeddings computed
2025-01-11 17:01:20,533 - INFO - Moving Transformer to GPU...
2025-01-11 17:03:10,575 - ERROR - Error during generation: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py", line 248, in generate
    transformer.to(DEVICE)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\diffusers\models\modeling_utils.py", line 1031, in to
    return super().to(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 1340, in to
    return self._apply(convert)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 927, in _apply
    param_applied = fn(param)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 1326, in convert
    return t.to(
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\queueing.py", line 624, in process_events
    response = await route_utils.call_process_api(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\route_utils.py", line 323, in call_process_api
    output = await app.get_blocks().process_api(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\blocks.py", line 2019, in process_api
    result = await self.call_function(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\blocks.py", line 1566, in call_function
    prediction = await anyio.to_thread.run_sync(  # type: ignore
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\_backends\_asyncio.py", line 2441, in run_sync_in_worker_thread
    return await future
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\_backends\_asyncio.py", line 943, in run
    result = context.run(func, *args)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\utils.py", line 865, in wrapper
    response = f(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\utils.py", line 865, in wrapper
    response = f(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py", line 285, in generate
    raise gr.Error(f"Generation failed: {str(e)}")
gradio.exceptions.Error: 'Generation failed: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)'2025-01-11 16:54:26,105 - INFO - Starting model loading...
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████| 2/2 [00:03<00:00,  1.77s/it]
You set `add_prefix_space`. The tokenizer needs to be converted from the slow tokenizers
D:\BaiduNetdiskDownload\qwen2vl-flux-main\flux\attention_processor.py:1645: FutureWarning: `FluxSingleAttnProcessor2_0` is deprecated and will be removed in version 0.32.0. `FluxSingleAttnProcessor2_0` is deprecated and will be removed in a future version. Please use `FluxAttnProcessor2_0` instead.
  deprecate("FluxSingleAttnProcessor2_0", "0.32.0", deprecation_message)
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████| 4/4 [03:48<00:00, 57.23s/it]
D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py:88: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  connector_state = torch.load(connector_path, map_location='cpu')
D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py:94: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  t5_embedder_state = torch.load(t5_embedder_path, map_location='cpu')
2025-01-11 16:59:49,515 - INFO - All models loaded successfully
INFO: Could not find files for the given pattern(s).
* Running on local URL:  http://127.0.0.1:7860
2025-01-11 16:59:50,997 - INFO - HTTP Request: GET http://127.0.0.1:7860/gradio_api/startup-events "HTTP/1.1 200 OK"
2025-01-11 16:59:51,019 - INFO - HTTP Request: HEAD http://127.0.0.1:7860/ "HTTP/1.1 200 OK"

To create a public link, set `share=True` in `launch()`.
2025-01-11 16:59:51,597 - INFO - HTTP Request: GET https://api.gradio.app/pkg-version "HTTP/1.1 200 OK"
2025-01-11 17:00:36,544 - INFO - Starting generation with prompt:  "A realistic  floor with one or two areas of water, "
            "water naturally spreading out and forming irregular shapes, "
2025-01-11 17:00:36,599 - INFO - Set random seed to: 0
2025-01-11 17:00:36,599 - INFO - Processing input image with Qwen2VL...
2025-01-11 17:00:36,600 - INFO - Moving Qwen2VL models to GPU...
2025-01-11 17:01:17,984 - INFO - Image processing completed
2025-01-11 17:01:17,986 - INFO - Computing text embeddings...
2025-01-11 17:01:20,532 - INFO - Text embeddings computed
2025-01-11 17:01:20,533 - INFO - Moving Transformer to GPU...
2025-01-11 17:03:10,575 - ERROR - Error during generation: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)
Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py", line 248, in generate
    transformer.to(DEVICE)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\diffusers\models\modeling_utils.py", line 1031, in to
    return super().to(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 1340, in to
    return self._apply(convert)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 900, in _apply
    module._apply(fn)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 927, in _apply
    param_applied = fn(param)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\torch\nn\modules\module.py", line 1326, in convert
    return t.to(
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\queueing.py", line 624, in process_events
    response = await route_utils.call_process_api(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\route_utils.py", line 323, in call_process_api
    output = await app.get_blocks().process_api(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\blocks.py", line 2019, in process_api
    result = await self.call_function(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\blocks.py", line 1566, in call_function
    prediction = await anyio.to_thread.run_sync(  # type: ignore
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\_backends\_asyncio.py", line 2441, in run_sync_in_worker_thread
    return await future
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\anyio\_backends\_asyncio.py", line 943, in run
    result = context.run(func, *args)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\utils.py", line 865, in wrapper
    response = f(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\python310\lib\site-packages\gradio\utils.py", line 865, in wrapper
    response = f(*args, **kwargs)
  File "D:\BaiduNetdiskDownload\qwen2vl-flux-main\app.py", line 285, in generate
    raise gr.Error(f"Generation failed: {str(e)}")
gradio.exceptions.Error: 'Generation failed: CUDA out of memory. Tried to allocate 90.00 MiB. GPU 0 has a total capacity of 15.99 GiB of which 0 bytes is free. Of the allocated memory 29.53 GiB is allocated by PyTorch, and 25.74 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation.  See documentation for Memory Management  (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables)'
```

