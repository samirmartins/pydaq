from PySide6.QtCore import QObject, Signal
from bitarray import bitarray
from random import randint
import numpy as np


class GuiSignals(QObject):
    returned = Signal(object)


class Signal:

    def __init__(self, prbs_bits: int, prbs_seed: int, prbs_var_tb: int = 1):
        self.prbs_types = {
            3: {"bit_1": 2, "bit_2": 1},  # size = 7
            4: {"bit_1": 3, "bit_2": 2},  # size = 15
            5: {"bit_1": 4, "bit_2": 2},  # size = 31
            6: {"bit_1": 5, "bit_2": 4},  # size = 63
            7: {"bit_1": 6, "bit_2": 5},  # size = 127
            9: {"bit_1": 8, "bit_2": 4},  # size = 511
            10: {"bit_1": 9, "bit_2": 6},  # size = 1_023
            11: {"bit_1": 10, "bit_2": 8},  # size = 2_047
            15: {"bit_1": 14, "bit_2": 13},  # size = 32_767
            17: {"bit_1": 16, "bit_2": 13},  # size = 131_071
            18: {"bit_1": 17, "bit_2": 10},  # size = 262_143
            20: {"bit_1": 19, "bit_2": 16},  # size = 1_048_575
            21: {"bit_1": 20, "bit_2": 18},  # size = 2_097_151
            22: {"bit_1": 21, "bit_2": 20},  # size = 4_194_303
            23: {"bit_1": 22, "bit_2": 17},  # size = 8_388_607
        }
        self.prbs_bits = prbs_bits
        self.prbs_seed = prbs_seed
        self.prbs_var_tb = prbs_var_tb
        self.sinal_prbs = self.generate_prbs()

    def generate_prbs(self) -> list:
        if self.prbs_bits >= max(self.prbs_types.keys()):
            self.prbs_bits = max(self.prbs_types.keys())
        else:
            self.prbs_bits = min(
                b for b in self.prbs_types.keys() if b >= self.prbs_bits
            )

        size = (2**self.prbs_bits) - 1
        bit_1 = self.prbs_types[self.prbs_bits]["bit_1"]
        bit_2 = self.prbs_types[self.prbs_bits]["bit_2"]
        start_value = randint(0, size - 1) if self.prbs_seed is None else self.prbs_seed
        start_value = int(min(max(start_value, 0), size - 1))

        bit_sequence = bitarray([start_value & 0x1])
        new_value = start_value
        for _ in range(size - 1):
            new_bit = ~((new_value >> bit_1) ^ (new_value >> bit_2)) & 0x1
            new_value = ((new_value << 1) + new_bit) & size
            if (new_value == start_value) or (new_value == size):
                return bit_sequence
            bit_sequence.append(bool(new_bit))

        # Repeating the signal to the correct size
        bit_sequence = [
            elem for elem in bit_sequence.tolist() for _ in range(self.prbs_var_tb)
        ]

        return bit_sequence

    def prbs_final(self, cycles, ao_max):
        """
        Extends or cut the prbs signal according to
        the number of cycles
        """
        len_prbs_signal = len(self.sinal_prbs)

        # Checks if Nt is less than the length of self.signal.sinal_prbs
        if cycles < len_prbs_signal:
            signal = self.sinal_prbs[:cycles]
            return [x * ao_max for x in signal]
        else:
            num_reps_int = cycles // len_prbs_signal
            num_left = cycles % len_prbs_signal
            signal = self.sinal_prbs * num_reps_int
            signal.extend(self.sinal_prbs[:num_left])
            return [x * ao_max for x in signal]
