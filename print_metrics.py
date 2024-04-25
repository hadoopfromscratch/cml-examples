import os
import pprint
import cml.metrics_v1 as metrics
import matplotlib.pyplot as plt
import cmlapi

# get model crn via api
api_key = os.environ.get('CDSW_APIV2_KEY')
domain = os.environ.get('CDSW_DOMAIN')
api_url= f"https://{domain}"
api_client=cmlapi.default_client(url=api_url,cml_api_key=api_key)
model = api_client.list_all_models()
crn = model.models[-1].crn

# print metrics
data = metrics.read_metrics(model_crn=crn)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(data)

# plot metrics
petal_width = [item['metrics']['petal_width'] for item in data['metrics']]
petal_length = [item['metrics']['petal_length'] for item in data['metrics']]
plt.scatter(x=petal_width, y=petal_length)
