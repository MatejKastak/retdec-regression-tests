from regression_tests import *

class TestMachoUniversal(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_uni',
        args='--json --verbose'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    def test_univeral_binary_file_format(self):
        self.assertEqual(self.fileinfo.output['fileFormat'], 'Mach-O Universal Binary: [x86_64] [i386]')

    # i386 is preferred input for decompilation so should be picked
    def test_correct_architecture_pick(self):
        self.assertEqual(self.fileinfo.output['fileClass'], '32-bit')
        self.assertEqual(self.fileinfo.output['architecture'], 'x86')

    # Entry point for x86 test
    def test_analyze_entry_point_info(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['address'], '0x1dac')
        self.assertEqual(self.fileinfo.output['entryPoint']['offset'], '0x4dac')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionIndex'], '0')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionName'], '__text')

    def test_corect_number_sections_segemnts(self):
        self.assertEqual(self.fileinfo.output['declaredNumberOfSegments'], '4')
        self.assertEqual(self.fileinfo.output['declaredNumberOfSections'], '9')

class TestMachoUniversalSelection(Test):
    settings = TestSettings(
        tool='fileinfo',
        input='macho_uni',
        args='--json --fat-macho-index=0'
    )

    def setUp(self):
        assert self.fileinfo.succeeded

    # i386 is preferred input for decompilation so should be picked
    def test_correct_architecture_pick(self):
        self.assertEqual(self.fileinfo.output['fileClass'], '64-bit')
        self.assertEqual(self.fileinfo.output['architecture'], 'x86-64')

    # Entry point for selected x86-64 test
    def test_analyze_entry_point_info(self):
        self.assertEqual(self.fileinfo.output['entryPoint']['address'], '0x100000e5c')
        self.assertEqual(self.fileinfo.output['entryPoint']['offset'], '0x1e5c')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionIndex'], '0')
        self.assertEqual(self.fileinfo.output['entryPoint']['sectionName'], '__text')
