import sys
import xarray as xr
import numpy as np


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def simple_x_y():
    x_sample = [1, 2, 3, 4]
    x_arry = [x_sample] * 3
    # print(f'{x_arry=}')

    y1 = [1] * 4
    y2 = [2] * 4
    y3 = [3] * 4
    y_arry = [y1, y2, y3]
    # print(f'{y_arry=}')

    x = np.array(x_arry)
    print(f'{x=}')
    y = np.array(y_arry)
    print(f'{y=}')


if __name__ == '__main__':
    print(
        f'Xarray Example using python version {get_python_version()}, XArray version {xr.__version__} and NumPy {np.__version__}')
    simple_x_y()
