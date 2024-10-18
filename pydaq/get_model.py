import os
import time
import warnings

import matplotlib.pyplot as plt
import matplotlib as mpl
import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import numpy as np
import serial
import serial.tools.list_ports
from pydaq.utils.base import Base

from pydaq.utils.signals import Signal
from math import floor

import pandas as pd
from sysidentpy.model_structure_selection import FROLS
from sysidentpy.basis_function._basis_function import Polynomial
from sysidentpy.metrics import root_relative_squared_error
from sysidentpy.utils.display_results import results
from sysidentpy.utils.plotting import plot_residues_correlation, plot_results
from sysidentpy.residues.residues_correlation import (
    compute_residues_autocorrelation,
    compute_cross_correlation,
)
from collections import Counter

from typing import Tuple

mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["axes.spines.top"] = False


def plot_combined_results(
    y: np.ndarray,
    yhat: np.ndarray,
    residuals: np.ndarray,
    cross_corr: np.ndarray,
    n: int = 100,
    title_main: str = "Free run simulation",
    title_residuals: str = "Residual Analysis - Autocorrelation",
    title_cross_corr: str = "Residual Analysis - Cross-Correlation",
    xlabel_main: str = "Samples",
    ylabel_main: str = r"y, $\hat{y}$",
    ylabel_residuals: str = "Correlation",
    ylabel_cross_corr: str = "Cross-Correlation",
    data_color: str = "#1f77b4",
    model_color: str = "#ff7f0e",
    marker: str = "o",
    model_marker: str = "*",
    linewidth: float = 1.5,
    figsize: Tuple[int, int] = (10, 18),
    style: str = "default",
    facecolor: str = "white",
) -> None:
    """Plot combined results with three stacked subplots.

    Parameters
    ----------
    y : np.ndarray
        True data values.
    yhat : np.ndarray
        Model predictions.
    residuals : np.ndarray
        Autocorrelation values of residuals.
    cross_corr : np.ndarray
        Cross-correlation values of residuals.
    n : int
        Number of samples to plot.
    title_main : str
        Title for the main plot.
    title_residuals : str
        Title for the residuals plot.
    title_cross_corr : str
        Title for the cross-correlation plot.
    xlabel_main : str
        Label for the x-axis of the main plot.
    ylabel_main : str
        Label for the y-axis of the main plot.
    ylabel_residuals : str
        Label for the y-axis of the residuals plot.
    ylabel_cross_corr : str
        Label for the y-axis of the cross-correlation plot.
    data_color : str
        Color for the data line.
    model_color : str
        Color for the model line.
    marker : str
        Marker style for the data line.
    model_marker : str
        Marker style for the model line.
    linewidth : float
        Line width for both lines.
    figsize : Tuple[int, int]
        Figure size (width, height).
    style : str
        Matplotlib style.
    facecolor : str
        Figure facecolor.
    """
    if len(y) == 0 or len(yhat) == 0:
        raise ValueError("Arrays must have at least 1 sample.")

    if len(residuals) == 0 or len(cross_corr) == 0:
        raise ValueError(
            "Residuals and cross-correlation arrays must have at least 1 sample."
        )

    # Set Matplotlib style and figure properties
    plt.style.use(style)
    plt.rcParams["axes.facecolor"] = facecolor

    # fig, axs = plt.subplots(4, 1, figsize=figsize, facecolor=facecolor)

    fig = plt.figure(figsize=figsize, facecolor=facecolor)
    gs = plt.GridSpec(2, 2, height_ratios=[2, 1])

    # Plot main results
    ax_main = fig.add_subplot(gs[0, :])
    ax_main.plot(
        y[:n], c=data_color, alpha=1, marker=marker, label="Data", linewidth=linewidth
    )
    ax_main.plot(
        yhat[:n], c=model_color, marker=model_marker, label="Model", linewidth=linewidth
    )
    ax_main.set_title(title_main, fontsize=18)
    ax_main.legend()
    ax_main.tick_params(labelsize=14)
    ax_main.set_xlabel(xlabel_main, fontsize=14)
    ax_main.set_ylabel(ylabel_main, fontsize=14)

    # Plot residuals autocorrelation
    ax_residuals = fig.add_subplot(gs[1, 0])
    ax_residuals.plot(residuals[0][:n], color=data_color)
    ax_residuals.axhspan(residuals[1], residuals[2], color="#ccd9ff", alpha=0.5, lw=0)
    ax_residuals.set_xlabel("Lag", fontsize=14)
    ax_residuals.set_ylabel(ylabel_residuals, fontsize=14)
    ax_residuals.tick_params(labelsize=14)
    ax_residuals.set_ylim([-1, 1])
    ax_residuals.set_title(title_residuals, fontsize=18)

    # Plot residuals cross-correlation
    ax_cross_corr = fig.add_subplot(gs[1, 1])
    ax_cross_corr.plot(cross_corr[0][:n], color=data_color)
    ax_cross_corr.axhspan(
        cross_corr[1], cross_corr[2], color="#ccd9ff", alpha=0.5, lw=0
    )
    ax_cross_corr.set_xlabel("Lag", fontsize=14)
    ax_cross_corr.set_ylabel(ylabel_cross_corr, fontsize=14)
    ax_cross_corr.tick_params(labelsize=14)
    ax_cross_corr.set_ylim([-1, 1])
    ax_cross_corr.set_title(title_cross_corr, fontsize=18)

    plt.tight_layout()
    plt.show()


