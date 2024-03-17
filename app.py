import gradio as gr
import os
import requests
import cmlapi

api_key = os.environ.get('CDSW_APIV2_KEY')
hostname = os.getenv('HOSTNAME')
domain = os.environ.get('CDSW_DOMAIN')
port = os.getenv('CDSW_APP_PORT')

# get model url via api
def get_model_url():
    api_url= f"https://{domain}"
    api_client=cmlapi.default_client(url=api_url,cml_api_key=api_key)
    model = api_client.list_all_models()
    access_key = model.models[0].access_key
    model_url = f"https://modelservice.{domain}/model?accessKey={access_key}"
    return model_url

def greet(text_input):
    query = '{"request":{"petal_length":"' + text_input + '"}}'
    model_url = get_model_url()
    r = requests.post(model_url, 
                      data=query, 
                      headers={'Content-Type': 'application/json', 
                               'Authorization': f'Bearer {api_key}'})
    return r.text

print(f"Launching demo at https://{hostname}.{domain}")

demo = gr.Interface(fn=greet, 
                    inputs="text",
                    outputs="text")

demo.launch(share=False,
            show_error=True,
            server_name='127.0.0.1',
            server_port=int(port))