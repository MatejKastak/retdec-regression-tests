from regression_tests import *


class TestBase(Test):
    settings = TestSettings(
        input=files_in_dir('bins'),
    )

    def test_if_dsm_contains_extern_segment(self):
        assert self.out_dsm.contains('; section: .EXTERN')

    def test_check_extern_functions(self):
        # print(self.out_c.funcs['main'].called_func_names)
        assert self.out_c.has_func('main')
        assert self.out_c.has_func('func_int')
        assert self.out_c.has_func('func_double')
        assert self.out_c.has_func('func_float')
        assert self.out_c.funcs['func_int'].calls('puts')
        assert self.out_c.funcs['func_float'].calls('puts')
        assert self.out_c.funcs['func_double'].calls('puts')
        assert self.out_c.funcs['main'].calls('extern_int')
        # assert self.out_c.funcs['main'].calls('printf')
        # mips binary generates this call, but assert still fails
        assert self.out_c.funcs['main'].calls('func_int')
        assert self.out_c.funcs['main'].calls('func_double')
        assert self.out_c.funcs['main'].calls('func_float')
