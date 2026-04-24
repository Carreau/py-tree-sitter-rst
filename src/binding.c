#include <Python.h>

/* Forward declaration — avoids pulling in tree_sitter/parser.h */
typedef struct TSLanguage TSLanguage;
const TSLanguage *tree_sitter_rst(void);

static PyObject *binding_language(PyObject *self, PyObject *args) {
    return PyCapsule_New((void *)tree_sitter_rst(), "tree_sitter.Language", NULL);
}

static PyMethodDef methods[] = {
    {"language", binding_language, METH_NOARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "_rst", NULL, -1, methods,
};

PyMODINIT_FUNC PyInit__rst(void) { return PyModule_Create(&module); }
