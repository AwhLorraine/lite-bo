import os
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(0, os.getcwd())

from litebo.optimizer.generic_smbo import SMBO
from litebo.benchmark.objective_functions.synthetic import BraninCurrin


prob = BraninCurrin()
bo = SMBO(prob.evaluate, prob.config_space,
          advisor_type='mcadvisor',
          task_id='mcehvi',
          num_objs=prob.num_objs,
          num_constraints=prob.num_constraints,
          acq_type='mcehvi',
          ref_point=prob.ref_point,
          max_runs=100, random_state=2)
bo.run()

hvs = bo.get_history().hv_data
log_hv_diff = np.log10(prob.max_hv - np.asarray(hvs))

pf = np.asarray(bo.get_history().get_pareto_front())
plt.scatter(pf[:, 0], pf[:, 1])
# plt.plot(log_hv_diff)
# plt.show()
