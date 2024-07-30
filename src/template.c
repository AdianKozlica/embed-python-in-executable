#include <Python.h>

int main() {
    Py_Initialize();

    if (!Py_IsInitialized()) {
        fprintf(stderr, "Failed to initialize Python interpreter\n");
        return 1;
    }

    const char* code = CODE GOES HERE;

    PyObject* compiled_code = Py_CompileString(code, "<string>", Py_file_input);

    if (compiled_code == NULL) {
        PyErr_Print();
        Py_Finalize();
        return 1;
    }

    PyObject* globals = PyDict_New();
    PyObject* locals = PyDict_New();
   
    PyDict_SetItemString(globals, "__name__", PyUnicode_FromString("__main__"));
    PyDict_SetItemString(globals, "__package__", PyUnicode_FromString(""));

    PyObject* sys_module = PyImport_ImportModule("sys");
    PyObject* sys_path = PyObject_GetAttrString(sys_module, "path");
    
    PyList_Append(sys_path, PyUnicode_FromString("."));

    PyObject* result = PyEval_EvalCode(compiled_code, globals, locals);

    if (result != NULL) {
        Py_DECREF(result);
    }

    Py_DECREF(globals);
    Py_DECREF(locals);
    Py_DECREF(compiled_code);

    Py_Finalize();

    return 0;
}
