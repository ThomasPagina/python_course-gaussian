import pytest
"""Test for normal.py
    Authors: Jamie Dimmick, Alex Harper
"""
from normal import (  # replace 'normal' with real module name, leave out .py
    mean, my_sum, median, std_dev, skewness, kurtosis,
    jarque_bera_statistic, p_value_approximation, percentage_in_1std,
    percentage_in_2std, percentage_in_3std, distance_mean_median
)

assert median([-5, -1, -3]) == -3
assert round(jarque_bera_statistic([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 0.57
assert round(std_dev([-5, -10, -15]), 2) == 4.08
assert my_sum([-1, -2, -3]) == -6
assert mean([10]) == 10
assert round(percentage_in_2std([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 1.0
assert my_sum([1.1, 2.2, 3.3]) == 6.6
assert round(std_dev([2, 4, 4, 4, 5, 5, 7, 9]), 2) == 2.0
assert distance_mean_median([1.1, 2.2, 3.3, 4.4, 5.5]) == 0
assert mean([-1, -2, -3, -4]) == -2.5
assert round(percentage_in_3std([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 1.0
assert round(kurtosis([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 1.77
assert mean([1.5, 2.5, 3.5]) == 2.5
assert round(p_value_approximation([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) >= 0
assert my_sum([1, 2, 3, 4]) == 10
assert median([1, 2, 3, 4]) == 2.5
assert round(percentage_in_1std([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 0.56
assert mean([]) == 0
assert round(skewness([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2) == 0.0
assert distance_mean_median([-1, -2, -3, -4, -5]) == 0
assert distance_mean_median([1, 2, 3, 4, 5]) == 0
assert my_sum([]) == 0
assert round(std_dev([1.2, 3.4, 5.6]), 2) == 1.80
assert mean([1, 2, 3, 4, 5]) == 3
assert median([2.3, 3.1, 4.8]) == 3.1
assert median([10]) == 10
assert distance_mean_median([1, 2, 3, 4, 10]) == 1.0

with pytest.raises(TypeError):
    my_sum(['X', 'V'])
with pytest.raises(TypeError):
    mean(['I', 'II', 'III'])
with pytest.raises(TypeError):
    distance_mean_median(['X', 'L', 'C'])
