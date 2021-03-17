
#ifndef _PYWRAPPER_H
#define _PYWRAPPER_H

#include <Python.h>
#include "pyarraymodule.h"

#include <vector>

//added on 20201028
PyObject* marching_cubes_partial(PyArrayObject* arr, double isovalue);
PyObject* marching_cubes(PyArrayObject* arr, double isovalue);
PyObject* marching_cubes_func(PyObject* lower, PyObject* upper,
    int numx, int numy, int numz, PyObject* f, double isovalue);


#endif // _PYWRAPPER_H
