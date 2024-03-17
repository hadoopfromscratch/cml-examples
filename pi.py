import random
import math
import cml.models_v1 as models
import mlflow

ITERATIONS = 1000

def estimate_pi(n_iterations):
    """Returns an estimate of pi computed using Monte-Carlo integration."""
    successes = 0
    for _ in range(n_iterations):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        if x ** 2 + y ** 2 < 1:
            successes += 1
    return 4.0 * successes / n_iterations
  
def cost_func(est_pi):
    return (math.pi - est_pi)**2

mlflow.set_experiment("PiXperiment")
with mlflow.start_run():
    mlflow.log_param("Iterations", ITERATIONS)
    pi = estimate_pi(ITERATIONS)
    mlflow.log_metric("Pi", pi)
    mlflow.log_metric("Square Error", cost_func(pi))
    print(pi)
