# pipeline/integration_pipeline.py

def full_run(image_path, text, model):
    from pipeline.prepare_data_pipeline import prepare_sample
    from pipeline.inference_pipeline import run_inference

    image, text = prepare_sample(image_path, text)
    input_data = (image, text)
    output = run_inference(model, input_data)
    return output
