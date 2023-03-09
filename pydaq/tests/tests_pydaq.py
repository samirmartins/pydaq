from pydaq.send_data import Send_data
from pydaq.get_data import Get_data
from pydaq.step_response import Step_response
from pydaq.utils.base import Base
import pytest
from nidaqmx.constants import TerminalConfiguration
import serial
import matplotlib.pyplot as plt
import os

@pytest.fixture()
def send():
    return Send_data()

@pytest.fixture()
def get():
    return Get_data()

@pytest.fixture()
def step():
    return Step_response()

@pytest.fixture()
def base():
    return Base();

# Testing Constructor
def test_constructor_send(send):

    assert send.device == 'Dev1'
    assert send.channel == 'ao0'
    assert send.com_port == 'COM1'
    assert len(send.com_ports)>0

    print('\n[Send_data] Constructor method test passed')


def test_constructor_base(base):

    assert base.term_map['Diff'] ==  TerminalConfiguration.DIFF
    assert base.term_map['RSE'] == TerminalConfiguration.RSE
    assert base.term_map['NRSE'] == TerminalConfiguration.NRSE

    print('\n[Base] Constructor method test passed')


def test_constructor_get(get):

    assert get.device == 'Dev1'
    assert get.channel == 'ai0'
    assert get.com_port == 'COM1'
    assert len(get.com_ports)>0

    print('\n[Get_data] Constructor method test passed')

def test_constructor_step(step):

    assert step.device == 'Dev1'
    assert step.ai_channel == 'ai0'
    assert step.ao_channel == 'ao0'
    assert step.com_port == 'COM1'
    assert len(step.com_ports)>0

    print('\n[Step_response] Constructor method test passed')


# Testing Base
def test_path(send, get, step):

    assert send._check_path() is None
    assert get._check_path() is None
    assert step._check_path() is None

    print('\n[_check_path] - Test Passed!')


def test_updatable_plot(send, get, step):

    send._start_updatable_plot()
    get._start_updatable_plot()
    step._start_updatable_plot()

    assert send.fig._label == 'iter_plot'
    assert get.fig._label == 'iter_plot'
    assert step.fig._label == 'iter_plot'

    plt.close('all')

    print('\n[_start_updatable_plot] - Test Passed!')

def test_nidaq_step(step):

    step._nidaq_info()

    assert len(step.device_names) > 0
    assert len(step.device_categories) > 0
    assert len(step.device_type) > 0

    print('\n[Step_response - _nidaq_info] - Test Passed!')


def test_nidaq_send(send):

    send._nidaq_info()

    assert len(send.device_names)>0
    assert len(send.device_categories) > 0
    assert len(send.device_type) > 0

    print('\n[Send_data - _nidaq_info] - Test Passed!')

def test_nidaq_get(get):

    get._nidaq_info()

    assert len(get.device_names) > 0
    assert len(get.device_categories) > 0
    assert len(get.device_type) > 0

    print('\n[Get_data - _nidaq_info] - Test Passed!')

def test_save_data_get(get):

    get.path = os.getcwd()
    get._save_data([1,2,3], 'test.dat')
    assert os.path.isfile(os.path.join(get.path, 'test.dat')) == True
    os.remove(os.path.join(get.path, 'test.dat'))

    print('\n[Get_data - _save_data] - Test Passed!')

def test_save_data_send(send):

    send.path = os.getcwd()
    send._save_data([1,2,3], 'test.dat')
    assert os.path.isfile(os.path.join(send.path, 'test.dat')) == True
    os.remove(os.path.join(send.path, 'test.dat'))

    print('\n[Send_data - _save_data] - Test Passed!')

def test_save_data_step(step):

    step.path = os.getcwd()
    step._save_data([1, 2, 3], 'test.dat')
    assert os.path.isfile(os.path.join(step.path, 'test.dat')) == True
    os.remove(os.path.join(step.path, 'test.dat'))

    print('\n[Step_response - _save_data] - Test Passed!')