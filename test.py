# Importing PYDAQ
from pydaq.get_model import GetModel

# Defining parameters
device_name = "Dev1"
ao_channel = "ao0"
ai_channel = "ai0"
channel = "ai0"
terminal = "Diff"
ao_min = 0
ao_max = 5
session_duration_in_s = 10
sample_period_in_s = 0.5
save_data = True
plot_data = "realtime"

# system identification parameters
degree = 2
start_save_time_in_s = 0
out_lag = 2
inp_lag = 2
num_info_val = 6
estimator = "least_squares"
ext_lsq = True
perc_value_to_train_the_model = 15

# PRBS input parameters
prbs_bits = 6
prbs_seed = 100
var_tb = 1

# Class GetModel
g = GetModel(
    device=device_name,
    ai_channel=ai_channel,
    ao_channel=ao_channel,
    ao_min=ao_min,
    ao_max=ao_max,
    channel=channel,
    terminal=terminal,
    session_duration= session_duration_in_s,
    ts= sample_period_in_s,
    save= save_data,
    plot_mode= plot_data,
    degree=degree,
    start_save_time=start_save_time_in_s,
    out_lag=out_lag,
    inp_lag=inp_lag,
    num_info_values=num_info_val,
    estimator=estimator,
    ext_lsq=ext_lsq,
    perc_value=perc_value_to_train_the_model,
    prbs_bits=prbs_bits,
    prbs_seed=prbs_seed,
    var_tb=var_tb,
)

# Method get_model_nidaq
g.get_model_nidaq()