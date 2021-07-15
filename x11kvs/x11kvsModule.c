#include <Python.h>
//#include "python3.6/Python.h"
#include "algo/x11/x11kvs-gate.h"

extern const uint32_t HASHX11KVS_CACHE_SIZE_6;

static PyObject *method_hash(PyObject *self, PyObject *args) {
    PyBytesObject *input;
 
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;

    Py_INCREF(input);
    char *output = PyMem_Malloc(32);
    uint8_t *cache = PyMem_Calloc(sizeof(uint8_t), HASHX11KVS_CACHE_SIZE_6);

    init_x11kv_ctx();
    x11kvs_hash(output, (char *)PyBytes_AsString((PyObject *)input), cache);
 
    Py_DECREF(input);

    PyObject *value = Py_BuildValue("y#", output, 32);

    PyMem_Free(output);
    return value;
}


static PyMethodDef x11kvsMethods[] = {
    {"hash", method_hash, METH_VARARGS, "x11kvs hash"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef x11kvsmodule = {
    PyModuleDef_HEAD_INIT,
    "x11kvs",
    "Python x11kvs module. ",
    -1,
    x11kvsMethods
};

PyMODINIT_FUNC PyInit_x11kvs(void) {
    return PyModule_Create(&x11kvsmodule);
}
