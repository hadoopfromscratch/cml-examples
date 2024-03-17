import pickle
import cml.models_v1 as models
import cml.metrics_v1 as metrics

model = pickle.load(open('model.pkl', 'rb'))

@models.cml_model(metrics=True)
def predict(args):
  petal_length = float(args.get('petal_length'))
  result = model.predict([[petal_length]])
  metrics.track_metric("petal_length", petal_length)
  metrics.track_metric("petal_width", result[0][0])
  return result[0][0]