class GetModel(Base):

    def __init__(
        self,
        device="Dev1",
        ao_channel="ao0",
        ai_channel="ai0",
        channel="ai0",
        terminal="Diff",
        com="COM1",
        ts=0.5,
        var_tb=1,
        ao_min=0,
        ao_max=5,
        session_duration=10.0,
        save=True,
        plot=True,
        degree=2,
        start_save_time=1,
        out_lag=3,
        inp_lag=3,
        num_info_values=6,
        estimator=None,
        ext_lsq=True,
        prbs_bits=6,
        prbs_seed=101,
        perc_value=30,
    ):

        super().__init__()
        self.device = device
        self.ai_channel = ai_channel
        self.ao_channel = ao_channel
        self.ao_min = ao_min
        self.ao_max = ao_max
        self.channel = channel
        self.session_duration = session_duration
        self.ts = ts
        self.var_tb = var_tb
        self.save = save
        self.plot = plot
        self.legend = ["Input", "Output"]
        self.degree = degree
        self.start_save_time = start_save_time
        self.out_lag = out_lag
        self.inp_lag = inp_lag
        self.num_info_val = num_info_values
        self.estimator = estimator
        self.ext_lsq = ext_lsq
        self.prbs_bits = prbs_bits
        self.prbs_seed = prbs_seed
        self.perc_value = perc_value
        self.final_model = None
        self.theta = None
        self.n_terms = None
        self.terminal = self.term_map[terminal]

        self.out_read = []
        self.time_var = []
        self.inp_read = []

        # Error flags
        self.error_path = False

        # COM ports
        self.com_ports = [i.description for i in serial.tools.list_ports.comports()]
        self.com_port = com  # Default COM port

        # Plot title
        self.title = None

        self._nidaq_info()

        # Defining default path
        self.path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

        # Arduino ADC resolution (in bits)
        self.arduino_ai_bits = 10

        # Arduino analog input max and min
        self.ard_ai_max, self.ard_ai_min = 5, 0

        # Value per bit - Arduino
        self.ard_vpb = (self.ard_ai_max - self.ard_ai_min) / (2**self.arduino_ai_bits)

        # Number of necessary cycles
        self.cycles = None

    def get_model_arduino(self):

        self.data = []
        self.time_var = []
        self.input, self.output = [], []

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        self.signal = Signal(self.prbs_bits, self.prbs_seed, self.var_tb)
        self.sinal = self.signal.prbs_final(cycles=self.cycles, ao_max=self.ao_max)
        sinal = np.array(self.sinal)

        self._open_serial()
        time.sleep(2)

        self.data_send = [b"1" if i == 5 else b"0" for i in sinal]

        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Geting Data. Arduino, Port: {self.com_port}"
            self._start_updatable_plot()

        for k in range(self.cycles):
            st = time.time()

            self.ser.reset_input_buffer()  # Reseting serial input buffer
            self.ser.write(self.data_send[k])

            temp = int(self.ser.read(14).split()[-2].decode("UTF-8")) * self.ard_vpb

            self.out_read.append(temp)
            self.time_var.append(k * self.ts)
            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break
                # Updating data values
                self._update_plot(
                    [self.time_var, self.time_var],
                    [sinal[0 : k + 1], self.out_read],
                    2,
                )
            print(f"Iteration: {k} of {self.cycles-1}")

            et = time.time()

            try:
                time.sleep(self.ts + (st - et))
            except:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )
        self.ser.write(b"0")
        self.ser.close()

        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.sinal, "input.dat")
            self._save_data(self.out_read, "output.dat")
            print("\nData saved ...")

        # adapts the time at which data starts to be saved to obtain the model
        time_save = int(self.start_save_time / self.ts)

        data_x = sinal
        data_y = np.array(self.out_read)
        perc_index = floor(data_x.shape[0] - data_x.shape[0] * (self.perc_value / 100))

        x_train, x_valid = (
            data_x[time_save:perc_index].reshape(-1, 1),
            data_x[perc_index:].reshape(-1, 1),
        )
        y_train, y_valid = (
            data_y[time_save:perc_index].reshape(-1, 1),
            data_y[perc_index:].reshape(-1, 1),
        )

        basis_function = Polynomial(degree=self.degree)

        model = FROLS(
            order_selection=True,
            n_info_values=self.num_info_val,
            extended_least_squares=self.ext_lsq,
            ylag=[i + 1 for i in range(self.inp_lag)],
            xlag=[i + 1 for i in range(self.out_lag)],
            info_criteria="aic",
            estimator=self.estimator,
            basis_function=basis_function,
        )
        model.fit(X=x_train, y=y_train)
        yhat = model.predict(X=x_valid, y=y_valid)
        rrse = root_relative_squared_error(y_valid, yhat)
        print(f"Root relative squared error: {rrse}")

        r = pd.DataFrame(
            results(
                model.final_model,
                model.theta,
                model.err,
                model.n_terms,
                err_precision=8,
                dtype="sci",
            ),
            columns=["Regressors", "Parameters", "ERR"],
        )
        print(r)
        self.acquired_model = model
        self.final_model = model.final_model
        self.theta = model.theta
        self.n_terms = model.n_terms

        ee = compute_residues_autocorrelation(y_valid, yhat)
        x1e = compute_cross_correlation(y_valid, yhat, x_valid)

        plot_combined_results(
            y=y_valid,
            yhat=yhat,
            residuals=ee,
            cross_corr=x1e,
            title_main="Free run simulation",
            title_residuals="Residues",
            title_cross_corr="Residues",
            xlabel_main="Samples",
            ylabel_main=r"y, $\hat{y}$",
            ylabel_residuals="$e^2$",
            ylabel_cross_corr="$x_1e$",
            data_color="#1f77b4",
            model_color="#ff7f0e",
            marker="o",
            model_marker="*",
            linewidth=1.5,
        )
        self.show_results(r)

    def get_model_nidaq(self):

        self.data = []
        self.time_var = []
        self.input, self.output = [], []

        self._check_path()
        self.cycles = int(np.floor(self.session_duration / self.ts)) + 1

        self.signal = Signal(self.prbs_bits, self.prbs_seed, self.var_tb)
        self.sinal = self.signal.prbs_final(cycles=self.cycles, ao_max=self.ao_max)
        sinal = np.array(self.sinal)

        task_ao = nidaqmx.Task()
        task_ai = nidaqmx.Task()

        task_ao.ao_channels.add_ao_voltage_chan(
            self.device + "/" + self.ao_channel,
            min_val=float(self.ao_min),
            max_val=float(self.ao_max),
        )

        task_ai.ai_channels.add_ai_voltage_chan(
            self.device + "/" + self.channel, terminal_config=self.terminal
        )

        # task_ao.start()
        # task_ai.start()

        self.data_send = sinal
        if self.plot:  # If plot, start updatable plot
            self.title = f"PYDAQ - Geting Data (NIDAQ). {self.device}, {self.channel}"
            self._start_updatable_plot()

        task_ao.write(self.ao_min)
        for k in range(self.cycles):
            st = time.time()

            task_ao.write(self.data_send[k])
            temp = task_ai.read()

            self.out_read.append(temp)
            self.inp_read.append(self.data_send[k])
            self.time_var.append(k * self.ts)
            if self.plot:

                # Checking if there is still an open figure. If not, stop the for loop.
                try:
                    plt.get_figlabels().index("iter_plot")
                except BaseException:
                    break

                # Updating data values
                self._update_plot(
                    [self.time_var, self.time_var],
                    [sinal[0 : k + 1], self.out_read],
                    2,
                )

            print(f"Iteration: {k} of {self.cycles-1}")

            et = time.time()

            try:
                time.sleep(self.ts + (st - et))

            except:
                warnings.warn(
                    "Time spent to append data and update interface was greater than ts. "
                    "You CANNOT trust time.dat"
                )

        # Turning off the output at the end
        task_ao.write(0)
        # self.out_read.insert(0, self.out_read[0])
        # self.out_read.pop()
        task_ao.close()
        task_ai.close()

        if self.save:
            print("\nSaving data ...")
            # Saving time_var and data
            self._save_data(self.time_var, "time.dat")
            self._save_data(self.inp_read, "input.dat")
            self._save_data(self.out_read, "output.dat")
            print("\nData saved ...")

        # adapts the time at which data starts to be saved to obtain the model
        time_save = int(self.start_save_time / self.ts)

        data_y = np.array(self.out_read)
        data_x = sinal.astype(data_y.dtype)

        perc_index = floor(data_x.shape[0] - data_x.shape[0] * (self.perc_value / 100))

        x_train, x_valid = (
            data_x[time_save:perc_index].reshape(-1, 1),
            data_x[perc_index:].reshape(-1, 1),
        )
        y_train, y_valid = (
            data_y[time_save:perc_index].reshape(-1, 1),
            data_y[perc_index:].reshape(-1, 1),
        )

        basis_function = Polynomial(degree=self.degree)

        model = FROLS(
            order_selection=True,
            n_info_values=self.num_info_val,
            extended_least_squares=self.ext_lsq,
            ylag=[i + 1 for i in range(self.inp_lag)],
            xlag=[i + 1 for i in range(self.out_lag)],
            info_criteria="aic",
            estimator=self.estimator,
            basis_function=basis_function,
        )
        model.fit(X=x_train, y=y_train)
        yhat = model.predict(X=x_valid, y=y_valid)
        rrse = root_relative_squared_error(y_valid, yhat)
        print(f"Root relative squared error: {rrse}")

        r = pd.DataFrame(
            results(
                model.final_model,
                model.theta,
                model.err,
                model.n_terms,
                err_precision=8,
                dtype="sci",
            ),
            columns=["Regressors", "Parameters", "ERR"],
        )
        print(r)
        self.acquired_model = model
        self.final_model = model.final_model
        self.theta = model.theta
        self.n_terms = model.n_terms

        ee = compute_residues_autocorrelation(y_valid, yhat)
        x1e = compute_cross_correlation(y_valid, yhat, x_valid)

        plot_combined_results(
            y=y_valid,
            yhat=yhat,
            residuals=ee,
            cross_corr=x1e,
            title_main="Free run simulation",
            title_residuals="Residues",
            title_cross_corr="Residues",
            xlabel_main="Samples",
            ylabel_main=r"y, $\hat{y}$",
            ylabel_residuals="$e^2$",
            ylabel_cross_corr="$x_1e$",
            data_color="#1f77b4",
            model_color="#ff7f0e",
            marker="o",
            model_marker="*",
            linewidth=1.5,
        )
        self.show_results(r)

    def show_results(self, results_dataframe):
        model_string = "y_k = "
        r = results_dataframe
        line_control = 0
        string_list = []
        for ind in r.index:
            if r.iat[ind, 0] == "1":
                model_string += f"{float(r.iat[ind,1]):.4f}"
            else:
                model_string += f"{float(r.iat[ind,1]):.4f}*{r.iat[ind,0]}"

            if len(r.index) != ind + 1:
                if float(r.iat[ind + 1, 1]) >= 0:
                    model_string += "+"
            line_control += 1
            if line_control % 2 == 0:
                string_list.append(model_string)
                model_string = ""
        if line_control % 2 != 0:
            string_list.append(model_string)

        for cont, i in enumerate(string_list):
            string_list[cont] = i.replace("(", "_{")
            string_list[cont] = string_list[cont].replace(")", "}")
            string_list[cont] = string_list[cont].replace("*", " ")
            string_list[cont] = string_list[cont].replace("x1", "x")

        fig, ax = plt.subplots()
        aux_pos = 0
        ax.axis("off")
        ax.text(0.35, 1, "Model equation", fontsize=18, ha="left")

        if (
            self.acquired_model.basis_function.degree == 1
            and 0 not in self.acquired_model.final_model
        ):
            numerator_string = ""
            denominator_string = "1"
            for i in range(self.acquired_model.n_terms):
                if np.max(self.acquired_model.final_model[i]) < 1:
                    tmp_regressor_str = str(1)
                else:
                    regressor_dic = Counter(self.acquired_model.final_model[i])
                    regressor_string = []
                    for j in range(len(list(regressor_dic.keys()))):
                        regressor_key = list(regressor_dic.keys())[j]
                        if regressor_key < 1:
                            regressor_Z_transformed = ""
                        else:
                            expoent_string = str(
                                -int(
                                    regressor_key
                                    - np.floor(regressor_key / 1000) * 1000
                                )
                            )
                            if int(regressor_key / 1000) < 2:
                                if self.acquired_model.theta[i][0] > 0:
                                    regressor_Z_transformed = f"\\,-\\,{self.acquired_model.theta[i][0]:.4f}\\,z^{{{expoent_string}}}"
                                else:
                                    regressor_Z_transformed = f"\\,+\\,{-self.acquired_model.theta[i][0]:.4f}\\,z^{{{expoent_string}}}"
                                denominator_string += regressor_Z_transformed
                            else:
                                if (
                                    numerator_string
                                    and self.acquired_model.theta[i][0] > 0
                                ):
                                    numerator_string += "\\,+\\,"
                                    regressor_Z_transformed = f"{self.acquired_model.theta[i][0]:.4f}\\,z^{{{expoent_string}}}"
                                    numerator_string += regressor_Z_transformed
                                else:
                                    regressor_Z_transformed = f"{self.acquired_model.theta[i][0]:.4f}\\,z^{{{expoent_string}}}"
                                    numerator_string += regressor_Z_transformed

            latex_eq = "H[z]\\,=\\,\\frac{Y[z]}{X[z]}\\,=\\,"

            if numerator_string:
                latex_eq += f"\\frac{{{numerator_string}}}{{{denominator_string}}}"
            else:
                latex_eq += f"\\frac{{1}}{{{denominator_string}}}"

            string_list.append("")
            string_list.append(latex_eq)

        for i in range(len(string_list)):
            if string_list[i]:
                ax.text(
                    0.15 + aux_pos * 0.1,
                    0.7 - i * 0.07,
                    rf"${string_list[i]}$",
                    fontsize=15,
                    ha="left",
                )
                aux_pos = 1

            ax.axis("off")

        plt.show()
